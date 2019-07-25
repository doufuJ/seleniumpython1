from c5 import Human


class student(Human):
    # sum = 0
    def __init__(self, school , name , age):
        self.school = school
        Human.__init__(self , name , age)
        # self.score = 0
        # self.__class__.sum += 1

    def do_homework(self):
        print('english homework')


student1 = student('泡桐树小学','张三',18)
# print(student1.sum)
# print(student.sum)
print(student1.name)
print(student1.age)
# student1.get_name()