def calculate_bonus_and_total_salary(grade, salary):
    try:
        salary = float(salary)
        if salary < 0:
            return "Invalid input: Salary cannot be negative."
        
        if grade == 'A':
            bonus = 0.05 * salary
        elif grade == 'B':
            bonus = 0.10 * salary
        else:
            return "Invalid input: Grade must be A or B."
        
        if salary < 10000:
            bonus += 0.02 * salary
        
        total_salary = salary + bonus
        return f"Salary={salary}\nBonus={bonus}\nTotal to be paid:{total_salary}"
    
    except ValueError:
        return "Invalid input: Salary must be a number."


print(calculate_bonus_and_total_salary('B', '50000')) 
print(calculate_bonus_and_total_salary('A', '8000'))  
print(calculate_bonus_and_total_salary('C', '60000'))  
print(calculate_bonus_and_total_salary('B', '0'))     
print(calculate_bonus_and_total_salary('38000', 'A')) 
print(calculate_bonus_and_total_salary('B', '-8000'))  
