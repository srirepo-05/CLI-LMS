-- Active: 1692888112245@@localhost@3306@lms
CREATE DATABASE lms;
USE lms;
CREATE Table student_details(reg_no DOUBLE PRIMARY KEY, name VARCHAR(30), dob DATE, specialization VARCHAR(10), mobile_no DOUBLE, year INT);
CREATE Table administrator(username VARCHAR(20) PRIMARY KEY,password VARCHAR(20));
CREATE Table staff_details(reg_no DOUBLE PRIMARY KEY, name VARCHAR(30),dob DATE, dept_name VARCHAR(20), mobile_no DOUBLE);
CREATE Table course_details(course_name VARCHAR(50), course_id VARCHAR(10) PRIMARY KEY, course_year INT, specialization VARCHAR(20));
CREATE Table announcements(announcement VARCHAR(250), year INT, date DATE);
CREATE TABLE attendance(reg_no DOUBLE, course_id VARCHAR(10), date DATE, time VARCHAR(10), marked VARCHAR(10) );
CREATE Table student_login_details(username DOUBLE PRIMARY KEY, password VARCHAR(20));
CREATE Table staff_login_details(username DOUBLE PRIMARY KEY, password VARCHAR(20));
CREATE Table super_admin(username VARCHAR(20) PRIMARY KEY, password VARCHAR(20));
