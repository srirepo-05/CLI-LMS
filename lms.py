import mysql.connector
import sys
import datetime

connection =mysql.connector.connect(host="127.0.0.1",user="root",passwd="Chatgpt@1#",database="lms")

if connection.is_connected():
       print("Connection Successfull\n")
else:
       print("Connection is not successful.")
       sys.exit()

cursor = connection.cursor()
cursor = connection.cursor()

def course_details_add():
       course_name=input("Enter course name : ")
       course_id= input("Enter the course ID : ")
       year = int(input("Enter the course year : "))
       specialization = input("Enter the course specialization : ")
       query = "INSERT INTO course_details VALUES (%s, %s, %s,%s)"
       cursor.execute(query, (course_name, course_id, year, specialization))
       connection.commit()
       print("Course added sucessfully.")

def update_course_details():
    course_id = input("Enter the course ID to update: ")
    query = "SELECT * FROM course_details WHERE course_id = %s"
    cursor.execute(query, (course_id,))
    course = cursor.fetchone()
    if not course:
        print("Course not found.")
        return
    new_course_name = input("Enter the new course name (or press Enter to leave it unchanged): ")
    new_year = input("Enter the new course year (or press Enter to leave it unchanged): ")
    new_specialization = input("Enter the new course specialization : ")
    new_year = int(new_year) if new_year else course[2]
    new_course_name = new_course_name if new_course_name else course[1]
    new_specialization = new_specialization if new_specialization else course[3]
    update_query = "UPDATE course_details SET course_name = %s, course_year = %s, specialization = %s WHERE course_id = %s"
    cursor.execute(update_query, (new_course_name, new_year,new_specialization, course_id))
    connection.commit()
    print("Course details updated successfully.")

def delete_course():
    course_id = input("Enter the course ID to delete: ")
    query = "SELECT * FROM course_details WHERE course_id = %s"
    cursor.execute(query, (course_id,))
    course = cursor.fetchone()
    if not course:
        print("Course not found.")
        return
    delete_query = "DELETE FROM course_details WHERE course_id = %s"
    cursor.execute(delete_query, (course_id,))
    connection.commit()
    print("Course deleted successfully.")

def student_details_add():
       reg_no = int(input("Assign a register number : "))
       name = input("Enter the name of student : ")
       dob = input("Enter the date of birth of student : ")
       sepcialization = input("Enter the specialization : ")
       mobile_no = int(input("Enter the mobile number : "))
       year = int(input("Enter the year : "))
       query="INSERT INTO student_details VALUES (%s,%s,%s,%s,%s,%s)"
       cursor.execute(query,(reg_no,name,dob,sepcialization,mobile_no,year))
       create_student_login(reg_no)
       print("Student added Successfully.")

def update_student_details():
    reg_no = int(input("Enter the register number of the student to update: "))
    query = "SELECT * FROM student_details WHERE reg_no = %s"
    cursor.execute(query, (reg_no,))
    student = cursor.fetchone()
    if not student:
        print("Student not found.")
        return
    new_name = input("Enter the new name (or press Enter to leave it unchanged): ")
    new_dob = input("Enter the new date of birth (or press Enter to leave it unchanged): ")
    new_specialization = input("Enter the new specialization (or press Enter to leave it unchanged): ")
    new_mobile_no = input("Enter the new mobile number (or press Enter to leave it unchanged): ")
    new_year_input = input("Enter the new year (or press Enter to leave it unchanged): ")
    student_name = new_name if new_name else student[1]
    dob = new_dob if new_dob else student[2]
    specialization = new_specialization if new_specialization else student[3]
    mobile_no = new_mobile_no if new_mobile_no else student[4]
    year = int(new_year_input) if new_year_input else student[5]
    update_query = "UPDATE student_details SET name = %s, dob = %s, specialization = %s, mobile_no = %s, year = %s WHERE reg_no = %s"
    cursor.execute(update_query, (student_name, dob, specialization, mobile_no, year, reg_no))
    connection.commit()
    print("Student details updated successfully.")

