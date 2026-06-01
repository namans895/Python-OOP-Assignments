# Employee Management using Inheritance

class Employee:
    def work(self):
        print("Employee is working")


class Manager(Employee):
    def manage(self):
        print("Manager is managing the team")


# Creating object
m1 = Manager()

m1.work()
m1.manage()
