N_COINS = 4
coins = [500, 100, 50, 10]

income = int(input("거스름돈 : "))

amount = []

if (income//10 != 0):
    print('입력하신 금액은 {}원 입니다. 내림하여  {}으로 계산합니다.'.format(income, (income//10)*10))
    income = (income // 10) * 10

for coin in coins:
    amount.append(income//coin)
    income %= coin

print('거슬러 줄 동전은 {}원짜리 {}개, {}원짜리 {}개, {}원짜리 {}개, {}원짜리 {}개, 총 {}개 입니다.'.format(coins[0], amount[0],
                                                                                coins[1], amount[1], coins[2], amount[2],
                                                                                coins[3], amount[3], sum(amount)))
