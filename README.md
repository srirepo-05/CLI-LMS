# Learning Management System (LMS)

## Overview

This Learning Management System (LMS) is designed to facilitate the management of students, staff, and courses within an educational institution. It allows for the management of student and staff records, course details, attendance tracking, and announcements. This system supports multiple user roles, including super administrators, administrators, staff, and students.

## Features

- **Database Structure:**
  - **Student Details:** Records for students including registration number, name, date of birth, specialization, mobile number, and year.
  - **Administrator Details:** Credentials for administrators.
  - **Staff Details:** Records for staff including registration number, name, date of birth, department name, and mobile number.
  - **Course Details:** Information about courses including course name, ID, year, and specialization.
  - **Announcements:** For making and managing announcements.
  - **Attendance Tracking:** Mark and manage student attendance.
  - **Login Details:** Separate login details for students, staff, and administrators.

- **User Roles:**
  - **Super Admin:** Can manage admins, update passwords, and oversee the entire system.
  - **Admin:** Can add, update, or delete courses, students, staff, and manage announcements.
  - **Staff:** Can mark attendance, make and delete announcements, and view their dashboard.
  - **Student:** Can view their personal details, registered courses, attendance records, and announcements.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sponge-24/CLI-LMS
   ```
2. **Navigate to the project directory:**
   ```bash
   cd CLI-LMS
   ```
3. **Ensure you have MySQL installed and running.**

4. **Create the database and tables:**
   - Run the provided SQL script to set up the database schema.

5. **Install required Python packages:**
   ```bash
   pip install mysql-connector-python
   ```

6. **Configure Database Connection:**
   - Update the database connection parameters in the `Python` script with your MySQL credentials.

## Usage

1. **Run the LMS application:**
   ```bash
   python lms.py
   ```
2. **Follow the prompts to log in as a super admin, admin, staff, or student.**

## Functions

- **Super Admin:**
  - Manage administrator accounts (create, delete, update passwords).
- **Admin:**
  - Manage courses, students, staff, and announcements.
- **Staff:**
  - Mark student attendance, make announcements, and manage their own details.
- **Student:**
  - View personal details, registered courses, attendance records, and announcements.

## Code Structure

- **Database Initialization:** `lms.sql` - Contains SQL statements for database setup.
- **Main Application Logic:** `lms.py` - Python script for running the LMS with CRUD operations and login functionality.
