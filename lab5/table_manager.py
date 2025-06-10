import psycopg2

#  connect to the data base
# db = psycopg2.connect("dbname=pythonlab5 user=belal")
# cursor = db.cursor()

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

# db.commit()


class DBModel:

    _primary_key: str = "id"
    _field_definations: dict = {}
    _table_name: str

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)
        cls._table_name = cls.__name__.lower()
        cls._create_table()

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k in self._get_fields():
                setattr(self, k, v)
            else:
                raise ValueError(f"Invalid field name {k}")

    @classmethod
    def _create_table(cls):
        table_name = cls._get_table_name()
        definations = [f"{fn} {fd}" for fn, fd in cls._get_definations().items()]

        with cls._get_connection() as conn:
            with conn.cursor() as cursor:

                cursor.execute(
                    f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
        {', '.join(definations)}
        )
        """
                )
            conn.commit()

    @classmethod
    def _get_connection(cls):
        """Get a database connection"""
        return psycopg2.connect("dbname=pythonlab5 user=belal")

    @classmethod
    def _get_table_name(cls) -> str:
        """Get the table name"""
        name = cls.__name__
        if hasattr(cls, "_table_name"):
            name = cls._table_name
        print(name)
        return name.lower()

    @classmethod
    def _get_definations(cls):
        fields_definations = cls._field_definations.copy()
        for field in cls._get_fields():
            if field in fields_definations:
                continue
            fields_definations[field] = cls._get_field_type(field)
        return fields_definations

    @classmethod
    def _get_field_type(cls, field_name: str):
        field_type = cls.__annotations__.get(field_name)
        if field_name == cls._primary_key:
            return "SERIAL PRIMARY KEY"
        if field_type == str:
            return "VARCHAR(255)"
        elif field_type == int:
            return "INTEGER"
        elif field_type == float:
            return "REAL"
        elif field_type == bool:
            return "BOOLEAN"

    @classmethod
    def _get_fields(cls):
        fields_names = [cls._primary_key]
        for attr_name in cls.__annotations__:
            if not attr_name.startswith("_"):
                fields_names.append(attr_name)
        return fields_names

    @classmethod
    def get(cls, **kwargs) -> list:
        """get  table record"""
        field_name = cls._primary_key
        for k in kwargs:
            if k not in cls._get_fields():
                raise ValueError(f"Invalid field name {k}")
            field_name = k
        with cls._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    f"SELECT * FROM {cls._get_table_name()} WHERE {field_name}='{kwargs[field_name]}' ;"
                )
                v = cursor.fetchall()
                return v

    @classmethod
    def get_by_pk(cls, pk):
        """get  table record"""
        with cls._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    f"SELECT * FROM {cls._get_table_name()} WHERE {cls._primary_key}='{pk}' ;"
                )
                v = cursor.fetchone()
                return v

    @classmethod
    def list_all(cls):
        """get all table records"""
        with cls._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {cls._get_table_name()};")
                v = cursor.fetchall()
                print(type(v))

    def save(self):
        fields_names = [
            f_name for f_name in self._get_fields() if f_name != self._primary_key
        ]
        q = f"""
INSERT INTO {self._get_table_name()} ({', '.join(fields_names)}) VALUES ( '{("', '".join([str(getattr(self, fn)) for fn in fields_names]))}' ) ;
"""
        print(q)

        with self._get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(q)
            conn.commit()


class Employee(DBModel):
    first_name: str
    last_name: str
    age: int
    department: str
    salary: float
    managed_department: str = ""


# emp = Employee(
#     first_name="bb",
#     last_name="elbanna",
#     age=22,
#     department="dprt1",
#     salary=22000,
# )
# emp.save()
# Employee.list_all()
# Employee.get_by_pk(1)
# Employee.get(first_name="bb")
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


def main():
    while True:
        print("Menu:")
        print("1. Add Employee (add)")
        print("2. List All Employees (list)")
        print("3. Get Employee by ID (get)")
        print("4. Exit (q)")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "add":
            try:
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                age = int(input("Age: "))
                department = input("Department: ")
                salary = float(input("Salary: "))
                emp = Employee(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    department=department,
                    salary=salary,
                )
                emp.save()
                print("Employee added successfully.")
            except ValueError as e:
                print(f"Error: {e}. Please enter valid data.")
                continue

        elif choice == "list":
            Employee.list_all()

        elif choice == "get":
            try:
                emp_id = int(input("Enter Employee ID: "))
                employee = Employee.get_by_pk(emp_id)
                if employee:
                    print(f"Employee Details: {employee}")
                else:
                    print("Employee not found.")
            except ValueError:
                print("Invalid ID. Please enter a valid integer.")

        elif choice == "q":
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
