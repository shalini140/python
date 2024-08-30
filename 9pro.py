def factors(num):
    count = 0
    factor_list = []
    for i in range(1, abs(num) + 1):
        if num % i == 0:
            count += 1
            factor_list.append(i)
    return count, factor_list

num = int(input("Given Number: "))
n = int(input("N: "))

count, factor_list = factors(num)

print("Number of factors =", count)
if n > 0 and n <= count:
    print(f"{n}th factor of {num} =", factor_list[n - 1])
else:
    print("Invalid N")
