def print_hollow_square(size, symbol):
    for i in range(size):
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        print()

symbol = input("Enter the symbol: ")
size = int(input("Enter the size of the square: "))

print_hollow_square(size, symbol)
