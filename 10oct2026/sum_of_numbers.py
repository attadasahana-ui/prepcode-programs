num = 90817
total = 0

while num > 0:
    last_num = num % 10
    num = num//10
    total = total + last_num

    print(total)