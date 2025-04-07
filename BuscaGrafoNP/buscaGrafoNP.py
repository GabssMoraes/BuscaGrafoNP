from listaDEnc import listaDEnc

class buscaGrafoNP(object):
    def __init__(self, nos):
        self.nos = nos
    
    # SUCESSORES PARA GRAFO (LISTA DE ADJACENCIAS)
    def sucessores(self,ind,grafo,ordem):
        
        #f = []
        #for suc in grafo[ind][::ordem]:
        #    f.append(suc)
        #return f
        no_atual = self.nos[ind]
        return grafo.arestas.get(no_atual, [])[::ordem]
#------------------------------------------------------------------------------    
    # CONTROLE DE NÓS REPETIDOS
    def verificaVisitado(self,novo,nivel,visitado):
        flag = True
        # controle de nós repetidos
        for aux in visitado:
            if aux[0]==novo:
                if aux[1]<=(nivel+1):
                    flag = False
                else:
                    aux[1]=nivel+1
                break
        return flag
    #---------------------------------------------
    # BUSCA EM AMPLITUDE
    def amplitude(self,inicio,fim,nos,grafo):

        # manipular a FILA para a busca
        l1 = listaDEnc()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o primeiro da fila
            atual = l1.deletaPrimeiro()
            
            ind = nos.index(atual.estado)
            filhos = self.sucessores(ind,grafo,1)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                # verifica se foi visitado
                flag = self.verificaVisitado(novo,atual.v1,visitado)

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo,atual.v1+1,0,atual)
                    l2.insereUltimo(novo,atual.v1+1,0,atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.v1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("\nFila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return None
    #---------------------------------------------
    # BUSCA EM PROFUNDIDADE
    def profundidade(self, inicio, fim, nos, grafo):
        # manipular a PILHA para a busca
        l1 = listaDEnc()

        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()

        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)

        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)

        while l1.vazio() == False:
            # remove o último da PILHA
            atual = l1.deletaUltimo()
            
            ind = nos.index(atual.estado)
            filhos = self.sucessores(ind,grafo,-1)

            # varre todos as conexões dentro do grafo a partir de atual
            for novo in filhos:

                # verifica se foi visitado
                flag = self.verificaVisitado(novo,atual.v1,visitado)

                # se não foi visitado inclui na fila
                if flag:
                    l1.insereUltimo(novo,atual.v1+1,0,atual)
                    l2.insereUltimo(novo,atual.v1+1,0,atual)

                    # marca como visitado
                    linha = []
                    linha.append(novo)
                    linha.append(atual.v1+1)
                    visitado.append(linha)

                    # verifica se é o objetivo
                    if novo == fim:
                        caminho = []
                        caminho += l2.exibeCaminho()
                        #print("\nFila:\n",l1.exibeLista())
                        #print("\nÁrvore de busca:\n",l2.exibeLista())
                        return caminho

        return None
    #---------------------------------------------
    # BUSCA EM PROFUNDIDADE LIMITADA
    def prof_limitada(self,inicio,fim,nos,grafo,lim):
        # manipular a PILHA para a busca
        l1 = listaDEnc()
    
        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()
    
        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
    
        # controle de nós visitados
        visitado = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado.append(linha)
    
        while l1.vazio() == False:
            # remove o último da PILHA
            atual = l1.deletaUltimo()
            
            if atual.v1<lim:
                ind = nos.index(atual.estado)
                filhos = self.sucessores(ind,grafo,1)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
        
                    # verifica se foi visitado
                    flag = self.verificaVisitado(novo,atual.v1,visitado)
        
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo,atual.v1+1,0,atual)
                        l2.insereUltimo(novo,atual.v1+1,0,atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado.append(linha)
        
                        # verifica se é o objetivo
                        if novo == fim:
                            caminho = []
                            caminho += l2.exibeCaminho()
                            #print("\nFila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            return caminho
    
        return None
    #---------------------------------------------
    # BUSCA EM APROFUNDAMENTO ITERATIVO
    def aprof_iterativo(self,inicio,fim,nos,grafo,l_max):
        for lim in range(1,l_max):
            # manipular a PILHA para a busca
            l1 = listaDEnc()
        
            # cópia para apresentar o caminho (somente inserção)
            l2 = listaDEnc()
        
            # insere ponto inicial como nó raiz da árvore
            l1.insereUltimo(inicio,0,0,None)
            l2.insereUltimo(inicio,0,0,None)
        
            # controle de nós visitados
            visitado = []
            linha = []
            linha.append(inicio)
            linha.append(0)
            visitado.append(linha)
        
            while l1.vazio() == False:
                # remove o último da PILHA
                atual = l1.deletaUltimo()
                
                if atual.v1<lim:
                    ind = nos.index(atual.estado)
                    filhos = self.sucessores(ind,grafo,1)
            
                    # varre todos as conexões dentro do grafo a partir de atual
                    for novo in filhos:
            
                        # verifica se foi visitado
                        flag = self.verificaVisitado(novo,atual.v1,visitado)
            
                        # se não foi visitado inclui na fila
                        if flag:
                            l1.insereUltimo(novo,atual.v1+1,0,atual)
                            l2.insereUltimo(novo,atual.v1+1,0,atual)
            
                            # marca como visitado
                            linha = []
                            linha.append(novo)
                            linha.append(atual.v1+1)
                            visitado.append(linha)
            
                            # verifica se é o objetivo
                            if novo == fim:
                                caminho = []
                                caminho += l2.exibeCaminho()
                                #print("\nFila:\n",l1.exibeLista())
                                #print("\nÁrvore de busca:\n",l2.exibeLista())
                                return caminho
    
        return None
    #------------------------------------------------------------------------------    # BUSCA BIDIRECIONAL
    def bidirecional(self,inicio,fim,nos,grafo):
        # Primeiro Amplitude"
        # Manipular a FILA para a busca
        l1 = listaDEnc()
        # cópia para apresentar o caminho (somente inserção)
        l2 = listaDEnc()
        
        # Segundo Amplitude"
        # Manipular a FILA para a busca
        l3 = listaDEnc()
        # cópia para apresentar o caminho (somente inserção)
        l4 = listaDEnc()
    
        # insere ponto inicial como nó raiz da árvore
        l1.insereUltimo(inicio,0,0,None)
        l2.insereUltimo(inicio,0,0,None)
        
        l3.insereUltimo(fim,0,0,None)
        l4.insereUltimo(fim,0,0,None)
        
        # controle de nós visitados
        visitado1 = []
        linha = []
        linha.append(inicio)
        linha.append(0)
        visitado1.append(linha)
        
        visitado2 = []
        linha = []
        linha.append(fim)
        linha.append(0)
        visitado2.append(linha)
        
        ni = 0
        while l1.vazio()==False or l3.vazio()==False:
            
            while l1.vazio() == False:
                
                # para ir para o próximo amplitude
                if ni!=l1.primeiro().v1:
                    break
                    
                # remove o primeiro da fila
                atual = l1.deletaPrimeiro()
        
                ind = nos.index(atual.estado)
                filhos = self.sucessores(ind,grafo,1)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
        
                    # pressuponho que não foi visitado
                    flag = self.verificaVisitado(novo,atual.v1+1,visitado1)
                    # se não foi visitado inclui na fila
                    if flag:
                        l1.insereUltimo(novo,atual.v1+1,0,atual)
                        l2.insereUltimo(novo,atual.v1+1,0,atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado1.append(linha)
        
                        # verifica se é o objetivo
                        flag = not(self.verificaVisitado(novo,atual.v1+1,visitado2))
                        if flag:
                            caminho = []
                            #print("Fila:\n",l1.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            caminho += l2.exibeCaminho()
                            caminho += l4.exibeCaminho1(novo)
                            return caminho
                        
            while l3.vazio() == False:
                
                # para ir para o próximo amplitude
                if ni!= l3.primeiro().v1:
                    break
                
                # remove o primeiro da fila
                atual = l3.deletaPrimeiro()
        
                ind = nos.index(atual.estado)
                filhos = self.sucessores(ind,grafo,1)
        
                # varre todos as conexões dentro do grafo a partir de atual
                for novo in filhos:
        
                    # pressuponho que não foi visitado
                    flag = self.verificaVisitado(novo,atual.v1+1,visitado2)
                    # se não foi visitado inclui na fila
                    if flag:
                        l3.insereUltimo(novo,atual.v1+1,0,atual)
                        l4.insereUltimo(novo,atual.v1+1,0,atual)
        
                        # marca como visitado
                        linha = []
                        linha.append(novo)
                        linha.append(atual.v1+1)
                        visitado2.append(linha)
        
                        # verifica se é o objetivo
                        flag = not(self.verificaVisitado(novo,atual.v1+1,visitado1))
                        if flag:
                            caminho = []
                            #print("Fila:\n",l3.exibeLista())
                            #print("\nÁrvore de busca:\n",l4.exibeLista())
                            #print("\nÁrvore de busca:\n",l2.exibeLista())
                            caminho += l4.exibeCaminho()
                            caminho += l2.exibeCaminho1(novo)
                            return caminho[::-1]
                            
            ni += 1
    
        return "caminho não encontrado"
