from db_conn import conn

cursor = conn.cursor()

cursor.execute('''CREATE TABLE employee_package(
               id SERIAL PRIMARY KEY, 
               employee_id INT NOT NULL, 
               basic_salary INT NOT NULL, 
               house_rent_allowance INT NOT NULL, 
               conveyance_allownce INT NOT NULL, 
               fixed_allowance INT NOT NULL, 
               other_allowance INT NOT NULL, 
               cost_to_company INT NOT NULL, 
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
               updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
               )''')

conn.commit()
cursor.close()
conn.close()