def delete_student():
    reg_no = int(input("Enter the registration number of the student to delete: "))
    query = "SELECT * FROM student_details WHERE reg_no = %s"
    cursor.execute(query, (reg_no,))
    student = cursor.fetchone()
    if not student:
        print("Student not found.")
        return
    delete_query = "DELETE FROM student_details WHERE reg_no = %s"
    cursor.execute(delete_query, (reg_no,))
    delete_student_login(reg_no)
    print("Student deleted successfully.")

def delete_student_login(username):
    query = "DELETE FROM student_login_details WHERE username = %s"
    cursor.execute(query, (username,))
    connection.commit()

def administrator_details_add():
       username=input("Create a Username : ")
       password= input("Create a password : ")
       query="INSERT INTO administrator VALUES (%s,%s)"
       cursor.execute(query,(username,password))
       connection.commit()
       print("Admin added successfully.")

def delete_administrator():
    username = input("Enter the username of the administrator to delete: ")
    query = "SELECT * FROM administrator WHERE username = %s"
    cursor.execute(query, (username,))
    admin = cursor.fetchone()
    if not admin:
        print("Administrator not found.")
        return
    delete_query = "DELETE FROM administrator WHERE username = %s"
    cursor.execute(delete_query, (username,))
    connection.commit()
    print("Administrator deleted successfully.")

def change_admin_password():
    username = input("Enter the username: ")
    query = "SELECT * FROM administrator WHERE username = %s"
    cursor.execute(query, (username,))
    admin = cursor.fetchone()
    if not admin:
        print("Administrator not found.")
        return
    new_password = input("Enter the new password: ")
    update_query = "UPDATE administrator SET password = %s WHERE username = %s"
    cursor.execute(update_query, (new_password, username))
    connection.commit()
    print("Password updated successfully.")

def super_admin_login():
    username = input("Enter your super admin username : ")
    password = input("Enter your super admin password : ")
    query = "SELECT username FROM super_admin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        print("\nSuper Admin Login successful. Welcome, super admin!\n")
        print("""1- Create admin
2- Delete admin
3- Change admin password
4- Logout\n""")
        while True:
            choice = int(input("Enter your choice : "))
            print("\n")
            if choice == 1:
                administrator_details_add()
            elif choice == 2:
                delete_administrator()
            elif choice == 3:
                change_admin_password()
            elif choice == 4:
                sys.exit("Logged out")
            else:
                print("Invalid choice.")
            print("\n")
    else:
        print("Login failed. Please check your username and password.")

def admin_login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    query = "SELECT username FROM administrator WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        print("\nLogin successful. Welcome, admin!\n")
        print("""1- Add courses
2- Delete courses
3- Update course details
4- Add student
5- Delete student
6- Update student Details
7- Add staff
8- Delete staff
9- Update Staff Details
10- Logout
              """)
        while True:
            choice = int(input("Enter your choice : "))
            print("\n")
            if choice == 1:
                course_details_add()
            elif choice == 2:
                delete_course()
            elif choice == 3:
                update_course_details()
            elif choice ==4:
                student_details_add()
            elif choice == 5:
                delete_student()
            elif choice == 6:
                update_student_details()
            elif choice == 7:
                staff_details_add()
            elif choice == 8:
                delete_staff()
            elif choice == 9:
                update_staff_details()
            elif choice == 10:
                sys.exit("Logged out")
            else:
                print("Invalid choice.")
            print("\n")
    else:
        print("Login failed. Please check your username and password.")

def announcement_details_add():
       announcement=input("Enter the announcement to be made : ")
       year=int(input("Enter the year : "))
       date=datetime.date.today()
       query="INSERT INTO announcements VALUES(%s,%s,%s)"
       cursor.execute(query,(announcement,year,date))
       connection.commit()
       print("Announcement added successfully.")

def delete_announcements_by_year():
    year = int(input("Enter the year to delete announcements for: "))
    query = "SELECT * FROM announcements WHERE year = %s"
    cursor.execute(query, (year,))
    announcements = cursor.fetchall()
    if not announcements:
        print("No announcements found for the specified year.")
        return
    delete_query = "DELETE FROM announcements WHERE year = %s"
    cursor.execute(delete_query, (year,))
    connection.commit()
    print("Announcement deleted successfully")

