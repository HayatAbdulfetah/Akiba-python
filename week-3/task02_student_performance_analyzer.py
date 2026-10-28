def validate(students):
    for student in students:
        score = student["score"]
        if score < 0 or score > 100:
            raise ValueError(
                f"Invalid score for {student['name']}: {score}"
            )
    return True

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def calculate_average(students):
    if len(students) == 0:
        raise ValueError("Student list cannot be empty.")
    total = 0
    for student in students:
        total += student["score"]
    average = total/len(students)
    return average

def largest_and_smallest(students):
    if len(students) == 0:
        raise ValueError("Student list cannot be empty.")
    largest=students[0]["score"]
    smallest=students[0]["score"]
    for student in students:
        if student["score"] > largest:
            largest=student["score"]

        if student["score"] < smallest:
            smallest=student["score"]
    return largest,smallest

def passed_and_failed(students):
    passed_count = 0
    failed_count = 0

    for student in students:
        if student["score"] >= 50:
            passed_count+=1
        else:
            failed_count += 1
    return passed_count,failed_count

def generate_report(students):
    validate(students)

    average = calculate_average(students)
    largest,smallest = largest_and_smallest(students)
    passed,failed = passed_and_failed(students)

    above_average = []

    print("======= STUDENT SCORE =======")
    for student in students:
        name = student["name"]
        score = student["score"]
        grade = calculate_grade(score)

        print(f"{name}: {score} - Grade {grade}")

        if score > average:
            above_average.append(student)
    print("--------------------------------")
    print(f"Class average: {average:.2f}")
    print(f"Highest score: {largest}")
    print(f"Lowest score: {smallest}")
    print(f"Passed students: {passed}")
    print(f"Failed students: {failed}")
    print("------------------------------------------")

    print("Students above class average:")
    for student in above_average:
        print(f"{student['name']}: {student['score']}")

    return above_average


students = [
    {"name": "Jude", "score": 83},
    {"name": "Reyan", "score": 45},
    {"name": "Anna", "score": 93},
    {"name": "Hayat", "score": 77}
]

generate_report(students)