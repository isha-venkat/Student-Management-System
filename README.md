# Student Management System

This is a simple **Student Management System** built using **Python** for the front-end interface and **MySQL** for the backend. Data is stored in a **CSV file format**, which makes it lightweight and portable for smaller use cases.

## Features

- **Add New Student**: Insert details like roll number, name, age, email, and phone number.
- **View Students**: Display a list of all student records in a tabular format.
- **Search Student**: Find a specific student by their roll number.
- **Update Student**: Modify the details of an existing student (except roll number).
- **Delete Student**: Remove a student's record from the database.
- **CSV File Storage**: All student records are saved in a CSV file (`student_database.csv`) for quick access and easy updates.

## Technologies Used

- **Python**: Front-end development and logic implementation.
- **MySQL**: Backend database management (conceptual support).
- **CSV**: For lightweight data storage and manipulation.

## Setup Instructions

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Student-Management-System.git
2. Ensure you have Python 3 installed on your system. You can download it [here](https://www.python.org/).

3. Install any required Python libraries (if applicable):
   ```bash
   pip install <library-name> (os, csv)

4. Run the program by executing the script:
   ```bash
   python student_management_system.py

### How to Use
1. Launch the program by running the script.
2. A menu will be displayed with the following options:
 1. Add New Student: Enter details like roll number, name, age, email, and phone.
<br> 2. View Students: Display all stored student records in a table.
<br> 3. Search Student: Enter a roll number to find the corresponding student.
<br> 4. Update Student: Modify details of an existing student record.
<br> 5. Delete Student: Remove a student's record by entering their roll number.
<br> 6. Quit: Exit the application.
3. Follow the prompts to input or retrieve data.

### File Structure
. student_management_system.py: The main Python script containing all functionality.
<br>. student_database.csv: A CSV file that stores all student records.

### Example Workflow
1. Run the program:
   ```bash
   python student_management_system.py
2. Choose an option from the menu, for example:
. Add New Student: Enter details such as roll number, name, age, email, and phone.
. Search Student: Input the roll number to fetch details of a specific student.
. Update Student: Modify the name, age, email, or phone of an existing student.
. Delete Student: Remove a student's record permanently from the database.
3. All changes will be saved automatically in the student_database.csv file.

### Limitations
. Storage: The system uses CSV for data storage instead of a relational database. For larger-scale applications, integrate MySQL or another RDBMS for better performance.
<br>. Validation: Input validation is basic. Future improvements can include stricter checks for data formats (e.g., email, phone number).
<br>. Error Handling: The current implementation includes minimal error handling. Exception handling can be enhanced to make the system more robust.

### Future Enhancements
. Add a Graphical User Interface (GUI) for better usability.
<br>. Integrate with MySQL for scalable and secure data storage.
<br>. Implement more advanced search and filtering options.
<br>. Provide options for exporting reports in formats like PDF or Excel.
<br>. Add login and authentication for secure access.

### Author
Developed by Isha Venkateswaran as a investigatory project. Contributions, suggestions, and improvements are always welcome!
