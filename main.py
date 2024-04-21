import psycopg2

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

            # Create some tables
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
                    location location
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

            # Insert random values
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

            # Random SELECT QUERIES
            cursor.execute("SELECT * FROM clients;")
            print("Clients:")
            for row in cursor.fetchall():
                print(row)

            cursor.execute("SELECT name, employees_count FROM departments;")
            print("\nDepartments:")
            for row in cursor.fetchall():
                print(*row)

            class Project:
                def __int__(self, project_name, end_date, budget):
                    self.project_name = project_name,
                    self.end_date = end_date,
                    self.budget = budget

                def __repr__(self):
                    return f'Project: {self.project_name} ends on {self.end_date} and costs {self.budget}$.'


            cursor.execute("SELECT project_name, end_date, budget FROM projects;")
            print("\nProjects:")
            projects = [Project(*row) for row in cursor.fetchall()]
            for project in projects:
                print(project)

            cursor.execute("""
                SELECT
                    p.project_name,
                    p.start_date,
                    p.end_date,
                    p.budget,
                    c.name AS client_name,
                    c.country AS client_country
                FROM
                    projects AS p
                JOIN
                    clients AS c ON p.client_id = c.id;
            """)

            [print(row) for row in cursor.fetchall()]

            cursor.execute("""
                SELECT 
                    e.first_name,
                    e.last_name,
                    e.job_title,
                    p.project_name,
                    d.name AS department_name
                FROM 
                    employees AS e
                JOIN 
                    projects AS p ON e.project_id = p.id
                JOIN 
                    departments AS d ON e.department_id = d.id
                ORDER BY 
                    e.first_name,
                    e.last_name;
                """)

            [print(row) for row in cursor.fetchall()]

            connection.commit()

            print("Success!")

            connection.close()
        except psycopg2.DatabaseError as e:
            print('Error with query:', e)
            connection.rollback()
        except Exception as e:
            print('Error:', e)
except (Exception, psycopg2.DatabaseError) as e:
    print('Unable to connect to the database:', e)
