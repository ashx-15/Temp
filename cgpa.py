def calculate_cgpa():
    # Prompt user for the number of courses
    num_courses = int(input("Enter the number of courses: "))

    # Initialize the total grade points
    total_grade_points = 0

    # Iterate to get grade points for each course
    for i in range(num_courses):
        # Input grade points for each course
        grade_point = float(input(f"Enter grade point for course {i+1}: "))
        total_grade_points += grade_point

    # Calculate CGPA
    cgpa = total_grade_points / num_courses

    # Display the result
    print(f"Your CGPA is: {cgpa:.2f}")

# Call the function to calculate CGPA
calculate_cgpa()
