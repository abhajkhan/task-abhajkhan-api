from repositories.employee_package_repository import fetch_employee_package_details, edit_employee_package_details
from flask import jsonify, request

def get_employee_package_details(employee_id):
    employee_package = fetch_employee_package_details(employee_id)
    return jsonify(employee_package) if employee_package else ("Employee package not found", 404)

def update_employee_package_details(employee_id):

    data = request.json
    if not data:
        return jsonify({"message": "Request body is empty"}), 400
    
    required_fields = ['cost_to_company', 'basic_salary_percentage', 'hra_percentage', 'conveyance_allowance', 'fixed_allowance_percentage']
    if not all(field in data for field in required_fields):
        return jsonify({"message": "Required fields are missing"}), 400
    
    ctc = data['cost_to_company']
    basic_salary_percentage = data['basic_salary_percentage']
    hra_percentage = data['hra_percentage']
    conveyance_allowance = data['conveyance_allowance']
    fixed_allowance_percentage = data['fixed_allowance_percentage']

    if ctc <= 0:
        return jsonify({"message": "Cost to company cannot be negative"}), 400
    
    if any(value < 0 or value > 100 for value in [basic_salary_percentage, hra_percentage, fixed_allowance_percentage]):
        return jsonify({"message": "Percentage values should be between 0 and 100"}), 400

    basic_salary = (ctc * basic_salary_percentage) / 100
    hra = (ctc * hra_percentage) / 100
    fixed_allowance = (ctc * fixed_allowance_percentage) / 100
    other_allowance = ctc - (basic_salary + hra + fixed_allowance + conveyance_allowance)

    package_details = {
        "basic_salary": basic_salary,
        "house_rent_allowance": hra,
        "conveyance_allowance": conveyance_allowance,
        "fixed_allowance": fixed_allowance,
        "other_allowance": other_allowance,
        "cost_to_company": ctc,
    }
    success = edit_employee_package_details(employee_id, package_details)
    if success:
        return jsonify({"message": "Package updated successfully"}), 200
    return jsonify({"message": "Employee not found"}), 404
