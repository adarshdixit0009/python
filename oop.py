# class Car:
#     def __init__(self,brand,color):
#       self.brand=brand
#       self.color=color

#     def start(self):  
#       print(f"{self.color}{self.brand}is starting...")

# car1=Car("white  ","Tata ")
# car2=Car("green ","mahindra ")

# car1.start()
# car2.start() 

# instance Vs class variables


# class Employee:
#     company="Tech crop"

#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

# e1=Employee("John",50000)         
# e2=Employee("Emma",60000) 

# print(e1.salary,e1.company,e1.name)
# print(e2.salary,e2.company,e2.name)


# inheritance  


# class animal:  
#  def speak(self):
#     print("animals make sounds")

# class Dog(animal):
#     def bark(self):
#         print("Dog barks!")

# d=Dog()
# d.speak()
# d.bark()   


# method overriding

# class animal:
#     def sound(self):
#         print("some generic sound")

# class Cat(animal):
#     def sound(self):
#         print("Meow!")

# a=animal()
# c=Cat()
# a.sound()
# c.sound()          

# question 1 


# class student:
#     def __init__(self,name,rollno,marks):
#      self.name=name
#      self.rollno=rollno
#      self.marks=marks

#     def start(self):
#        print(f"{self.name}{self.rollno}{self.marks} is getting")

# student1=student("abhay ","12345 ",85)      
# student2=student("aman ","12346  ",90)      
# student3=student("abhi ","12347 ",82)     

# student1.start()
# student2.start()
# student3.start()
   

# question2

# class circle: 

    
#     def __init__(self,r):
#         self.r=r

#     def area(self,r):
#         print(3.14*r*r)

#     def circumference(self)    


# encapsulation   
 
# class bankaccount:
#  def __init__(self,owner,balance):
#   self.owner=owner
#   self.__balance=balance

#  def deposit(self,amount):
#   self.__balance+=amount

#  def get_balance(self):
#    return self.__balance
    

# acc=bankaccount("alice",10000)
# acc.deposit(5000)
# print(acc.get_balance())    

# question1

# class student:
#   def __init__(self,marks):
    
#      self.marks=marks 


#   def display_marks(self):
#     print("marks:",self.marks)

# s1=student(95)
# s1.display_marks()       


