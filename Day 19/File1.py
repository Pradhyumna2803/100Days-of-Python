class Employee:
    def __init__(self,id, name):
        self.id = id
        self.name = name

    def showDetails(self):
        print(f'ID: {self.id}\nName: {self.name}\n')

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")



e1 = Employee(1, 'Rohan')
e1.showDetails()

# e2 = Employee(2,'Harry')
e2 = Programmer(3,'Ganesh Rao')
e2.showDetails()
e2.showLanguage()

