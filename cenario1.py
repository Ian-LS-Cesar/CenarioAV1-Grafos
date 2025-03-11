from collections import deque

def bfs_caminho_mais_curto(grafo, partida, chegada):
    # Guardar os vértices explorados
    vertices_explorados = []
    # Guardar todos os caminhos para checar
    fila = deque([[partida]])
    
    # Retornar o caminho se a partida for a chegada
    if partida == chegada:
        return [partida]
    
    # Fazer loop até que todos os caminhos sejam checados
    while fila:
        # Tirar o primeiro caminho da fila
        caminho = fila.popleft()
        # Pegar o último nó do caminho
        vertice = caminho[-1]
        if vertice not in vertices_explorados:
            vizinhos = grafo[vertice]
            # Ir para todos os vértices vizinhos, construir um novo caminho e
            # colocá-lo na fila
            for vizinho in vizinhos:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                
                # Retornar o caminho se o vizinho for a chegada
                if vizinho == chegada:
                    return novo_caminho
            # Marcar o vertice como explorado
            vertices_explorados.append(vertice)
    
    # Caso não haja caminho entre os 2 vértices
    return None

# Exemplo de grafo usando lista de ajdacência
grafo = {
    'A': ['B', 'N'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'G'],
    'G': ['F', 'H'],
    'H': ['G', 'I'],
    'I': ['H', 'J'],
    'J': ['I', 'K'],
    'K': ['J', 'L'],
    'L': ['K', 'M'],
    'M': ['L', 'N'],
    'N': ['M', 'A']
}

partida = input("Digite o vértice de partida do Fantasma (A - N): ") 
chegada = input("Digite o vértice de chegada do Fantasma (A - N): ")   

caminho = bfs_caminho_mais_curto(grafo, partida, chegada)
print(f"O caminho mais curto de {partida} para {chegada} é: {caminho}")