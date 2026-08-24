def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "FAIL"


if __name__ == "__main__":
    marks = 86
    grade = calculate_grade(marks)

    print("Student Marks:", marks)
    print("Student Grade:", grade)