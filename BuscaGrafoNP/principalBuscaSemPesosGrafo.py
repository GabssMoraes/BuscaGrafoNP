from buscaGrafoNP import buscaGrafoNP  

def Gera_Problema(arquivo):
    f = open(arquivo,"r")
    
    i=0
    nos = []
    grafo = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        if i==0:
            nos = str1
        else:
            grafo.append(str1)
        i += 1       
    
    return nos, grafo


# PROGRAMA PRINCIPAL
nos, grafo = Gera_Problema("romenia.txt")

#print("======== Lista de nós ========\n",nos )

sol = buscaGrafoNP()
caminho = []

origem  = input("\nOrigem......: ").upper()
destino = input("Destino.....: ").upper()


if origem not in nos or destino not in nos:
    print("Cidade não está na lista")
else:
    caminho = sol.amplitude(origem,destino,nos,grafo)
    if caminho!=None:
        print("\n*****AMPLITUDE*****")
        print("Caminho: ",caminho)
        print("Custo..: ",len(caminho)-1)
    else:
        print("CAMINHO NÃO ENCONTRADO")
      
    caminho = sol.profundidade(origem,destino,nos,grafo)
    if caminho!=None:
        print("\n*****PROFUNDIDADE*****")
        print("Caminho: ",caminho)
        print("Custo..: ",len(caminho)-1)
    else:
        print("CAMINHO NÃO ENCONTRADO")

    limite = 5
    caminho = sol.prof_limitada(origem,destino,nos,grafo,limite)
    if caminho!=None:
        print("\n*****PROFUNDIDADE LIMITADA*****")
        print("Caminho: ",caminho)
        print("Custo..: ",len(caminho)-1)
    else:
        print("CAMINHO NÃO ENCONTRADO")
        
    l_max = len(nos)
    caminho = sol.aprof_iterativo(origem,destino,nos,grafo,l_max)
    if caminho!=None:
        print("\n*****APROFUNDAMENTO ITERATIVO*****")
        print("Caminho: ",caminho)
        print("Custo..: ",len(caminho)-1)
    else:
        print("CAMINHO NÃO ENCONTRADO")
     
    caminho = sol.bidirecional(origem,destino,nos,grafo)
    if caminho!=None:
        print("\n*****BIDIRECIONAL*****")
        print("Caminho: ",caminho)
        print("Custo..: ",len(caminho)-1)
    else:
        print("CAMINHO NÃO ENCONTRADO")
    