def staff_details_add():
       reg_no=int(input("Create a registraion no : "))
       name=input("Enter the name : ")
       dob=input("Enter the date of birth : ")
       dept_name=input("Enter the department : ")
       mobile_no=int(input("Enter the mobile no : "))
       query="INSERT INTO staff_details VALUES(%s,%s,%s,%s,%s)"
       cursor.execute(query,(reg_no,name,dob,dept_name,mobile_no))
       create_staff_login(reg_no)
       print("Staff added Successfully.")

def update_staff_details():
    reg_no = int(input("Enter the registration number of the staff to update: "))
    query = "SELECT * FROM staff_details WHERE reg_no = %s"
    cursor.execute(query, (reg_no,))
    staff = cursor.fetchone()
    if not staff:
        print("Staff not found.")
        return
    new_name = input("Enter the new name (or press Enter to leave it unchanged): ")
    new_dob = input("Enter the new date of birth (or press Enter to leave it unchanged): ")
    new_dept_name = input("Enter the new department (or press Enter to leave it unchanged): ")
    new_mobile_no_input = input("Enter the new mobile number (or press Enter to leave it unchanged): ")
    name = new_name if new_name else staff[1]
    dob = new_dob if new_dob else staff[2]
    dept_name = new_dept_name if new_dept_name else staff[3]
    mobile_no = int(new_mobile_no_input) if new_mobile_no_input else staff[4]
    update_query = "UPDATE staff_details SET name = %s, dob = %s, dept_name = %s, mobile_no = %s WHERE reg_no = %s"
    cursor.execute(update_query, (name, dob, dept_name, mobile_no, reg_no))
    connection.commit()
    print("Staff details updated successfully.")

def delete_staff():
    reg_no = int(input("Enter the registration number of the staff to delete: "))
    query = "SELECT * FROM staff_details WHERE reg_no = %s"
    cursor.execute(query, (reg_no,))
    staff = cursor.fetchone()
    if not staff:
        print("Staff not found.")
        return
    delete_query = "DELETE FROM staff_details WHERE reg_no = %s"
    cursor.execute(delete_query, (reg_no,))
    delete_staff_login(reg_no)
    print("Staff deleted successfully.")

def delete_staff_login(username):
    query = "DELETE FROM staff_login_details WHERE username = %s"
    cursor.execute(query, (username,))
    connection.commit()

def create_staff_login(reg_no):
     username = int(reg_no)
     password = input("Create the password for LMS login : ")
     query="INSERT INTO staff_login_details VALUES(%s,%s)"
     cursor.execute(query,(username,password))
     connection.commit()

def staff_login():
    username = int(input("Enter your username: "))
    password = input("Enter your password: ")
    query = "SELECT username FROM staff_login_details WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        print("\nLogin successful. Welcome, staff!\n")
        print("""1- Dashboard
2- Mark attendance
3- Make announcement
4- Delete announcement
5- Logout\n""")
        while True:
            choice = int(input("Enter your choice : "))
            print("\n")
            if choice == 1:
                staff_dashboard(username)
            elif choice == 2:
                mark_attendance()
            elif choice == 3:
                announcement_details_add()
            elif choice ==4:
                delete_announcements_by_year()
            elif choice == 5:
                sys.exit("Logged out")
            else:
                print("Invalid choice.")
            print("\n")
    else:
        print("Login failed. Please check your username and password.")

def staff_dashboard(username):
    reg_no = username
    query = "SELECT * FROM staff_details WHERE reg_no = %s"
    cursor.execute(query, (reg_no,))
    staff = cursor.fetchone()
    print("\nStaff Dashboard:\n")
    print("Registration Number:", int(staff[0]))
    print("Name:", staff[1])
    print("Date of Birth:", staff[2])
    print("Department Name:", staff[3])
    print("Mobile Number:", int(staff[4]))


def mark_attendance():
    reg_no = int(input("Enter the registration number of student : "))
    course_id = input("Enter the course ID: ")
    date = datetime.date.today()
    time = datetime.datetime.now().strftime('%H:%M:%S')
    marked = input("Whether the student is present or not (yes or no): ")
    check_query = "SELECT reg_no FROM student_details WHERE reg_no = %s"
    cursor.execute(check_query, (reg_no,))
    result = cursor.fetchone()
    if result is None:
        print("Student not found.")
    else:
        query = "INSERT INTO attendance VALUES(%s, %s, %s, %s, %s)"
        cursor.execute(query, (reg_no,course_id,date,time,marked))
        connection.commit()
        print("Attendance marked successfully.")


