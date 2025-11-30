class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    
    def isPassed(self):
        return sum(self.marks) / len(self.marks) > 50
    

stud1 = Student("Anna",[51,42,70])
stud2 = Student("Piotr",[40,30,50])

print(f"Imie: {stud1.name},  Srednia z ocen >50: {stud1.isPassed()}")
print(f"Imie: {stud2.name},  Srednia z ocen >50: {stud2.isPassed()}")