INF = 9999999
V = 5
G = [
    [INF, 9, 4, 6, INF],
    [9, INF, INF, 7, 2],
    [4, INF, INF, 5, 6],
    [6, 7, 5, INF, 8],
    [INF, 2, 6, 8, INF]
]

selected = [False] * V
selected[0] = True
no_edge = 0
cost = 0

print("Edge : Weight")
while no_edge < V - 1:
    min_val = INF
    x = y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if not selected[j] and G[i][j] != INF:
                    if min_val > G[i][j]:
                        min_val = G[i][j]
                        x, y = i, j
    print(f"{x + 1} - {y + 1} : {G[x][y]}")
    cost += G[x][y]
    selected[y] = True
    no_edge += 1
print(f"Загальна вартість: {cost}")
