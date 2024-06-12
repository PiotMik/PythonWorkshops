# import numpy as np
# import matplotlib.pyplot as plt

# if __name__=="__main__":

#     n = 1000
#     X = np.zeros(n)
#     for i in range(n):
#         X[i] = np.random.random()
#     plt.plot(X)
#     plt.show()
#     #print("UwU",x)

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return self.greet() #gdy ktoś weźmie printa to go przywita

    def greet(self):
        return f"Hi, my name is {self.name} {self.surname}!"

    #dekorator z małpą
    @property   #zamiast fullname() jest fullname
    def fullname(self):
        return f"{self.name} {self.surname}"

    @classmethod
    def from_dict(cls, d: dict):   #by czytało inne formaty #cls to klasa np pies, self to konkretna osoba
        return cls(name = d['name'], surname = d['surname'], age = d['age'])

class Student(Person): #student też człowiek, cyk dziedziczenie

    def __init__(self, name: str, surname: str, age: int, faculty: str):    #informacja dla developera, czystość kodu
        super().__init__(name = name ,surname = surname ,age = age) #podpowiada potem po kropce funkcje
        self.faculty = faculty

    def greet(self) -> str:     #podpowiada co ma zwracać
        parent_greeting = super().greet()
        return f"{parent_greeting} I study {self.faculty} :("


if __name__ == "__main__":
    user_dict = {#dane ale w innym formacie, adapter patern tzn niech czyta wiele
        "name": "Piotr",
        "surname": "Mikler",
        "age": 27   
    }


    person0 = Person(name = "Piotr", surname = "Mikler", age = 27)
    person1 = Person.from_dict(user_dict)
    person2 = Student("Maciej", "Trus", 27, "WMS")
    print(person1.fullname)
    print(person2)


