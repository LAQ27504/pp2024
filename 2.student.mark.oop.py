class Date():
    def __init__(self):
        self.__day = ""
        self.__month = ""
        self.__year = ""

    def setDate(self, mystr):
        if mystr.count("/") != 2:
            return False
        else: 
            self.__day, self.__month, self.__year = mystr.split("/")
            if self.__day.isnumeric() and self.__month.isnumeric() and self.__year.isnumeric():
                self.__day = int(self.__day)
                self.__month = int(self.__month)
                self.__year = int(self.__year)
            else:
                return False
            if self.__month in [1,3,5,7,8,10,12]:
                if self.__day <= 31:
                    return True
                else:
                    return False
            elif self.__month in [4,6,9,11]:
                if self.__day <= 30:
                    return True
                else:
                    return False
            elif self.__month == 2:
                if self.__year % 4 == 0:
                    if self.__year % 100 == 0:
                        if self.__year % 400 == 0:
                            if self.__day <= 29:
                                return True
                            else: 
                                return False
                            
                        else:
                            if self.__day <= 28:
                                return True
                            else:
                                return False
                    else:
                        if self.__day <= 29:
                                return True
                        else: 
                            return False
                else:
                    if self.__day <= 28:
                        return True
                    else:
                        return False
            else:
                return False
    
    def addZero(number):
        if number < 10:
            number = "0" + str(number)
        return number


    def stringDate(self):
        return f"{Date.addZero(self.__day)}/{Date.addZero(self.__month)}/{self.__year}"


# Class Student
class Student():
    def __init__(self):
        self.__ID = ""
        self.__name = ""
        self.__dob = ""

    def setID(self, students_list):
        self.__ID = input("Enter student ID: ")
        check = False
        while check == False:
            check = True
            for i in range(len(students_list)):
                if (self.__ID == students_list[i].getID()):
                    self.__ID = input("Please re-enter student ID ( This ID has been available in the student list ): ")
                    check = False
    
    def getID(self):
        return self.__ID
    
    def setName(self):
        self.__name = input("Enter student name: ")
    
    def getName(self):
        return self.__name
    
    def setDOB(self):
        st_dob = Date()
        check = st_dob.setDate(input("Enter student DOB ( format dd/mm/yyyy ): "))
        while ( check == False):
            check = st_dob.setDate(input("Please re-enter student DOB ( Incorrect format ): "))
        self.__dob = st_dob.stringDate()
    
    def getDOB(self):
        return self.__dob

    def display_info(self):
        print(f"Student ID: {self.__ID}")
        print(f"Student name: {self.__name}")
        print(f"Student DoB: {self.__dob}")



class Students_list():
    def __init__(self):
        self.__st_list = []

    def getList(self):
        return self.__st_list

    def addStudent(self, number_of_students):
        print("+"*20)
        for i in range(number_of_students):
            print("--------------------")
            if (i == 0):
                print(f"{i + 1}st student:")
            elif (i == 1):
                print(f"{i + 1}nd student:")
            elif (i == 2):
                print(f"{i + 1}rd student:")
            else:
                print(f"{i + 1}th student:")
            temp_student = Student()
            temp_student.setID(self.__st_list)
            temp_student.setName()
            temp_student.setDOB()
            self.__st_list.append(temp_student)
    
    def displayStudentList(self):
        print("+"*20)
        if (len(self.__st_list) == 0):
            print("There are no students in the list\n")
        else:
            for i in range(len(self.__st_list)):
                print("--------------------")
                if (i == 0):
                    print(f"{i + 1}st student information:")
                elif (i == 1):
                    print(f"{i + 1}nd student information:")
                elif (i == 2):
                    print(f"{i + 1}rd student information:")
                else:
                    print(f"{i + 1}th student information:")
                self.__st_list[i].display_info()

        

class Course():
    def __init__(self):
        self.__ID = ""
        self.__Name = ""

    def setID(self, courses_list):
        self.__ID = input("Enter course ID: ")
        check = False
        while check == False:
            check = True
            for i in range(len(courses_list)):
                if (self.__ID == courses_list[i].getID()):
                    self.__ID = input("Please re-enter course ID ( This ID has been available in the student list ): ")
                    check = False

    def getID(self):
        return self.__ID
    
    def setName(self):
        self.__Name = input("Enter course name: ")

    def getName(self):
        return self.__Name

    def display_course(self):
        print(f"Course ID: {self.__ID}")
        print(f"Course Name: {self.__Name}\n")



class Courses_list():
    def __init__(self):
        self.__cour_list = []

    def addCourses(self, number_of_courses):
        print("+"*20)
        for i in range(number_of_courses):
            print("--------------------")
            if (i == 0):
                print(f"{i + 1}st course:")
            elif (i == 1):
                print(f"{i + 1}nd course:")
            elif (i == 2):
                print(f"{i + 1}rd course:")
            else:
                print(f"{i + 1}th course:")
            temp_course = Course()
            temp_course.setID(self.__cour_list)
            temp_course.setName()
            self.__cour_list.append(temp_course)

    def searchCourseById(self, id):
        check = False
        for i in range(len(self.__cour_list)):
            if (self.__cour_list[i].getID() == id):
                check = True
        return check
         
    def getList(self):
        return self.__cour_list

    def display_courses(self):
        print("+"*20)
        if (len(self.__cour_list) == 0):
            print("There are no students in the list\n")
        else:
            for i in range(len(self.__cour_list)):
                print("--------------------")
                if (i == 0):
                    print(f"{i + 1}st course information:")
                elif (i == 1):
                    print(f"{i + 1}nd course information:")
                elif (i == 2):
                    print(f"{i + 1}rd course information:")
                else:
                    print(f"{i + 1}th course information:")
                self.__cour_list[i].display_course()
                


