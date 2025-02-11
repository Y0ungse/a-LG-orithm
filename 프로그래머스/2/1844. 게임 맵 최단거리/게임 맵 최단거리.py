from collections import deque

def solution(maps):
    # 맵 크기
    n, m = len(maps), len(maps[0])

    # 방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문 여부 체크 배열
    visited = [[False] * m for _ in range(n)]
    
    def bfs():
        queue = deque([(0, 0)])  # 시작 위치
        visited[0][0] = True  # 방문 체크

        while queue:
            x, y = queue.popleft()

            # 도착지 확인
            if x == n - 1 and y == m - 1:
                return maps[x][y]

            # 4방향 탐색
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                # 범위 체크 & 방문 체크 & 벽이 아닐 때만 이동
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1  # 거리 증가
                    visited[nx][ny] = True  # 방문 체크
                    queue.append((nx, ny))  # 큐에 추가

        return -1  # 도달할 수 없는 경우

    return bfs()
