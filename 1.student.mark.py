#function input number of student
def input_number_of_student(number_of_student):
    while number_of_student <= 0:
        print("Please enter number of student:")
        number_of_student = int(input())
    return number_of_student

#function input student information
def input_student_information(student_list, number_of_student):
    number_of_student = input_number_of_student(number_of_student)
    for i in range(number_of_student):
        if (i == 0):
            print(f"{i + 1}st student:")
        elif (i == 1):
            print(f"{i + 1}nd student:")
        elif (i == 2):
            print(f"{i + 1}rd student:")
        else:
            print(f"{i + 1}th student:")
        print("Enter the student ID:")
        student_id = input()
        while (len(student_list) != 0 ):
            check = True
            for i in student_list:
                if (student_id == i["ID"]):
                    check = False
            if check == True:
                break
            print("Pleas re-enter the student ID: ( This ID has available in the student list )")
            student_id = input()
        print("Enter the student name:")
        student_name = input()
        print("Enter the student Date of Birth:")
        student_DoB = input()
        student_info = {"ID" : student_id, "Name" : student_name, "DoB" : student_DoB}
        student_list.append(student_info)
        print()

#function input number of course
def input_number_of_courses(number_of_courses):
    while number_of_courses <= 0:
        print("Enter number of course:")
        number_of_courses = int(input())
    return number_of_courses

#function input the courses information        
def input_courses_information(course_dict, number_of_courses):
    number_of_courses = input_number_of_courses(number_of_courses)
    for i in range(number_of_courses):
        if (i == 0):
            print(f"{i + 1}st course:")
        elif (i == 1):
            print(f"{i + 1}nd course:")
        elif (i == 2):
            print(f"{i + 1}rd course:")
        else:
            print(f"{i + 1}th course:")
        print("Enter course ID:")
        course_id = input()
        while (course_id in course_dict):
            print("Pleas re-enter the course ID: ( This ID has available in the course list )\n")
            course_id = input()
        print("Enter the course name:")
        course_name = input()
        course_dict[course_id] = course_name
        print()

#function input mark for the choosen courses
def input_mark(mark_dict, course_dict, student_list):
    if (len(course_dict) == 0):
        print("There are no courses available\n")
    else:
        print("Enter course id:")
        course_id = input()
        while course_id not in course_dict.keys():
            print("Please re-enter the course ID, there are no courses ID matched:\n")
            course_id = input()
        course_mark = {}
        for i in student_list:
            student_name = i["Name"]
            student_id = i["ID"]
            print(f"Enter mark of student {student_name} ID {student_id}:")
            student_mark = float(input())
            course_mark[student_id] = student_mark
            mark_dict[course_id] = course_mark
                
#function display courses list                
def list_courses(course_dict):
    if (len(course_dict) == 0):
        print("There are no courses available\n")
    else:
        for count, course_id in enumerate(list(course_dict.keys())):
            course_name = course_dict[course_id]
            print(f"Course number {count + 1}:")
            print(f"Course ID: {course_id}")
            print(f"Course Name: {course_name}\n")

#function display students list
def list_student(student_list):
    if (len(student_list) == 0):
        print("There are no students in the list\n")
    else:
        for count, student_info in enumerate(student_list):
            student_id = student_info["ID"]
            student_name = student_info["Name"]
            student_DoB = student_info["DoB"]
            print(f"Student number {count + 1}")
            print(f"Student ID: {student_id}")
            print(f"Student name: {student_name}")
            print(f"Student DoB: {student_DoB}\n")
            

#function display mark of a choosen course
def display_mark(mark_dict, student_list, course_dict):
    if (len(student_list) == 0):
        print("There are no students in the list\n")
    elif (len(mark_dict) == 0):
        print("There are no marks for the student\n")
    else:
        print("Enter the course ID:")
        course_id = input()
        while course_id not in course_dict.keys():
            print("Please re-enter the course ID, there are no courses ID matched:")
            course_id = input()
        course_name = course_dict[course_id]
        print(f"Mark of students in the course {course_id}, Name {course_name}")
        temp_list = mark_dict[course_id]
        for count, student_id in enumerate(list(temp_list.keys())):
            student_mark = temp_list[student_id]
            student_name = student_list[count]["Name"]
            print(f"Student number {count + 1}")
            print(f"ID: {student_id}")
            print(f"Name: {student_name}")
            print(f"Mark: {student_mark}\n")

#main function
def main():
    #Declare all required data
    number_of_students = 0
    number_of_courses = 0
    student_list = []
    course_dict = {}
    mark_dict = {}

    choice = 0

    while (True):
        print("-------------------------------")
        print("Choosing an action:")
        print("1. Input number of students")
        print("2. Input students information")
        print("3. Input number of courses")
        print("4. Input courses information")
        print("5. Input mark for a course")
        print("6. Display courses list")
        print("7. Display student list")
        print("8. Display a course mark")
        print("9. Exit program")
        choice = input()
        if (choice == '1'):
            number_of_students = input_number_of_student(number_of_students)
        elif (choice == '2'):
            input_student_information(student_list, number_of_students)
            number_of_students = 0
        elif (choice == '3'):
            number_of_courses = input_courses_information(number_of_courses)
        elif (choice == '4'):
            input_courses_information(course_dict, number_of_courses)
            number_of_courses = 0
        elif (choice == '5'):
            input_mark(mark_dict, course_dict, student_list)
        elif (choice == '6'):
            list_courses(course_dict)
        elif (choice == '7'):
            list_student(student_list)
        elif (choice == '8'):
            display_mark(mark_dict, student_list, course_dict)
        elif (choice == '9'):
            return
        else:
            print("Not valid choice, please choose again")


#Running main
if __name__ == "__main__":
    main()