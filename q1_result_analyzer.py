def analyze_result(name, roll, marks):
    total_marks = sum(marks)
    average_marks = total_marks / len(marks)

    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 75:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    elif average_marks >= 40:
        grade = "D"
    else:
        grade = "Fail"
        
    print(f"Student: {name} (Roll: {roll})")
    print(f"Total: {total_marks:.1f}, Average: {average_marks:.1f}")
    print(f"Grade: {grade}")
  
    failed_subjects = []
    for index, mark in enumerate(marks, start=1):
        if mark < 40:
            failed_subjects.append(f"Subject {index}")
            
    if failed_subjects:
        print(f"Subjects below 40: {', '.join(failed_subjects)}")
    else:
        print("Subjects below 40: None")
      
# Demonstration (Sample Input from Assignment)
if __name__ == "__main__":
    student_name = "Aarav"
    roll_number = 101
    student_marks = [88.5, 35.0, 76.0, 92.5, 48.0]
    analyze_result(student_name, roll_number, student_marks)
