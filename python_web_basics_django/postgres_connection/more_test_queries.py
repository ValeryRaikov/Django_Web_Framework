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
            # cursor.execute("""
            #     SELECT name, country
            #     FROM clients
            #     ORDER BY name;
            # """)
            #
            # [print(row) for row in cursor.fetchall()]

            # cursor.execute("""
            #     SELECT name, employees_count
            #     FROM departments
            #     WHERE employees_count > 300
            #     ORDER BY employees_count DESC;
            # """)
            #
            # [print(row) for row in cursor.fetchall()]

            # cursor.execute("""
            #     SELECT
            #         CONCAT(first_name, ' ', last_name) AS full_name,
            #         job_title
            #     FROM employees
            #     ORDER BY full_name;
            # """)
            #
            # [print(f'Full name: {row[0]}, Job Title: {row[1]}') for row in cursor.fetchall()]

            # cursor.execute("SELECT SUM(budget) FROM projects")
            # print(f'Total income: {cursor.fetchone()[0]}$')

            cursor.execute("""
                SELECT 
                    CONCAT(e.first_name, ' ', e.last_name) AS full_name,
                    e.job_title,
                    p.project_name,
                    p.budget,
                    c.name,
                    c.country
                FROM employees AS e 
                JOIN projects AS p ON e.project_id = p.id
                JOIN clients AS c ON p.client_id = c.id;
            """)

            [print(row) for row in cursor.fetchmany(10)]

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
