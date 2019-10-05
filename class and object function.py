
class student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def good_gpa(self):
        if self.gpa >= 3.5:
            print('Indeed a good gpa')
        elif self.gpa >= 2 or self.gpa < 3.5:
            print('Okay gpa')
        else:
            print('gpa is low')


student1 = student('aman', 21, 3.75)
student2 = student('bman', 22, 3.2)
student3 = student('cman', 23, 1.5)

student1.good_gpa()
student2.good_gpa()
student3.good_gpa()