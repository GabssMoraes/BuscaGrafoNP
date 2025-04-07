import tkinter as tk
from tkinter import ttk, messagebox
from buscaGrafoNP import buscaGrafoNP
from listaDEnc import listaDEnc
from node import Node
import random
import math

class principalComGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Algoritmos de Busca")

        self.grafo = self.carregar_grafo("BuscaGrafoNP/romenia.txt")
        self.origem = tk.StringVar()
        self.destino = tk.StringVar()
        self.algoritmo = tk.StringVar()

        self.coord_nos = {}
        self.arestas_com_peso = {}

        self.criar_interface()
        self.distribuir_nos()
        self.desenhar_grafo()

    def criar_interface(self):
        estilo = ttk.Style()
        estilo.configure("TButton", font=("Arial", 10))
        estilo.configure("TLabel", font=("Arial", 10))

        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        painel_opcoes = ttk.LabelFrame(frame, text="Configuração da Busca", padding=10)
        painel_opcoes.pack(pady=10)

        ttk.Label(painel_opcoes, text="Origem:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        cb_origem = ttk.Combobox(painel_opcoes, textvariable=self.origem, values=list(self.grafo.keys()), state="readonly")
        cb_origem.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(painel_opcoes, text="Destino:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        cb_destino = ttk.Combobox(painel_opcoes, textvariable=self.destino, values=list(self.grafo.keys()), state="readonly")
        cb_destino.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(painel_opcoes, text="Algoritmo:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        cb_algoritmo = ttk.Combobox(painel_opcoes, textvariable=self.algoritmo,
                                    values=["Amplitude", "Profundidade", "Profundidade Limitada",
                                            "Aprofundamento Iterativo", "Bidirecional"],
                                    state="readonly")
        cb_algoritmo.grid(row=2, column=1, padx=5, pady=5)

        btn_frame = ttk.Frame(painel_opcoes)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

        btn_buscar = ttk.Button(btn_frame, text="Buscar", command=self.executar_busca)
        btn_buscar.grid(row=0, column=0, padx=5)

        btn_resetar = ttk.Button(btn_frame, text="Limpar", command=self.resetar_interface)
        btn_resetar.grid(row=0, column=1, padx=5)

        self.label_resultado = ttk.Label(self.root, text="Resultado:")
        self.label_resultado.pack(pady=5)

        self.canvas = tk.Canvas(self.root, width=700, height=500, bg="white")
        self.canvas.pack(padx=10, pady=10)

        self.status_bar = ttk.Label(self.root, text="Pronto", relief="sunken", anchor="w")
        self.status_bar.pack(fill="x", side="bottom")

    def carregar_grafo(self, arquivo):
        grafo = {}
        try:
            with open(arquivo, "r") as f:
                for linha in f:
                    a, b = linha.strip().split()
                    grafo.setdefault(a, []).append(b)
                    grafo.setdefault(b, []).append(a)
        except FileNotFoundError:
            messagebox.showerror("Erro", f"Arquivo '{arquivo}' não foi localizado.")
        return grafo

    def distribuir_nos(self):
        largura, altura = 700, 500
        margem = 50
        for cidade in self.grafo:
            while True:
                x = random.randint(margem, largura - margem)
                y = random.randint(margem, altura - margem)
                if all(math.hypot(x - x2, y - y2) > 50 for x2, y2 in self.coord_nos.values()):
                    self.coord_nos[cidade] = (x, y)
                    break

    def criar_lista_adj(self):
        lista = listaDEnc()
        for origem, destinos in self.grafo.items():
            for destino in destinos:
                lista.adicionar_aresta(origem, destino)
        return lista

    def executar_busca(self):
        inicio = self.origem.get()
        fim = self.destino.get()
        metodo = self.algoritmo.get()

        if not inicio or not fim or not metodo:
            messagebox.showwarning("Aviso", "Todos os campos precisam ser preenchidos.")
            return

        listaAdj = self.criar_lista_adj()
        nos = list(self.grafo.keys())
        busca = buscaGrafoNP(nos)
        caminho = []
        limProfLimi = 10
        limAprofIte = 30
        if metodo == "Amplitude":
            caminho = busca.amplitude(inicio, fim, nos, listaAdj)
        elif metodo == "Profundidade":
            caminho = busca.profundidade(inicio, fim, nos, listaAdj)
        elif metodo == "Profundidade Limitada":
            caminho = busca.prof_limitada(inicio, fim, nos, listaAdj, limProfLimi)
        elif metodo == "Aprofundamento Iterativo":
            caminho = busca.aprof_iterativo(inicio, fim, nos, listaAdj, limAprofIte)
        elif metodo == "Bidirecional":
            caminho = busca.bidirecional(inicio, fim, nos, listaAdj)

        texto = f"Resultado: {' -> '.join(caminho) if caminho else 'Caminho não encontrado.'}"
        self.label_resultado.config(text=texto)
        self.status_bar.config(text="Busca concluída")
        self.desenhar_grafo(caminho=caminho, origem=inicio, destino=fim)

    def desenhar_grafo(self, caminho=None, origem=None, destino=None):
        self.canvas.delete("all")
        raio = 20

        for cidade, vizinhos in self.grafo.items():
            x1, y1 = self.coord_nos[cidade]
            for vizinho in vizinhos:
                x2, y2 = self.coord_nos[vizinho]
                cor = "gray"
                if caminho and cidade in caminho and vizinho in caminho:
                    idx1, idx2 = caminho.index(cidade), caminho.index(vizinho)
                    if abs(idx1 - idx2) == 1:
                        cor = "blue"
                self.canvas.create_line(x1, y1, x2, y2, fill=cor, width=2)

        for cidade, (x, y) in self.coord_nos.items():
            if cidade == origem:
                cor = "green"
            elif cidade == destino:
                cor = "red"
            elif caminho and cidade in caminho:
                cor = "skyblue"
            else:
                cor = "white"
            self.canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill=cor, outline="black", width=2)
            self.canvas.create_text(x, y, text=cidade, font=("Arial", 11, "bold"))

    def resetar_interface(self):
        self.origem.set("")
        self.destino.set("")
        self.algoritmo.set("")
        self.label_resultado.config(text="Resultado:")
        self.status_bar.config(text="Pronto")
        self.desenhar_grafo()

if __name__ == "__main__":
    root = tk.Tk()
    app = principalComGUI(root)
    root.mainloop()
