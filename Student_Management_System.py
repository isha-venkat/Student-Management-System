# Student Management System
import csv
import os
# Define global variables
student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'student_database.csv'


def display_menu():
    print("---------------------------------------")
    print(" Student Database Management System")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields
    global student_database

    existing_roll_number=[]

    if os.path.exists(student_database):
        with open(student_database, "r", encoding="utf-8") as f:
            existing_roll_number = [line.split(',')[0] for line in f]
    else:
        print("Database does not exist. Your data will be stored in 'student_database.csv' file")
        
    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        if field=="roll":
            while value in existing_roll_number:
                print("Roll Number already exists, Please enter the correct roll number")
                value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database,"a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
        
    print("Data saved successfully")
    input("Press any key to continue - ")
    return

        
def view_students():
    global student_fields
    global student_database

    print("--- Student Records ---")

    if os.path.exists(student_database):
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for x in student_fields:
                print(x,end='\t |')
            print("\n-----------------------------------------------------------------")

            for row in reader:
                for item in row:
                    print(item, end="\t |")
                print("\n")
    else:
        print("File does not exist")
    
    input("Press any key to continue - ")
    


def search_student():
    global student_fields
    global student_database

    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")
    if os.path.exists(student_database):
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        print("----- Student Found -----")
                        print("Roll: ", row[0])
                        print("Name: ", row[1])
                        print("Age: ", row[2])
                        print("Email: ", row[3])
                        print("Phone: ", row[4])
                        break
            else:
                print("Roll No. not found in our database")
    else:
        print("File does not exist")
    input("Press any key to continue - ")
    

def update_student():
    global student_fields
    global student_database

    print("--- Update Student ---")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    if os.path.exists(student_database):
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        index_student = counter
                        print("Student Found: at index ",index_student+1)
                        student_data = []
                        fieldIndex=0
                        for field in student_fields:
                            if fieldIndex!=0:
                                value = input("Enter " + field + ": ")
                                student_data.append(value)
                            else:
                                student_data.append(row[0])
                            fieldIndex+=1
                        updated_data.append(student_data)
                    else:
                        updated_data.append(row)
                    counter += 1
        
    
        if index_student is not None:
            with open(student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("Data updated successfully")

        else:
            print("Roll No. not found in our database")
        
    else:
        print("File does not exist")

    input("Press any key to continue-")

def delete_student():
    global student_fields
    global student_database

    print("--- Delete Student ---")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    if os.path.exists(student_database):
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if roll != row[0]:
                        updated_data.append(row)
                        counter += 1
                    else:
                        student_found = True

        if student_found is True:
            with open(student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("Roll no. ", roll, "deleted successfully")
        else:
            print("Roll No. not found in our database")
    else:
        print("File does not exist")

    input("Press any key to continue - ")
    

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")

