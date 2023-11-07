'''숫자 카드 게임'''

# N : 행의 개수, M : 열의 개수

N, M = map(int, input().split())

result = 0

# 한 줄씩 입력받기
for i in range(N):
    data = list(map(int, input().split()))
    min_data = min(data) # 현재 줄에서 가장 작은 수 찾기
    result = max(result, min_data) # 행에 있는 가장 작은 수들 중 가장 큰 수 찾기

print(result) # 최종결과 출력