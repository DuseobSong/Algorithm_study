'''
=====   상하좌우   =====
여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다. 이 공간은  1 x 1 크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좌표는 (1, 1)
이며, 기징 오른쪽 아래 좌표는 (N, N)이다. 여행가는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다. 우리 앞에는
여행가가 이동할 계획이 적힌 계획서가 놓여있다.

계획서에는 하나의 줄에 띄어스기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있다. 각 문자의 의미는 다음과 같다.
 - L:  왼쪽으로 한 칸 이동
 - R:  오른쪽으로 한 칸 이동
 - U:  위로 한 칸 이동
 - D:  아래로 한 칸 이동
이때, 여행가가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.

입력조건 ----
 1. 첫재 줄에 공간의 크기를 나타내는 N이 주어진다. ( 1 <= N <= 100)
 2. 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. ( 1 <= 이동 횟수 <= 100)

출력조건 ----
 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다.

입력 예시                       출력 예시
5                              3 4
R R R U D D
'''
x, y = 1, 1
n = map(int, input("정사각형의 크기 : "))
plans = input("계획서 : ").split()

moves = ['L', 'R', 'U', 'D']

for plan in plans:
    if plan == moves[0]:
        if(x == 1):
            continue
        else:
            x -= 1
    elif plan == moves[1]:
        if(x == n):
            continue
        else:
            x += 1
    elif plan == moves[2]:
        if(y == 1):
            continue
        else:
            y -= 1
    elif plan == moves[3]:
        if(y == n):
            continue
        else:
            y += 1

print('{} {}'.format(x, y))

'''
# 답안
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x = dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

print(nx, ny)
'''