def create_student_login(reg_no):
     username = reg_no
     password = input("Create the password for LMS login : ")
     query="INSERT INTO student_login_details VALUES(%s,%s)"
     cursor.execute(query,(username,password))
     connection.commit()

def student_login():
    username = int(input("Enter your username: "))
    password = input("Enter your password: ")
    query = "SELECT username FROM student_login_details WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        print("\nLogin successful. Welcome, student!")
        student_dashboard(username)
    else:
        print("Login failed. Please check your username and password.")

def student_dashboard(username):
    reg_no = username
    print("\n")
    query = "SELECT * FROM student_details WHERE reg_no = %s"
    cursor.execute(query, (reg_no,))
    student = cursor.fetchone()
    if not student:
        print("Student not found.")
        return
    print("Student Details:\n")
    print("Registration Number:", int(student[0]))
    print("Name:", student[1])
    print("Date of Birth:", student[2])
    print("Specialization:", student[3])
    print("Mobile Number:", int(student[4]))
    print("Year:", student[5])
    query = "SELECT C.course_id, C.course_name FROM course_details C " \
            "INNER JOIN student_details S ON C.course_year = S.year " \
            "WHERE S.reg_no = %s AND C.specialization = %s"
    cursor.execute(query, (reg_no,student[3]))
    registered_courses = cursor.fetchall()
    if not registered_courses:
        print("You have not registered for any courses.")
    else:
        print("\nYour Registered Courses:\n")
        for course_id, course_name in registered_courses:
            print(f"Course ID: {course_id}, Course Name: {course_name}")
    print("\n")
    calculate_attendance_percentage(reg_no)
    print("\n")
    display_announcements_by_year(student[5])

def calculate_attendance_percentage(reg_no):
    query = "SELECT C.course_id, C.course_name, COUNT(A.reg_no) AS total_attendance " \
            "FROM course_details C " \
            "LEFT JOIN attendance A ON C.course_id = A.course_id " \
            "WHERE A.reg_no = %s AND A.marked='yes'" \
            "GROUP BY C.course_id, C.course_name"
    cursor.execute(query, (reg_no,))
    course_attendance = cursor.fetchall()
    if not course_attendance:
        print("No attendance records found for your registered courses.")
    else:
        print("\nAttendance Percentage for Registered Courses:\n")
        for course_id, course_name, total_attendance in course_attendance:
            query = "SELECT COUNT(*) FROM attendance A " \
                    "WHERE A.reg_no = %s AND A.course_id = %s"
            cursor.execute(query, (reg_no, course_id))
            total_classes = cursor.fetchone()[0]

            if total_classes > 0:
                attendance_percentage = (total_attendance / total_classes) * 100
            else:
                attendance_percentage = 0
            print(f"Course ID: {course_id}, Course Name: {course_name}")
            print(f"Total Attendance: {total_attendance}")
            print(f"Total Classes: {total_classes}")
            print(f"Attendance Percentage: {attendance_percentage:.2f}%")

def display_announcements_by_year(year):
    query = "SELECT announcement, date FROM announcements WHERE year = %s"
    cursor.execute(query, (year,))
    announcements = cursor.fetchall()
    if not announcements:
        print("No announcements found.")
    else:
        print(f"Announcements : \n")
        for announcement, date in announcements:
            print(f"Date: {date}",end=" ")
            print(f"Announcement: {announcement}\n")
            print("\n")
print("+-------------------------------------------------------------------------------------------------------+")
print("|                                    Learning Management System                                         |")
print("+-------------------------------------------------------------------------------------------------------+\n")
print("""1- SUPER ADMIN LOGIN
2- ADMIN LOGIN
3- STAFF LOGIN
4- STUDENT LOGIN\n""")
choice = int(input("Enter your choice : "))
print("\n")
if choice == 1:
    super_admin_login()
elif choice == 2:
    admin_login()
elif choice == 3:
    staff_login()
elif choice == 4:
    student_login()
cursor.close()
connection.close()