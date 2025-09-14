dictionary = {'Ram': 45, 'Raghu': 23, 'Rajan': 60, 'Zia': 77, 'Mushfiqur': 23, 'Nancy': 89}

try:
    student_name = input("Enter the student's name: ")
    print("{}'s marks: {}".format(student_name, str(dictionary[student_name])))
except Exception:
    print("Student not found")