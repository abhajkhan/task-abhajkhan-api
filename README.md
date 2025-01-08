**API Contract**
---
API = */api/employees/<int:employee_id>/employee_package*

method = `"GET"`

    response = {
	    "basic_salary": 400000,
	    "conveyance_allownce": 1600,
	    "cost_to_company": 1000000,
	    "employee_id": 1,
	    "fixed_allowance": 300000,
	    "house_rent_allowance": 200000,
	    "id": 1,
	    "other_allowance": 98400,
	    "updated_at": "Tue, 07 Jan 2025 17:25:08 GMT"
	    }


---
API = */api/employees/<int:employee_id>/employee_package*

method = `"PUT"`

body = 

    {
	    "cost_to_company": 1000000,
	    "basic_salary_percentage": 40,
	    "hra_percentage": 20,
	    "conveyance_allowance": 1600,
	    "fixed_allowance_percentage": 30
    }

response =

    {
	    "message": "Employee package updated successfully"
    }
     