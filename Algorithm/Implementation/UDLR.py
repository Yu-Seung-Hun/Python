'''
구현.
완전 탐색 : 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행
'''


'''상하좌우'''

N = int(input())
x, y = 1, 1
plans = input().split()

# U, D, L, R에 따른 이동 방향
# dx, dy 설정할때 좌표가 어떻게 변하는지 보고 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['U', 'D', 'L', 'R']


# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
        
    # 이동 수형
    x, y = nx, ny

print(x, y)