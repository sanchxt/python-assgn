class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks


def create_csv(file_path):
    students = [
        Student(1, 'Sanchit', 92.7),
        Student(2, 'Sanchita', 95.3),
        Student(3, 'Sanidhya', 91.6),
        Student(4, 'Elisha', 90.5),
        Student(5, 'Khushi', 65.8)
    ]

    with open(file_path, 'w') as file:
        for stud in students:
            file.write(f'{stud.roll},{stud.name},{stud.marks}\n')


def display_record(file_path, r):
    with open(file_path, 'r') as file:
        for line in file:
            roll, name, marks = line.strip().split(',')
            if int(roll) == r:
                print(f'Roll No.: {roll}, name: {name}, marks: {marks}\n')
                return
    print(f'record not found\n')


def update_record(file_path, r, new_marks):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        roll, name, marks = line.strip().split(',')
        if int(roll) == r:
            lines[i] = f'{roll},{name},{new_marks}\n'
            with open(file_path, 'w') as new_file:
                new_file.writelines(lines)
            print('Record updated\n')
            return
    print('record not found\n')


def delete_record(file_path, r):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = [line for line in lines if int(
        line.strip().split(',')[0]) != r]

    with open(file_path, 'w') as new_file:
        new_file.writelines(lines)
    print('record deleted\n')


def add_record(file_path, r, n, m):
    with open(file_path, 'a') as file:
        file.write(f'{r},{n},{m}\n')
    print('record added\n')


def search_record(file_path, r):
    with open(file_path, 'r') as file:
        for line in file:
            roll, name, marks = line.strip().split(',')
            if int(roll) == r:
                print(f'record found\nRoll No.: {
                    roll}, Name: {name}, Mark: {marks}\n')
                return
    print('record not found\n')


if __name__ == "__main__":
    csv_file = 'assignments/ques14/student_data.csv'
    create_csv(csv_file)

    roll_inp = int(input("Roll number: "))

    marks_inp = float(input("New marks: "))
    update_record(csv_file, roll_inp, marks_inp)

    new_roll = int(input("Roll number: "))
    new_name = input("Name: ")
    new_marks = float(input("Marks: "))
    add_record(csv_file, new_roll, new_name, new_marks)

    search_roll = int(input("Roll number to search: "))
    search_record(csv_file, search_roll)
