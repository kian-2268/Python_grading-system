class student:
    def __init__(self,year, name):
        self.name = name
        self.year = year
        self.grade = []

    def addGrade(self, grade):
        if grade < 1 or grade > 4:
            raise ValueError("Grade must be within 1 and 4.")
        self.grade.append(grade)

    def calculate_grade(self):
        if not self.grade:
            raise ZeroDivisionError("No Available grades that can be calculated.")
        return sum (self.grade)/ len(self.grade)

def main():
    try:
        name = input("Enter student name: ")
        year = input("Enter student year level: ")

        students = student(year, name)

        while True:
            try:
                grade = float(input("Enter your grades: "))
                if grade == 3:
                    break
                students.addGrade(grade)
            except ValueError as e:
                print("Invalid output", e)

        average = students.calculate_grade()
        print(f"\nStudent Name: {students.name}")
        print(f"Student Year: {students.year}")
        print(f"Average Grade: {average:.2f}")

    except ZeroDivisionError as e:
        print("Error: ", e)
    except Exception as e:
        print("Unexpected error: ", e)

if __name__ == "__main__":
    main()
