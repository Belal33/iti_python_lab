import psycopg2

#  connect to the data base
db = psycopg2.connect("dbname=pythonlab5 user=belal")
cursor = db.cursor()


cursor.execute("Drop table employee")

# cursor.execute(
#     """
# CREATE TABLE IF NOT EXISTS employee (
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(255) NOT NULL,
#     last_name VARCHAR(255) NOT NULL,
#     age INTEGER NOT NULL,
#     department VARCHAR(255) NOT NULL,
#     salary INTEGER NOT NULL
# )
# """
# )

db.commit()


class Employee:
    first_name: str
    last_name: str
    age: str
    department: str
    salary: str
    __employees: list["Employee"] = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        type(self).__employees.append(self)

    def transfer(self, new_department: str):
        self.department = new_department

    def fire(self):
        type(self).__employees.remove(self)
        # delete its record form database

    def show(self):
        print(f"fname: {self.first_name}")
        print(f"lname: {self.last_name}")
        print(f"age: {self.age}")
        print(f"department: {self.department}")
        print(f"salary: {self.salary}")

    def list_employees(self):
        for employee in type(self).__employees:
            employee.show()


class Manager(Employee):
    managed_department = None

    def __init__(
        self, first_name, last_name, age, department, salary, managed_department
    ):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def show(self):
        # Will print all data except the salary will print confidential instead of the salary value
        sal = self.salary
        self.salary = "Confidential"
        super().show()
        print(f"managed department: {self.managed_department}")
        self.salary = sal


"""
Let the app be use command interface as follow:
	● Print a menu for the user with the operation he can do and the key word to
	enter for running an operation, for example:
	● For adding new employee enter “add”
	If manager press “m”/ if employee press ‘e’
	Please insert data
	Name:>>
	Age:>>
	And so on.
	● The final option in the menu should be q for exiting the program
"""
