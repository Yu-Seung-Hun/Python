'''큰 수의 법칙'''

# N : 배열의 크기, M : 숫자가 더해지는 횟수, K : 연속 가능한 횟수
N, M, K = map(int, input().split()) # 5 6 2

data = list(map(int, input().split())) # 1 5 2 3 4

data.sort() # 1 2 3 4 5

first = data[-1] # 5. 가장 큰 수
second = data[-2] # 4. 두 번째로 큰 수

result = 0
count = 0

while True:
    for i in range(K): # 가장 큰 수를 K번 더하기
        if M == 0: # M이 0이라면 반복문 탈출
            break
        result += first
        M -= 1 # 더할 때마다 1씩 빼기
    
    if M == 0:
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    M -= 1 # 더할 때마다 1씩 빼기

print(result)