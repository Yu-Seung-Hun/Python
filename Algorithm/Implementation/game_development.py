'''게임 개발'''

# N : 맵의 세로 크기, M : 맵의 가로 크기. N x M
N, M = map(int, input().split())


# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화. 리스트 컴프리헨션 문법 사용.
# default는 0, 가본 곳은 1로 변경.
d = [[0] * M for _ in range(N)]
# 게임 캐릭터가 있는 칸의 좌표(A, B)와 바라보는 방향 d 입력
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# 방향을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만드는 것이 좋다.
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동하기
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        
        # 뒤가 바다로 막혀있는 경우
        else:
            break

        turn_time = 0


# 정답 출력
print(count)