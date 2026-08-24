import pytest
from app import analyze_performance


def test_outstanding_student():
    marks = [95, 92, 94, 96, 98]

    result = analyze_performance(marks)

    assert result["average"] == 95.0
    assert result["grade"] == "A+"
    assert result["result"] == "PASS"
    assert result["performance"] == "Outstanding"
    assert result["distinction"] is True


def test_excellent_student():
    marks = [82, 85, 80, 84, 89]

    result = analyze_performance(marks)

    assert result["grade"] == "A"
    assert result["result"] == "PASS"
    assert result["performance"] == "Excellent"


def test_good_student():
    marks = [65, 68, 72, 64, 71]

    result = analyze_performance(marks)

    assert result["grade"] == "A"
    assert result["result"] == "PASS"
    assert result["performance"] == "Good"


def test_average_student():
    marks = [55, 58, 52, 61, 57]

    result = analyze_performance(marks)

    assert result["grade"] == "D"
    assert result["result"] == "PASS"
    assert result["distinction"] is False


def test_failed_student():
    marks = [80, 75, 30, 85, 90]

    result = analyze_performance(marks)

    assert result["result"] == "FAIL"
    assert result["grade"] == "F"
    assert result["performance"] == "Needs Improvement"
    assert result["distinction"] is False


def test_invalid_number_of_subjects():
    marks = [80, 75, 90]

    with pytest.raises(ValueError):
        analyze_performance(marks)


def test_invalid_marks():
    marks = [80, 75, 110, 85, 90]

    with pytest.raises(ValueError):
        analyze_performance(marks)