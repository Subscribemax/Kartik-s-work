# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D9vG_D8-75VwLsFERU-GC4oEgqUkHV-u
"""

# Smart Student Grading & Report Card Generator
# Built by Kartik (The Honored One)

def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'D'

def get_status(avg):
    return "PASS" if avg >= 35 else "FAIL"

# Initialize class analytics
class_averages = []
grade_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
pass_count = 0
fail_count = 0
students = []

# === INPUTS ===
num_students = int(input("Enter total number of students: "))
num_subjects = int(input("Enter number of subjects (same for all students): "))

# === PROCESS EACH STUDENT ===
for i in range(num_students):
    print(f"\n--- Entering data for Student {i+1} ---")
    name = input("Student Name: ")

    marks = []
    total = 0

    for j in range(num_subjects):
        mark = float(input(f"Enter marks for Subject {j+1}: "))
        marks.append(mark)
        total += mark

    average = total / num_subjects
    grade = calculate_grade(average)
    status = get_status(average)

    # Update analytics
    class_averages.append(average)
    grade_counts[grade] += 1
    if status == "PASS":
        pass_count += 1
    else:
        fail_count += 1

    # Store student data
    students.append({
        'name': name,
        'marks': marks,
        'total': total,
        'average': average,
        'grade': grade,
        'status': status
    })

    # Optional: print report card
    generate = input("Generate report card for this student? (y/n): ").lower()
    if generate == 'y':
        print("\n========== REPORT CARD ==========")
        print(f"Name: {name}")
        print(f"Number of Subjects: {num_subjects}")
        for k, m in enumerate(marks):
            print(f"Subject {k+1}: {m}")
        print(f"Total Marks: {total}")
        print(f"Average Marks: {average:.2f}")
        print(f"Grade: {grade}")
        print(f"Status: {status}")
        print("==================================")

# === FINAL CLASS STATISTICS ===
print("\n\n========== CLASS STATISTICS ==========")
print(f"Total Students: {num_students}")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Class Average: {sum(class_averages)/len(class_averages):.2f}")
print(f"Highest Average: {max(class_averages):.2f}")
print(f"Lowest Average: {min(class_averages):.2f}")
print("Grade Distribution:")
for g in ['A', 'B', 'C', 'D']:
    print(f"  {g}: {grade_counts[g]}")
print("======================================")