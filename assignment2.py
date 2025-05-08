class EmployeeManager:
    def __init__(self):
        # List to hold employee records (each as a dictionary)
        self.employees = []

    def add_employee(self, emp_id, name, department):
        # Add a new employee dictionary to the list
        employee = {
            "id": emp_id,
            "name": name,
            "department": department
        }
        self.employees.append(employee)
        print(f"✅ Added employee {name}.")

    def update_employee(self, emp_id, name=None, department=None):
        # Find and update an employee by ID
        for emp in self.employees:
            if emp["id"] == emp_id:
                if name:
                    emp["name"] = name
                if department:
                    emp["department"] = department
                print(f"🔄 Updated employee ID {emp_id}.")
                return
        print(f"❌ Employee ID {emp_id} not found.")

    def delete_employee(self, emp_id):
        # Remove an employee by ID
        for emp in self.employees:
            if emp["id"] == emp_id:
                self.employees.remove(emp)
                print(f"🗑️ Deleted employee ID {emp_id}.")
                return
        print(f"❌ Employee ID {emp_id} not found.")

    def display_all_employees(self):
        # Display all employee records
        if not self.employees:
            print("No employees to display.")
        else:
            print("\n📋 All Employees:")
            for emp in self.employees:
                print(f"ID: {emp['id']}, Name: {emp['name']}, Department: {emp['department']}")

# Example usage
if __name__ == "__main__":
    manager = EmployeeManager()

    # Adding employees
    manager.add_employee(101, "Alice", "HR")
    manager.add_employee(102, "Bob", "Finance")

    # Updating employee
    manager.update_employee(101, department="Recruitment")

    # Deleting employee
    manager.delete_employee(102)

    # Displaying all employees
    manager.display_all_employees()
