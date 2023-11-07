import sys
sys.stdin = open("input.txt", "r")

 
T = int(input()) # 전체 TC 갯수

for test_case in range(1, T + 1): # TC마다
    M = int(input()) #배열의 길이
    answer = 0 #출력할 정답
    arr = list(map(int, input().split())) #배열 입력 받기
    sellPrice = 0 #현재 판매가격(최댓값)

    for val in arr[::-1]: # 배열 거꾸로 순회
        if val >= sellPrice: #현재 값이 최댓값보다 크거나 같다면
            sellPrice = val #최댓값 업데이트
        else:
            answer += sellPrice - val #아니라면 정답값에 가격차이를 더한다. (현재 값에 구매해서 최댓값에 판다)
    print("#", test_case, " ", answer, sep="") #출력 양식에 맞춰서 출력



# 앞에서부터 살핀다면, 오늘보다 비싼 가격이 나올 때까지 값을 계속 저장하고 있어야하는데, 
# 뒤에서부터 살핀다면 지금보다 가격이 낮았을 때만을 찍어서 보면 되니까 훨씬 간단할 것 같다는 생각을 해야함