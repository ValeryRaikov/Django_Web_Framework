import psycopg2


class Project:
    def __init__(self, project_name, start_date, end_date, budget, client_name, client_country):
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.client_name = client_name
        self.client_country = client_country

    def __repr__(self):
        return f'Project: {self.project_name}, Start Date: {self.start_date}, End Date: {self.end_date}, Budget: {self.budget}, Client: {self.client_name} ({self.client_country})'


class Employee:
    def __init__(self, first_name, last_name, job_title, project_name, department_name):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title = job_title
        self.project_name = project_name
        self.department_name = department_name

    def __repr__(self):
        return f'Employee: {self.first_name} {self.last_name}, Job Title: {self.job_title}, Project: {self.project_name}, Department: {self.department_name}'


try:
    connection = psycopg2.connect(
        host='127.0.0.1',
        database='company_demo',
        user='postgres-user',
        password='password',
    )

    with connection.cursor() as cursor:
        try:
            cursor.execute("CREATE TYPE location AS ENUM ('Sofia', 'Plovdiv', 'Varna', 'Stara Zagora', 'Pleven');")

            # Create tables
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    country VARCHAR(50) NOT NULL,
                    address VARCHAR(100),
                    contract_key VARCHAR(16) NOT NULL UNIQUE
                );"""
            )

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS departments (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    employees_count INT NOT NULL CHECK(employees_count > 0),
                    location VARCHAR(50)
                );"""
            )

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS projects (
                    id SERIAL PRIMARY KEY,
                    project_name VARCHAR(50),
                    start_date DATE NOT NULL,
                    end_date DATE NOT NULL CHECK(end_date > start_date),
                    budget INT,
                    client_id INT NOT NULL,
                    FOREIGN KEY (client_id) REFERENCES clients(id) ON UPDATE CASCADE ON DELETE CASCADE
                );"""
            )

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    job_title VARCHAR(100),
                    project_id INT NOT NULL,
                    department_id INT NOT NULL,
                    FOREIGN KEY (project_id) REFERENCES projects(id) ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (department_id) REFERENCES departments(id) ON UPDATE CASCADE ON DELETE CASCADE
                );"""
            )

            # Insert data
            cursor.execute("""
                INSERT INTO clients (name, country, address, contract_key)
                VALUES 
                    ('Volex-2000', 'Bulgaria', 'ul. Institutska №8', '100200300400abcd'),
                    ('Galus-2004', 'Serbia', 'bul. Aleksander Veliki', '100200300400efgh'),
                    ('magnaPharm EOOD', 'Hungary', 'Rompasso st. 8', '100200300400ijk');
            """)

            cursor.execute("""
                INSERT INTO departments (name, employees_count, location)
                VALUES 
                    ('SAP Bulgaria', 550, 'Sofia'),
                    ('Software AG', 300, 'Sofia'),
                    ('VM-Ware', 335, 'Varna'),
                    ('Sirma Solutions', 200, 'Pleven');
            """)

            cursor.execute("""
                INSERT INTO projects (project_name, start_date, end_date, budget, client_id)
                VALUES 
                    ('Front-End React App', '2024-01-01', '2024-03-01', 10000, 1),
                    ('Back-End Java Server', '2024-02-14', '2024-03-14', 25000, 3),
                    ('banking system with Node JS', '2024-04-10', '2024-06-12', 35000, 2);
            """)

            cursor.execute("""
                INSERT INTO employees (first_name, last_name, job_title, project_id, department_id)
                VALUES 
                    ('Valery', 'Raikov', 'Full-stack dev', 1, 2),
                    ('Ivaylo', 'Papazov', 'Front-end dev', 3, 3),
                    ('Maria', 'Mitkova', 'Back-end dev', 2, 1),
                    ('Kalin', 'Stefanov', 'System Admin', 2, 2),
                    ('Lili', 'Petkova', 'DevOps', 3, 1);
            """)

            # Example select queries
            cursor.execute("SELECT * FROM clients;")
            print("Clients:")
            for row in cursor.fetchall():
                print(row)

            cursor.execute("SELECT * FROM departments;")
            print("\nDepartments:")
            for row in cursor.fetchall():
                print(row)

            cursor.execute("SELECT * FROM projects;")
            print("\nProjects:")
            for row in cursor.fetchall():
                print(row)

            cursor.execute("SELECT * FROM employees;")
            print("\nEmployees:")
            for row in cursor.fetchall():
                print(row)

            cursor.execute("""
                SELECT 
                    projects.project_name,
                    projects.start_date,
                    projects.end_date,
                    projects.budget,
                    clients.name AS client_name,
                    clients.country AS client_country
                FROM 
                    projects
                JOIN 
                    clients ON projects.client_id = clients.id;
            """)
            print("\nProjects:")
            projects = [Project(*row) for row in cursor.fetchall()]
            for project in projects:
                print(project)

            cursor.execute("""
                SELECT 
                    employees.first_name,
                    employees.last_name,
                    employees.job_title,
                    projects.project_name,
                    departments.name AS department_name
                FROM 
                    employees
                JOIN 
                    projects ON employees.project_id = projects.id
                JOIN 
                    departments ON employees.department_id = departments.id;
            """)
            print("\nEmployees:")
            employees = [Employee(*row) for row in cursor.fetchall()]
            for employee in employees:
                print(employee)

            connection.commit()

            print('Success!')

            connection.close()
        except psycopg2.DatabaseError as e:
            print('Error with query:', e)
            connection.rollback()
        except Exception as e:
            print('Error:', e)

except (Exception, psycopg2.DatabaseError) as e:
    print('Unable to connect to the database:', e)
