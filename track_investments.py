#Assignment: Track your investments p61

def invest(amount, rate, time):
    print("principal amount: ", amount)
    print("annual rate of return: ", rate)
    for i in range(1, time + 1):
        amount += amount * rate
        print(f'year {i}:', amount)

invest(100, 0.05, 8)
invest(2000, 0.025, 5)
