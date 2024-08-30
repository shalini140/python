def calculate_student_users(total_users, staff_users):
    if total_users < 0 or staff_users < 0:
        return "Invalid input: Total users and staff users must be non-negative."
    non_teaching_staff_users = staff_users // 3
    if total_users < staff_users + non_teaching_staff_users:
        return "Invalid input: Total users cannot be less than the sum of staff and non-teaching staff users."
    student_users = total_users - staff_users - non_teaching_staff_users
    if student_users < 0:
        return "Invalid input: Number of student users cannot be negative."
        return f"Student Users: {student_users}"
print(calculate_student_users(856, 126))  
print(calculate_student_users(0, 0))      
print(calculate_student_users(-143, 0))   
print(calculate_student_users(1026, 1026))
print(calculate_student_users(450, 540))  
print(calculate_student_users(600, 450))  
