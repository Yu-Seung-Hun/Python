'''숫자 카드 게임'''

# N : 행의 개수, M : 열의 개수

N, M = map(int, input().split())

result = 0

# 한 줄씩 입력받기
for i in range(N):
    data = list(map(int, input().split()))
    min_data = 10001
    for a in data:
        min_data = min(min_data, a)
    
    result = max(result, min_data)

print(result) # 최종결과 출력