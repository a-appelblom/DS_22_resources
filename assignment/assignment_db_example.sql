CREATE Table
    programme (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL
    );

-- Create a table for the courses

-- Path: assignment.sql

CREATE Table
    course (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        programme_id INTEGER NOT NULL,
        FOREIGN KEY (programme_id) REFERENCES programme (id)
    );

-- Create a table for the students

-- Path: assignment.sql

CREATE Table
    student (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        programme_id INTEGER NOT NULL,
        FOREIGN KEY (programme_id) REFERENCES programme (id)
    );

-- Create a table for the students enrolled in a course

-- Path: assignment.sql

CREATE Table
    student_course (
        id INTEGER PRIMARY KEY,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES student (id),
        FOREIGN KEY (course_id) REFERENCES course (id)
    );

-- Create a table for the students enrolled in a module

-- Path: assignment.sql

CREATE Table
    teacher (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (course_id) REFERENCES course (id)
    );

-- Create a table for the assignments

-- Path: assignment.sql

CREATE Table
    assignment (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        course_id INTEGER NOT NULL,
        FOREIGN KEY (course_id) REFERENCES course (id)
    );

-- Create a table for the students enrolled in a module