class Students_mark():
    def __init__(self):
        self.__student_id = ""
        self.__mark = 0.0
    
    def setStudentID(self, student_id):
        self.__student_id = student_id
    
    def getStudentID(self):
        return self.__student_id

    def setMark(self):
        print(f"Student ID {self.__student_id}")
        self.__mark = input("Enter student mark: ")
        while (self.__mark.isdecimal() == False):
            self.__mark = input("Please re-enter student mark (Wrong type, not decimal): ")
        self.__mark = float(self.__mark)
    
    def getMark(self):
        return self.__mark



class Course_mark():
    def __init__(self):
        self.__course_ID = ""
        self.__student_list_mark = []
    
    def setCourseID(self, courses_list):
        print("+"*20)
        self.__course_ID = input("Enter course ID: ")
        while (courses_list.searchCourseById(self.__course_ID) == False):
            print("This course ID isn't available, please re-enter the course ID")
            self.__course_ID = input("Enter course ID: ")
    
    def getCourseID(self):
        return self.__course_ID
    
    def addStudent(self, student_list):
        for i in range(len(student_list)):
            myStudentMark = Students_mark()
            myStudentMark.setStudentID(student_list[i].getID())
            myStudentMark.setMark()
            self.__student_list_mark.append(myStudentMark)

    def getStudentListMark(self):
        return self.__student_list_mark
    
    def displayStudentList(self, students_list, courses_list):
        temp_course = ""
        for i in range(len(courses_list)):
            if (self.__course_ID == courses_list[i].getID()):
                temp_course = courses_list[i].getName()
        print(f"Course ID: {self.__course_ID}")
        print(f"Course name: {temp_course}")
        for i in range(len(self.__student_list_mark)):
            print(f"Student ID: {self.__student_list_mark[i].getStudentID()}")
            print(f"Student name: {students_list[i].getName()}")
            print(f"Mark: {self.__student_list_mark[i].getMark()}")



class Mark_list():
    def __init__(self):
        self.__mark_list = []

    def addCourseMark(self, student_list, courses_list):
        my_course = Course_mark()
        my_course.setCourseID(courses_list)
        my_course.addStudent(student_list)
        self.__mark_list.append(my_course)
    
    def display_course_mark(self, student_list,courses_list):
        print("+"*20)
        temp_course = input("Enter course ID: ")
        while (courses_list.searchCourseById(temp_course) == False):
            print("This course ID isn't available, please re-enter the course ID")
            temp_course = input("Enter course ID: ")

        for i in range(len(self.__mark_list)):
            if (temp_course == self.__mark_list[i].getCourseID()):
                self.__mark_list[i].displayStudentList(student_list, courses_list.getList())

    

class university():
    def __init__(self):
        self.__number_of_students = 0
        self.__number_of_courses = 0
        self.__students_list = Students_list()
        self.__courses_list = Courses_list()
        self.__mark_list = Mark_list()


    def input_number_of_students(self):
        self.__number_of_students = input("Enter number of students: ")
        while (self.__number_of_students.isnumeric() == False):
            self.__number_of_students = input("Please re-enter number of students (Wrong type - not numberic): ")
        self.__number_of_students = int(self.__number_of_students)
    
    def input_number_of_courses(self):
        self.__number_of_courses = input("Enter number of courses: ")
        while (self.__number_of_courses.isnumeric() == False):
            self.__number_of_courses = input("Please re-enter number of courses (Wrong type - not numberic): ")
        self.__number_of_courses = int(self.__number_of_courses)

    def input_student_information(self):
        if (self.__number_of_students == 0):
            self.input_number_of_students()
        self.__students_list.addStudent(self.__number_of_students)
        self.__number_of_students = 0

    def input_courses_information(self):
        if (self.__number_of_courses == 0):
            self.input_number_of_courses()
        self.__courses_list.addCourses(self.__number_of_courses)
        self.__number_of_courses = 0

    def input_mark(self):
        self.__mark_list.addCourseMark(self.__students_list.getList(), self.__courses_list)

    def display_list_courses(self):
        self.__courses_list.display_courses()

    def display_list_students(self):
        self.__students_list.displayStudentList()

    def display_mark(self):
        self.__mark_list.display_course_mark(self.__students_list.getList(), self.__courses_list)




def main():
    my_university = university()
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
            my_university.input_number_of_students()
        elif (choice == '2'):
            my_university.input_student_information()
        elif (choice == '3'):
            my_university.input_courses_information()
        elif (choice == '4'):
            my_university.input_courses_information()
        elif (choice == '5'):
            my_university.input_mark()
        elif (choice == '6'):
            my_university.display_list_courses()
        elif (choice == '7'):
            my_university.display_list_students()
        elif (choice == '8'):
            my_university.display_mark()
        elif (choice == '9'):
            return
        else:
            print("Not valid choice, please choose again")


if __name__ == "__main__":
    main()