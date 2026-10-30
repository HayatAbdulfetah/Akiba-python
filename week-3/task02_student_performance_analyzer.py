def validate_score(score):
    # Validates that a score is between 0 and 100.
    if not (0 <= score <= 100):
        raise ValueError(f"Invalid score: {score}. Must be between 0 and 100.")
    return True

def calculate_grade(score):
    # Returns the letter grade for a given score based on criteria.
    validate_score(score)
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
    if not students:
        return 0
    total_score = 0
    count = 0
    for student in students:
        total_score += student["score"]
        count += 1
    return total_score / count

def find_highest_lowest(students):
    if not students:
        return None, None
        
    highest = students[0]["score"]
    lowest = students[0]["score"]
    
    for student in students:
        score = student["score"]
        if score > highest:
            highest = score
        if score < lowest:
            lowest = score
            
    return highest, lowest

def count_pass_fail(students, passing_score=50):
    passed = 0
    failed = 0
    for student in students:
        if student["score"] >= passing_score:
            passed += 1
        else:
            failed += 1
    return passed, failed


def get_above_average_students(students, average):
    above_average = []
    for student in students:
        if student["score"] > average:
            above_average.append(student)
    return above_average

def generate_report(students):
    try:
        # Pre-validate all scores to ensure data integrity before reporting
        for student in students:
            validate_score(student["score"])
            
        # Run calculation functions
        avg_score = calculate_average(students)
        highest, lowest = find_highest_lowest(students)
        passed, failed = count_pass_fail(students)
        above_avg_list = get_above_average_students(students, avg_score)
        
        # 1. Print Student Grade Breakdown Table
        print("\n" + "="*40)
        print(f"{'STUDENT PERFORMANCE REPORT':^40}")
        print("="*40)
        print(f"{'Name':<15} {'Score':<10} {'Grade':<10}")
        print("-"*40)
        for student in students:
            grade = calculate_grade(student["score"])
            print(f"{student['name']:<15} {student['score']:<10} {grade:<10}")
            
        # 2. Print Summary Metrics
        print("-"*40)
        print(f"{'Class Average:':<25} {avg_score:>6.2f}")
        print(f"{'Highest Score:':<25} {highest:>6}")
        print(f"{'Lowest Score:':<25} {lowest:>6}")
        print(f"{'Passed Students:':<25} {passed:>6}")
        print(f"{'Failed Students:':<25} {failed:>6}")
        print("="*40)
        
        # 3. Print Challenge Feature Results
        print(f"{'STARS (ABOVE AVERAGE)':^40}")
        print("-"*40)
        for student in above_avg_list:
            print(f" * {student['name']:<15} (Score: {student['score']})")
        print("="*40 + "\n")
        
        return {
            "average": avg_score,
            "highest": highest,
            "lowest": lowest,
            "passed": passed,
            "failed": failed,
            "above_average": above_avg_list
        }
        
    except ValueError as e:
        print(f"\n[Data Error]: {e}\n")
        return None


students_data = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]

generate_report(students_data)
