import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Passo 1: Carregar os dados do CSV
df = pd.read_csv('rules.csv', index_col=1)

# Passo 2: Converter os valores para float, tratando valores não numéricos como zero
association_matrix = df.applymap(lambda x: float(x) if str(x).replace('.', '', 1).isdigit() else 0)

# Passo 3: Criar um grafo a partir da matriz de associação
G = nx.Graph()

# Passo 4: Adicionar nós ao grafo
for item in df.index:
    G.add_node(item)

# Passo 5: Adicionar arestas ao grafo
for i, item1 in enumerate(df.index):
    for j, item2 in enumerate(df.columns):
        if i != j:  # Evita adicionar laços (self-loops)
            weight = association_matrix.iloc[i, j]
            if weight > 0:  # Adiciona apenas as arestas com associações positivas
                G.add_edge(item1, item2, weight=weight)

# Passo 6: Desenhar o grafo
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Layout para posicionar os nós
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=10, font_weight='bold')

# Passo 7: Exibir o gráfico
plt.title('Diagrama de Rede da Matriz de Associação')
plt.show()
