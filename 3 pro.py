def convert_decimal(decimal_number):
    try:
        decimal_number = int(decimal_number)
        return f"Binary Number = {bin(decimal_number)[2:]}\nOctal = {oct(decimal_number)[2:]}"
    except ValueError:
        return "Invalid input: Please enter a valid integer."
inputs = ["15", "111", "15.2", "0", "B12", "1A.2"]
for inp in inputs:
    print(f"Input: {inp} => {convert_decimal(inp)}")
