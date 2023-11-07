'''큰 수의 법칙'''

# N : 배열의 크기, M : 숫자가 더해지는 횟수, K : 연속 가능한 횟수
N, M, K = map(int, input().split()) # 5 6 2

data = list(map(int, input().split())) # 1 5 2 3 4

data.sort() # 1 2 3 4 5

first = data[-1] # 5. 가장 큰 수
second = data[-2] # 4. 두 번째로 큰 수


# 가장 큰 수가 더해지는 횟수 계산
count = int(M / (K+1)) * K
count += M % (K+1) # M이 K+1로 나누어지지 않을때 나머지만큼 first가 추가로 더해짐

result = 0
result += (count) * first # 가장 큰 수 더하지
result += (M - count) * second # 두 번째로 큰 수 더하기


print(result)