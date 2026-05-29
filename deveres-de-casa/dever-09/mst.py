import time

class Grafo:
    def __init__(self, vertices):
        self.v = vertices
        self.grafo = []

    def adicionar_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

    def buscar_raiz(self, pai, i):
        if pai[i] == i:
            return i
        pai[i] = self.buscar_raiz(pai, pai[i])
        return pai[i]

    def unir_redes(self, pai, rank, x, y):
        raiz_x = self.buscar_raiz(pai, x)
        raiz_y = self.buscar_raiz(pai, y)

        if rank[raiz_x] < rank[raiz_y]:
            pai[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            pai[raiz_y] = raiz_x
        else:
            pai[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def executar_kruskal(self):
        resultado = []
        i = 0  
        e = 0  
        custo_total = 0

        self.grafo = sorted(self.grafo, key=lambda item: item[2], reverse=True)

        pai = []
        rank = []

        for no in range(self.v):
            pai.append(no)
            rank.append(0)

        while e < self.v - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.buscar_raiz(pai, u)
            y = self.buscar_raiz(pai, v)

            if x != y:
                e = e + 1
                resultado.append([u, v, w])
                custo_total += w
                self.unir_redes(pai, rank, x, y)

        return resultado, custo_total

if __name__ == '__main__':
    g = Grafo(8)

    g.adicionar_aresta(4, 7, 1)
    g.adicionar_aresta(5, 6, 2)
    g.adicionar_aresta(4, 5, 3)
    g.adicionar_aresta(6, 7, 4)
    g.adicionar_aresta(0, 1, 5)
    g.adicionar_aresta(3, 7, 6)
    g.adicionar_aresta(2, 5, 7)
    g.adicionar_aresta(2, 6, 8)
    g.adicionar_aresta(1, 2, 9)
    g.adicionar_aresta(1, 6, 10)
    g.adicionar_aresta(1, 5, 11)
    g.adicionar_aresta(1, 7, 13)
    g.adicionar_aresta(1, 4, 14)
    g.adicionar_aresta(0, 4, 15)
    g.adicionar_aresta(0, 3, 16)
    g.adicionar_aresta(3, 6, 17)
    g.adicionar_aresta(0, 7, 18)

    inicio = time.perf_counter()
    
    caminho_final, custo_final = g.executar_kruskal()
    
    fim = time.perf_counter()
    tempo_execucao = (fim - inicio) * 1000 

    print("--- RESULTADO DA ÁRVORE GERADORA MÁXIMA ---")
    print("Rotas escolhidas para a rede:")
    for u, v, peso in caminho_final:
        print(f"Rota da cidade {u} para a cidade {v} | Custo: {peso}")
    print(f"\nCusto Total da Obra: {custo_final}")
    print(f"Tempo de execução: {tempo_execucao:.4f} milissegundos")