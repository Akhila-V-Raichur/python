class employee():
    def __init__(self):
        self.name=""
        self.salary=0
        self.branch=""
    def getempdetails(self):
        self.name=input("enter the name")
        self.salary=int(input("enter salary"))
        self.branch=input("enter branch")
    def showempdetails(self):
        print("NAME=",self.name)
        print("SALARY=",self.salary)
        print("BRANCH=",self.branch)
    def updtsalary(self):
        self.salary=int(input("enter new salary"))
        print("new salaryy=",self.salary)
e1=employee()
e1.getempdetails()
e1.showempdetails()
e1.updtsalary()