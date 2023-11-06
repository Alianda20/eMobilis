class Students:
    def __init__(self, name, gender, course, age):
        self.name = name
        self.gender = gender
        self.course = course
        self.age = age
    def wanafunzi(self):
        print("Name %s \n Gender %s \n Course %s \n Age %d"%(self.name, self.gender, self.course, self.age))
Stud1=Students("Kelvin Alianda", "Male", "Computer Science", 21)
Stud1.wanafunzi()
Stud2=Students("Anne Mungai", "Female", "Software Engineering", 20)
Stud2.wanafunzi()
