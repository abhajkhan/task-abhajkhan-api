from route_handlers.employee_route_handler import get_employee_package_details, update_employee_package_details


def register_routes(app):
    app.route('/api/employees/<int:employee_id>/employee_package', methods=['GET'])(get_employee_package_details)
    app.route('/api/employees/<int:employee_id>/employee_package', methods=['PUT'])(update_employee_package_details)
