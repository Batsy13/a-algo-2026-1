import heapq

def prim(grafo, inicio):
    mst = []
    visitados = {inicio}
    arestas = [(custo, inicio, destino) for destino, custo in grafo[inicio].items()]
    heapq.heapify(arestas)
    custo_total = 0

    while arestas:
        custo, origem, destino = heapq.heappop(arestas)
        if destino not in visitados:
            visitados.add(destino)
            mst.append((origem, destino, custo))
            custo_total += custo

            for prox_destino, prox_custo in grafo[destino].items():
                if prox_destino not in visitados:
                    heapq.heappush(arestas, (prox_custo, destino, prox_destino))

    return mst, custo_total

grafo = {
    'A': {'B': 4, 'C': 4},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 5, 'E': 6},
    'D': {'B': 5, 'C': 5, 'E': 4, 'F': 4},
    'E': {'C': 6, 'D': 4, 'F': 2},
    'F': {'D': 4, 'E': 2}
}

rota, custo_total = prim(grafo, 'A')

print("Rota dos cabos (em ordem):")
for origem, destino, custo in rota:
    print(f"{origem} -> {destino}: {custo} Km")
    
print(f"\nQuantidade total mínima de cabos: {custo_total} Km")