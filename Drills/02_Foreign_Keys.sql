CREATE TABLE employees (
    employee_id INTEGER   NOT NULL,
    first_name VARCHAR   NOT NULL,
    last_name VARCHAR   NOT NULL,
    department_id INTEGER   NOT NULL,
    CONSTRAINT pk_employees PRIMARY KEY (
        employee_id
     )
);

INSERT INTO employees (employee_id, first_name, last_name, department_id)
VALUES (14, 'Jan', 'Jansson', 45), (17, 'Sam', 'Samuels', 45);

CREATE TABLE departments (
    id INTEGER   NOT NULL,
    dept_name VARCHAR   NOT NULL
);

INSERT INTO departments (id, dept_name)
VALUES (45, 'webdev'), (45, 'webdev');


ALTER TABLE departments ADD CONSTRAINT fk_departments_id FOREIGN KEY(id)
REFERENCES employees (department_id);