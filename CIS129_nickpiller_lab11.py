9.1
with open("grades.txt", "w") as file:
    while True:
        grade = input("Enter a grade (or -1 to finish): ")
        if grade == "-1":
            break
        file.write(grade + "\n")

9.2
total = 0
count = 0

with open("grades.txt", "r") as file:
    for line in file:
        grade = int(line.strip())
        print("Grade:", grade)
        total += grade
        count += 1

if count > 0:
    average = total / count
    print("Total:", total)
    print("Count:", count)
    print("Average:", average)
else:
    print("No grades found.")

9.3
import csv

with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    while True:
        first = input("Enter first name (or 'done' to finish): ")
        if first.lower() == "done":
            break
        last = input("Enter last name: ")
        exam1 = input("Enter exam 1 grade: ")
        exam2 = input("Enter exam 2 grade: ")
        exam3 = input("Enter exam 3 grade: ")
        
        writer.writerow([first, last, exam1, exam2, exam3])
