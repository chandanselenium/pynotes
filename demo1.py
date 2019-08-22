#oops concepts

'''class Student():
    def __init__(self):
        self.name="chandan"
        self.age=10
        self.marks=28

    def disp(self):
        print('name of the student is',self.name)
        print('age of the student is',self.age)
        print('marks of the student is',self.marks)

obj=Student()
obj.disp()'''

'''class Student():
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def disp(self):
        print('name of the student is ',self.name)
        print('age of the students is ',self.age)
        print('marks of the student is ',self.marks)
        print('****************************************')

obj=Student('chandan',10,25)
obj1=Student('harshith',25,25)
obj.disp()
obj1.disp()'''

'''class Student():
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def disp(self):
        print('name of the student ={}\n age={}\n marks={}'.format(self.name,self.age,self.marks))

obj=Student('chandan',10,30)
obj1=Student('harshith',30,30)
obj.disp()
obj1.disp()'''

'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def disp(self):
        print('name of the student:',self.name)
        print('marks of the student:',self.marks)

    def grade(self):
        if self.marks >= 75:
            print("distintion")
        elif self.marks<=75 and self.marks>=60:
            print('first class')
        elif self.marks<60 and self.marks>=45:
            print('second class')
        elif self.marks<45 and self.marks>=35:
            print('third class')
        else:
            print('fail')

n=input('enter the number of students')
for i in n:
    name=input('enter the name:')
    marks=int(input('enter the marks:'))
    s1=Student(name,marks)
    s1.disp()
    s1.grade()

class Animal:
    a=4
    @classmethod
    def anileg(self):
        print('the animal {} legs'.format(self.a))

Animal.anileg()'''




'''n=int(input('enter the length of elements'))
l1=[]
for i in range(1,n+1):
    l2=input('enter the number')
    l1.append(l2)
l1.sort()
print(l1[-1])'''

l1=list(eval(input('enter the element of list one')))
l2=list(eval(input('enter the numbers of list two')))
l1.extend(l2)
l1.sort()
print(l1)











