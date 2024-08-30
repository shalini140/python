def calculate_interest(principal, years, senior_citizen=False):
    rate = 0.12 if senior_citizen else 0.10
    return principal * rate * years


principal = float(input("Enter the principal amount: "))
years = int(input("Enter the no of years: "))
senior_citizen = input("Is customer senior citizen (y/n): ").lower() == 'y'


interest = calculate_interest(principal, years, senior_citizen)
print("Interest:", interest)
