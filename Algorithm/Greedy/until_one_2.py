'''1이 될 때까지'''

# N : 1을 만들기 위한 수, K : N을 1로 만들기 위해 연산되는 수

N, K = map(int, input().split())

count = 0

while True:
    if N == 1:
        break

    if (N % K) == 0:
        N //= K
        count += 1
    else:
        N -= 1
        count += 1

print(count)