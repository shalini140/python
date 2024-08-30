def find_first_n_perfect_numbers(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input: N must be a positive integer."

    def is_perfect_number(num):
        return num > 1 and sum(d + num // d for d in range(2, int(num ** 0.5) + 1) if num % d == 0) + 1 == num

    perfect_numbers = []
    num = 2
    while len(perfect_numbers) < n:
        if is_perfect_number(num):
            perfect_numbers.append(num)
        num += 1
    
    return f"First {n} perfect numbers are: {', '.join(map(str, perfect_numbers))}"


for n in [0, 5, -2, -5, 0.2]:
    print(f"N = {n} => {find_first_n_perfect_numbers(n)}")
