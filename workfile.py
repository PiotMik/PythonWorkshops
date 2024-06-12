class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return self.greet()

    def greet(self):
        return f"Hi, my name is {self.name} {self.surname}!"

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    @classmethod
    def from_dict(cls, d: dict):
        return cls(name=d["name"], surname=d["surname"], age=d["age"])


class Student(Person):
    def __init__(self, name: str, surname: str, age: int, faculty: str):
        super().__init__(name=name, surname=surname, age=age)
        self.faculty = faculty

    def greet(self) -> str:
        parent_greeting = super().greet()
        return f"{parent_greeting} I study {self.faculty}."


if __name__ == "__main__":
    user_dict = {"name": "Piotr", "surname": "Mikler", "age": 27}

    person1 = Person.from_dict(user_dict)
    person2 = Student("Maciej", "Truś", 27, "Mathematics")
    print(person1.greet())
    print(person2.greet())
