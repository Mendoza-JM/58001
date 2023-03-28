class Person:
    def __init__(self, std, pre, mid, fin):
        self.__std = std
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

    def display(self):
        print(self.__std, ", your prelim grade is", self.__pre)
        print(self.__std, ", your midterm grade is", self.__mid)
        print(self.__std, ", your finals grade is", self.__fin)

    def Grade(self):
        print("Your average Grade is", int((self.__pre + self.__mid + self.__fin) / 3))
        print()


class std1(Person):
    pass


class std2(Person):
    pass


class std3(Person):
    pass


student1 = std1("JM", 95, 85, 80)
student1.display()
student1.Grade()

student2 = std2("MJ", 75, 70, 80)
student2.display()
student2.Grade()

student3 = std3("Miguel", 90, 70, 80)
student3.display()
student3.Grade()