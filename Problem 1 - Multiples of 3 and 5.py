def multiplesOf3and5(number):
    total = 0
    for x in range(0, number):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    
    print(total)

multiplesOf3and5(10)