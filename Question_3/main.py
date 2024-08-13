import os
EMPLOYEES_FILE = 'employees.txt'
PERFORMANCE_FILE = 'performance.txt'
SALARIES_FILE = 'salaries.txt'

def load_file(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as file:
        return file.readlines()

def save_to_file(file_name, data):
    with open(file_name, 'w') as file:
        file.writelines(data)

def add_employee(employee_id, name, age, position, salary):
    employees = load_file(EMPLOYEES_FILE)
    employees.append(f"{employee_id},{name},{age},{position},{salary}\n")
    save_to_file(EMPLOYEES_FILE, employees)
    print(f"Employee {name} added successfully.")

def view_employees():
    employees = load_file(EMPLOYEES_FILE)
    if not employees:
        print("No employees available.")
        return
    for employee in employees:
        emp_id, name, age, position, salary = employee.strip().split(',')
        print(f"ID: {emp_id}, Name: {name}, Age: {age}, Position: {position}, Salary: {salary}")

def update_employee(employee_id, name=None, age=None, position=None, salary=None):
    employees = load_file(EMPLOYEES_FILE)
    updated = False
    with open(EMPLOYEES_FILE, 'w') as file:
        for employee in employees:
            emp_id, old_name, old_age, old_position, old_salary = employee.strip().split(',')
            if emp_id == employee_id:
                if name is None:
                    name = old_name
                if age is None:
                    age = old_age
                if position is None:
                    position = old_position
                if salary is None:
                    salary = old_salary
                file.write(f"{employee_id},{name},{age},{position},{salary}\n")
                updated = True
            else:
                file.write(employee)
    if updated:
        print(f"Employee {employee_id} updated successfully.")
    else:
        print(f"Employee {employee_id} not found.")

def add_performance(employee_id, metric_name, value):
    performance = load_file(PERFORMANCE_FILE)
    performance.append(f"{employee_id},{metric_name},{value}\n")
    save_to_file(PERFORMANCE_FILE, performance)
    print(f"Performance metric {metric_name} for employee {employee_id} added.")

def view_performance():
    performance = load_file(PERFORMANCE_FILE)
    if not performance:
        print("No performance metrics available.")
        return
    for metric in performance:
        emp_id, metric_name, value = metric.strip().split(',')
        print(f"Employee ID: {emp_id}, Metric: {metric_name}, Value: {value}")

def calculate_salary(employee_id):
    employees = load_file(EMPLOYEES_FILE)
    performance = load_file(PERFORMANCE_FILE)
    salaries = load_file(SALARIES_FILE)
    
    emp_salary = None
    for employee in employees:
        emp_id, _, _, _, salary = employee.strip().split(',')
        if emp_id == employee_id:
            emp_salary = float(salary)
            break
    
    if emp_salary is None:
        print(f"Employee {employee_id} not found.")
        return
    
    bonus = 0
    for metric in performance:
        emp_id, metric_name, value = metric.strip().split(',')
        if emp_id == employee_id:
            bonus += float(value) * 0.01
    
    total_salary = emp_salary + bonus
    salaries.append(f"{employee_id},{total_salary}\n")
    save_to_file(SALARIES_FILE, salaries)
    print(f"Salary and bonus for employee {employee_id} calculated. Total: {total_salary}")

def view_salaries():
    salaries = load_file(SALARIES_FILE)
    if not salaries:
        print("No salaries calculated.")
        return
    for salary in salaries:
        emp_id, total_salary = salary.strip().split(',')
        print(f"Employee ID: {emp_id}, Total Salary: {total_salary}")

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Add Performance Metric")
        print("5. View Performance Metrics")
        print("6. Calculate Salary")
        print("7. View Salaries")
        print("8. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            age = input("Enter employee age: ")
            position = input("Enter employee position: ")
            salary = input("Enter employee salary: ")
            add_employee(emp_id, name, age, position, salary)
        elif choice == '2':
            view_employees()
        elif choice == '3':
            emp_id = input("Enter employee ID to update: ")
            name = input("Enter new name (leave blank to keep current): ") or None
            age = input("Enter new age (leave blank to keep current): ") or None
            position = input("Enter new position (leave blank to keep current): ") or None
            salary = input("Enter new salary (leave blank to keep current): ") or None
            update_employee(emp_id, name, age, position, salary)
        elif choice == '4':
            emp_id = input("Enter employee ID: ")
            metric_name = input("Enter performance metric name: ")
            value = input("Enter performance metric value: ")
            add_performance(emp_id, metric_name, value)
        elif choice == '5':
            view_performance()
        elif choice == '6':
            emp_id = input("Enter employee ID to calculate salary: ")
            calculate_salary(emp_id)
        elif choice == '7':
            view_salaries()
        elif choice == '8':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
