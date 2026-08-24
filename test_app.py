from app import calculate_grade


def test_grade_a():
    assert calculate_grade(95) == "A"


def test_grade_b():
    assert calculate_grade(80) == "B"


def test_grade_c():
    assert calculate_grade(65) == "C"


def test_grade_d():
    assert calculate_grade(45) == "D"


def test_fail_student():
    assert calculate_grade(30) == "FAIL"