'''
== 큰 수의 법칙 ==
다양한 수로 이루어진 배열이 있을 때주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 단, 배열의 특정한 인덱스에 해당하는 수가
연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
-- 규칙
1. 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며 각 자연수는 공백으로 구분한다.
2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10000이하의 수로 주어진다.
3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.
'''

n, m, k = map(int, input("N, M, K : ").split())
data = list(map(int, input("배열 : ").split()))

data.sort()
first = data[n-1]
second = data[n-2]

times = m // (k+1)
rest  = m % (k+1)

result = (first * k + second) * times + rest * first

print("조합할 수 있는 가장 큰 수는 {}입니다.".format(result))


