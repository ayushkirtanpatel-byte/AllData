class person:
    
    def __init__(self,name,age,):
        self.name=name
        self.age=age
        

    def getdata(self):
            print(f"The name is : {self.name}  age is : {self.age} ")


class employ(person):
    def __init__(self, name, age, id, salary):
        self.id=id
        self.salary=salary
        super().__init__(name, age)

    def getdata(self):
            print(f"The name is : {self.name} id was : {self.id} age is : {self.age} salary is : {self.salary} ")

class manager(employ):
    def __init__(self, name, age, id, salary, department, program):
        self.program=program
        self.department=department
        super().__init__(name, age, id, salary)
    def getdata(self):
            print(f"The name is : {self.name} id was : {self.id} age is : {self.age} salary is : {self.salary} department: {self.department} programing of : {self.program}")



ofice=[]
employlist=[]
managerlist=[]



while True:
    
    print("\nwelcome\n")

    print("enter 1 to creat a person :")
    print("emter 2 to creat a employ : ")
    print("enter 3 to creat a manager :")
    print("enter 4 to show details :")
    print("enter 5 to  exit : \n")


    choice=int(input("enter your choice :"))

    if choice==1:
        Name=(input("enter the name of person : "))
        Age=int(input("enter your age :"))

        pobj = person(Name,Age)
        ofice.append(pobj)
        print("\nThe person was created 👍")

    elif choice==2:
        Name=(input("enter the name of person : "))
        Age=int(input("enter your age :"))
        Id=int(input("enter employ id :"))
        Salary=int(input("enter the amount of salary :"))

        eobj = employ(Name,Age,Id,Salary)
        employlist.append(eobj)
        print("\nthe emplo was created 👍")

    elif choice==3:
        Name=(input("enter the name of person : "))
        Age=int(input("enter your age :"))
        Id=int(input("enter employ id :"))
        Salary=int(input("enter the amount of salary :"))
        Department=(input("enter the drpartment of manager : "))
        program=(input("enter the language of programer knows :"))

        mobj = manager(Name,Age,Id,Salary,Department,program)
        managerlist.append(mobj)
        print("\nThe manager was created 👍")

    elif choice==4:
         
         print("enter 1 to show person data :")
         print("enter 2 to shpw employ data :")
         print("enter 3 to show manger data :") 

         num=int(input("\nenter your number : "))


         if num==1:
              for pobj in ofice:
                   pobj.getdata()

         elif num==2:
              for eobj in employlist:
                   eobj.getdata()

         elif num==3:
              for mobj in managerlist:
                   mobj.getdata()
         

    elif choice==5:
         print("exiting ... !")
         break
    
    else:
         print("ENTER VALID CHOICE : ")