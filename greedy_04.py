'''
1이 될 대가지

어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두 번째 연산은 N이 K로 나누어떨어질 때만
선택할 수 있다.
  1. N에서 1을 뺀다.
  2. N을 K로 나눈다.
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 구하시오.

입력 ----
  - 첫째 줄에 N(2 <= N <= 100000)과 K (2 <= K <= 100000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은
   항상 K보다 크거나 같다.

출력 ----
  - 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.

입력 예시                           출력 예시
25 5                               2
'''
def function(n, k):
    if n==1:
        return n
    else:
        if n % k == 0:
            return n // k
        else:
            return n - 1

n, k = map(int, input("N, K 입력 : ").split())

cnt = 0
while n != 1:
    if n==1:
        break;
    else:
        if n % k == 0:
            n //= k
        else:
            n -= 1
        cnt+=1;

print(cnt)

'''
# 답안 2
n, k = map(int, input("N, K 입력 : ").split());
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    result += 1

print(result)

# 답안 3
n, k = map(int, input("N, K 입력 : ").split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k
result += (n-1)
print(result)
'''