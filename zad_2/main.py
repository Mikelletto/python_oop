class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code} | Hours: {self.open_hours} | Phone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Employee: {self.first_name} {self.last_name}, hired: {self.hire_date}, born: {self.birth_date}, "
                f"address: {self.city}, {self.street}, {self.zip_code}, phone: {self.phone}")


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, marks: {self.marks}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book: {self.author_name} {self.author_surname}, {self.publication_date}, "
                f"pages: {self.number_of_pages}, from → [{self.library}]")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n    ".join(str(book) for book in self.books)
        return (f"ORDER (date: {self.order_date})\n"f"  Employee: {self.employee}\n"f"  Student: {self.student}\n"f"  Books:\n    {books_str}\n")

lib1 = Library("Warszawa", "Marszałkowska 12", "00-001", "8:00-18:00", "555-111-222")
lib2 = Library("Kraków", "Długa 8", "30-002", "9:00-17:00", "555-333-444")

book1 = Book(lib1, "2001", "Adam", "Mickiewicz", 350)
book2 = Book(lib1, "1998", "Henryk", "Sienkiewicz", 280)
book3 = Book(lib2, "2010", "Olga", "Tokarczuk", 400)
book4 = Book(lib2, "2020", "Andrzej", "Sapkowski", 500)
book5 = Book(lib1, "1980", "Stanisław", "Lem", 300)

emp1 = Employee("Jan", "Kowalski", "2015-01-10", "1990-03-21", "Warszawa", "Kwiatowa 5", "00-123", "555-000-111")

emp2 = Employee("Anna", "Nowak", "2018-05-15", "1992-11-02","Kraków", "Lipowa 7", "30-345", "555-000-222")

emp3 = Employee("Piotr", "Zieliński", "2020-09-01", "1995-07-10","Warszawa", "Leśna 9", "00-567", "555-000-333")

stu1 = Student("Kamil", [60, 70, 90])
stu2 = Student("Julia", [30, 40, 50])
stu3 = Student("Marek", [80, 85, 88])

order1 = Order(emp1, stu1, [book1, book3], "2024-01-15")
order2 = Order(emp2, stu3, [book4, book5, book2], "2024-02-01")

# WYŚWIETLENIE ZAMÓWIEŃ

print(order1)
print(order2)
