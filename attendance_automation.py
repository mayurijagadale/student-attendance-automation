import csv

while True:
    try:
        minimum_attendance = int(
            input("Enter minimum attendance percentage: ")
        )

        if 0 <= minimum_attendance <= 100:
            break
        else:
            print("Please enter a percentage between 0 and 100.")

    except ValueError:
        print("Invalid input. Please enter a number.")


good_count = 0
low_count = 0
total_students = 0

with open("student.csv", "r") as file:
    reader = csv.DictReader(file)

    with open("attendance_report.csv", "w", newline="") as report:
        writer = csv.writer(report)

        writer.writerow(["Name", "Attendance", "Status"])

        for student in reader:
            name = student["Name"]

            try:
                attendance = int(student["Attendance"])
            except ValueError:
                print("Invalid attendance for", name)
                continue

            total_students += 1

            if attendance < minimum_attendance:
                status = "LOW ATTENDANCE"
                low_count += 1
            else:
                status = "GOOD ATTENDANCE"
                good_count += 1

            print(name, "-", attendance, "% -", status)
            writer.writerow([name, attendance, status])


print("\n--- Attendance Summary ---")
print("Total Students:", total_students)
print("Good Attendance:", good_count)
print("Low Attendance:", low_count)