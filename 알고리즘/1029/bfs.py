import sys
sys.stdin = open('input.txt')

def bfs(x,y):
    global re
    q = [(x,y)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = 1
    while q:
        (x, y) = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if mazz[nx][ny] == 3:
                    re = 1
                    return
                if mazz[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    for k in visited:
                        print(*k)
                    print()
                    q.append((nx,ny))

for tc in range(1,int(input())+1):
    n = int(input())
    mazz = [list(map(int, input())) for _ in range(n)]

    visited = [[0]*n for _ in range(n)]
    re = 0
    for i in range(n):
        for j in range(n):
            if mazz[i][j] == 2:
                bfs(i,j)
                break
            else:
                re = 0

    if re == 1:
        print('#{} {}'.format(tc,1))
    else:
        print('#{} {}'.format(tc,0))