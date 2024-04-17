#how to make a class
class Student():
    #age=7
    #name="Elizabeth"
    #school="CherryElementry"
    #classteacher="Mrs.Quick"
    #grade=2
    #constructor
    def __init__(self):
        self.age=7
        self.name="Elizabeth"
        self.school="CherryElementry"
        self.classteacher="Mrs.Quick"
        self.grade=2
    def changeDetails(self):
        self.name=input("What is your name?") 
        self.age=input("How old are you?") 
        self.grade=input("What grade are you in?")
        self.classteacher=input("Who is your teacher?") 
    def printDetails(self):
        print ("The properties of the students are:",self.name,self.age,self.grade,self.classteacher,self.school)
Aahana=Student()
Aahana.changeDetails()
Aahana.printDetails()
Anya=Student()
Anya.changeDetails()
Anya.printDetails()
Mia=Student()
Mia.changeDetails()
Mia.printDetails()
Noy=Student()
Noy.changeDetails()
Noy.printDetails()
#Make a car class 
class car():
    def _init_(self):
        self.color="teal"
        self.model="outback"
        self.size="large"
        self.year_made=2022
        self.company="Maserati"
    def changeCar(self):
        self.color=input("what color is the car")
        self.model=input("what model is the car")
        self.size=input("what size is your car?")
        self.year_made=input("what year was the car made")
        self.company=input("what company made this car")
        print("the properties of the students are:",self.color,self.model,self.size,self.year_made,self.company)
Lexus=car()
Lexus.changeCar()


