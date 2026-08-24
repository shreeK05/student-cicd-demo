def analyze_performance(marks):
    """
    Analyze a student's performance using marks from 5 subjects.
    """

    if len(marks) != 5:
        raise ValueError("Exactly 5 subject marks are required.")

    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Marks must be between 0 and 100.")

    average = sum(marks) / len(marks)

    # Result
    if any(mark < 35 for mark in marks):
        result = "FAIL"
    else:
        result = "PASS"

    # Grade
    if result == "FAIL":
        grade = "F"
    elif average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "E"

    # Performance level
    if result == "FAIL":
        performance = "Needs Improvement"
    elif average >= 90:
        performance = "Outstanding"
    elif average >= 80:
        performance = "Excellent"
    elif average >= 70:
        performance = "Very Good"
    elif average >= 60:
        performance = "Good"
    else:
        performance = "Satisfactory"

    # Distinction
    distinction = result == "PASS" and average >= 75

    return {
        "average": round(average, 2),
        "grade": grade,
        "result": result,
        "performance": performance,
        "distinction": distinction
    }


if __name__ == "__main__":

    student_name = "Sai Jannawar"

    subject_marks = [
        92,  # Mathematics
        85,  # Python
        78,  # DBMS
        88,  # Operating Systems
        95   # Artificial Intelligence
    ]

    result = analyze_performance(subject_marks)

    print("Student Name:", student_name)
    print("Subject Marks:", subject_marks)
    print("Average:", result["average"])
    print("Grade:", result["grade"])
    print("Result:", result["result"])
    print("Performance:", result["performance"])
    print("Distinction:", "YES" if result["distinction"] else "NO")