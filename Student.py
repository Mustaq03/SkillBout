class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        if self.__marks>100 or self.__marks<0:
            print("Error: marks should be between 0 and 100")
        return self.__marks

stu=Student("mustaq",105)
stu.set_name("mustaq")
print("Student name:",stu.get_name())
stu.set_marks(105)
print("Student marks:",stu.get_marks())