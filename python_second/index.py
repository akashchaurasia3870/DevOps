#Grade Checker
print("Enter The Score \n")
score = int(input())

if score>90:
    print("Grade A")
elif score>=80 and score<=89:
    print("Grade B")
elif score>=70 and score<=79:
    print("Grade C")
elif score>=60 and score<=69:
    print("Grade D")
else:
    print("Grade F")


#Student Grade 

students = {}

while True:
    print("\n\n*******************************")
    print("Student Operations:")
    print("Type 1 For Add student")
    print("Type 2 For Update grade")
    print("Type 3 For Show all students")
    print("Type 4 For Exit")
    print("*******************************")

    menu_option = input("Enter : ")

    if menu_option == "1":
        name = input("Student name: ")
        grade = input("Grade: ")
        if name in students:
            print(name, "already exists!")
        else:
            students[name] = grade
            print("Added", name)

    elif menu_option == "2":
        name = input("Student name to update: ")
        if name in students:
            new_grade = input("New grade: ")
            students[name] = new_grade
            print("Updated", name)
        else:
            print("Student not found")

    elif menu_option == "3":
        if len(students) == 0:
            print("No students yet")
        else:
            print("\nStudent Grades:")
            for n, g in students.items():
                print(n, ":", g)

    elif menu_option == "4":
        print("bye!")
        break

    else:
        print("invalid choice, try again")

#Write To A File

myfile = open('myfile.txt','w')
myfile.write("Python Is A Dynamically Typed Language")
myfile.write("\nPython Is A Easy To Learn")
myfile.close()

#Reading A file 

myfile = open("myfile.txt", "r")
content = myfile.read()
print("File Content: ")
print(content)
myfile.close()
