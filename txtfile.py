def enter_grades(filename):
    with open(filename, "w") as file:
        grades = []
        while True:
            grade = input("Enter a grade (or 'q' to finish): ")
            if grade.lower() == 'q':
                break
            elif grade.replace(".", "", 1).isdigit():
                grade = float(grade)
                grades.append(grade)
                file.write(f"{grade}\n")
            else:
                print("Invalid input. Please enter a valid number.")

        if grades:
            average = sum(grades) / len(grades)
            print(f"Class Average: {average:.2f}")
        else:
            print("No grades entered.")

filename = "grades.txt"
enter_grades(filename)