# School Management System

## Description

This is a **School Management System** built using Python's `tkinter` library for the graphical user interface (GUI) and `pymysql` for database connectivity. The application allows users to manage student and professor data, including adding, updating, deleting, and searching records. The system dynamically updates the interface based on the user's role (Student or Professor) and stores data in a MySQL database.

---

## Features

1. **Dynamic Interface**:
   - The interface changes based on the selected status (Student or Professor).
   - For Students: Fields for "Filiere" and "Semestre" are displayed.
   - For Professors: Fields for "Departement" and "Element" are displayed.

2. **Database Integration**:
   - Connects to a MySQL database to store and retrieve data.
   - Two separate tables are used: `student_data` and `professor_data`.

3. **CRUD Operations**:
   - **Add**: Add new student or professor records.
   - **Update**: Modify existing records.
   - **Delete**: Remove records from the database.
   - **Clear**: Clear all input fields.

4. **Search Functionality**:
   - Search for students or professors by specific fields (e.g., CIN, Name, Email, etc.).
   - Display all records with the "Show All" button.

5. **Data Display**:
   - Data is displayed in a tabular format using `ttk.Treeview`.
   - Scrollbars are provided for easy navigation.

6. **Error Handling**:
   - Displays error messages for invalid or missing inputs.

---

## Requirements

- Python 3.x
- Libraries:
  - `tkinter` (included with Python)
  - `pymysql` (install via `pip install pymysql`)
- MySQL Database:
  - Two databases: `sms1` for students and `sms2` for professors.
  - Tables: `student_data` and `professor_data` with the following columns:
    - `CIN`, `Name`, `Email`, `Contact`, `Birthday`, `Address`, `Status`, `Filiere/Semestre` (for students), `Departement/Element` (for professors).

---

## How to Run

1. **Set Up MySQL Database**:
   - Create two databases: `sms1` and `sms2`.
   - Create tables `student_data` and `professor_data` with the required columns.

2. **Install Dependencies**:
   ```bash
   pip install pymysql
   ```

3. **Run the Application**:
   ```bash
   python school_management_system.py
   ```

4. **Use the Application**:
   - Fill in the fields in the "Enter Data" section.
   - Select "Student" or "Professor" to dynamically update the interface.
   - Use the buttons to add, update, delete, or search records.
   - View the data in the respective tables.

---

## Code Structure

- **Main Window**:
  - Contains frames for data entry, student data display, and professor data display.
  - Dynamically updates based on the selected status.

- **Functions**:
  - `update_status`: Updates the interface based on the selected status.
  - `fetch_student_data` / `fetch_professor_data`: Fetches data from the database and displays it in the table.
  - `add_func`: Adds new records to the database.
  - `update_func`: Updates existing records.
  - `delete_func`: Deletes records from the database.
  - `search_func_student` / `search_func_professor`: Searches for records based on the selected field.
  - `clear_funct`: Clears all input fields.

- **Database Connection**:
  - Uses `pymysql` to connect to the MySQL database.
  - Executes SQL queries to perform CRUD operations.

---


## Notes

- Ensure the MySQL server is running and the database credentials are correctly configured in the code.
- The application is designed for educational purposes and can be extended with additional features.

---

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.

---
