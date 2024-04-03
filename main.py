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
   


