import sys
sys.stdin = open('input.txt')

t = int(input())

def bfs(x,y):
    global cnt
    if x == n-1 and y == n-1:
        result.append(cnt)
        return
    dx = [1,0]
    dy = [0,1]
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            visited[nx][ny] += 1
            cnt += matrix[nx][ny]
            dfs(nx,ny)
            visited[nx][ny] = 0
            cnt -= matrix[nx][ny]

for tc in range(1,t+1):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    cnt = matrix[0][0]
    result = []
    visited[0][0] = 1
    dfs(0,0)
    print('#{} {}'.format(tc,min(result)))