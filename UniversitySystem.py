class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


class Lecturer(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


class Staff(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def display_info(self):
        super().display_info()
        print(f"Role: {self.role}")


# Example usage
print("=== Student ===")
s = Student("Alice", 20, "S12345")
s.display_info()

print("\n=== Lecturer ===")
l = Lecturer("Dr. John", 45, "Computer Science")
l.display_info()

print("\n=== Staff ===")
st = Staff("Mr. Paul", 38, "Administrator")
st.display_info()
