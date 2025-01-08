from db.db_conn import conn

def fetch_employee_package_details(employee_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id,employee_id,basic_salary,house_rent_allowance,conveyance_allownce,fixed_allowance,other_allowance,cost_to_company,updated_at FROM employee_package WHERE employee_id = %s", (employee_id,))
        data = cursor.fetchone()
        if data:
            employee_package = {
                "id": data[0],
                "employee_id": data[1],
                "basic_salary": data[2],
                "house_rent_allowance": data[3],
                "conveyance_allownce": data[4],
                "fixed_allowance": data[5],
                "other_allowance": data[6],
                "cost_to_company": data[7],
                "updated_at": data[8]
            }
            return employee_package
    except Exception as e:
        print("fetching failed", e)
    finally:
        cursor.close()

def edit_employee_package_details(employee_id,package_details):
    try:
        cursor = conn.cursor()
        cursor.execute('''UPDATE employee_package 
                       SET basic_salary=%s,
                       house_rent_allowance=%s,
                       conveyance_allownce=%s,
                       fixed_allowance=%s,
                       other_allowance=%s,
                       cost_to_company=%s ,
                        updated_at=NOW()
                       WHERE employee_id=%s
                       RETURNING id
                       ''', (
                           package_details['basic_salary'],
                           package_details['house_rent_allowance'],
                           package_details['conveyance_allowance'],
                           package_details['fixed_allowance'],
                           package_details['other_allowance'],
                           package_details['cost_to_company'],
                           employee_id
                        )
        )

        conn.commit()
        return cursor.fetchone() is not None
    except Exception as e:
        conn.rollback()
        raise e
        
    finally:
        cursor.close()
