grade_data = float(input())


def grading(grade):
    if 6 >= grade >= 5.50:
        return 'Excellent'
    elif 4.50 <= grade < 5.50:
        return 'Very Good'
    elif 3.50 <= grade < 4.50:
        return 'Good'
    elif 3.00 <= grade < 3.50:
        return 'Poor'
    elif 2.00 <= grade < 3.00:
        return 'Fail'


print(grading(grade_data))
