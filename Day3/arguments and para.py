
#program for demotrating positionarguments


#objects defination 
def displayinfor(name,age,classs):
    print("\t{}\t{}\t{}".format(name,age,classs))
    
#main program and calling the funtion after defining the function
print("="*50)
print("\tname\tage\tclasss")
print("="*50)
displayinfor("makia", 12 ,"grade1")
displayinfor("makia", 13 ,"grade2")
displayinfor("makia", 14 ,"grade3") 
displayinfor("makia", 15 ,"grade5")      
print("="*50)
    

#Using default arguments 

#objects defination 
def displayinfor(name,age,classs,cur="Python"):
    print("\t{}\t{}\t{},\t{}".format(name,age,classs,cur))
    
#main program and calling the funtion after defining the function
print("="*50)
print("\tname\tage\tclasss\tcur")
print("="*50)
displayinfor("makia", 12 ,"grade1")
displayinfor("makia", 13 ,"grade2")
displayinfor("makia", 14 ,"grade3") 
displayinfor("makia", 15 ,"grade5")      
print("="*50)

#object defination
def displayinfor(name,age,classs,cur="Python"):
    print("\t{}\t{}\t{},\t{}".format(name,age,classs,cur))
    
#main program and calling the funtion after defining the function
print("="*50)
print("\tname\tage\tclasss\tcur")
print("="*50)
displayinfor("makia", 12 ,"grade1")
displayinfor("makia", 13 ,"grade2")
displayinfor("makia", 14 ,"grade3") 
displayinfor("makia", 15 ,"grade5")      
print("="*50)


#Using keywords arguments 

#object defination 
def displayinfor(name,age,classs,salary,city="kumba"):
    print("\t{}\t{}\t{}\t{}\t{}".format(name,age,classs,salary,city))
    
#main program and calling the funtion after defining the function
print("="*50)
print("\tname\tage\tclasss\tsalary\tcity")
print("="*50)
displayinfor("makia", 12 ,"grade1", 50)
displayinfor("makia", 13 ,"grade2", 49)
displayinfor(salary=50, classs= "kinderger", age=14, name="makia")  
displayinfor("makia", 15 ,"grade5", 60) 
displayinfor(salary=50, classs= "kinderger", age=14, name="makia")  
displayinfor("max", 35,classs="from4", salary= 56)   
print("="*50)


#example2 
def displayinfor(name,age,classs,salary,city="kumba"):
    print("\t{}\t{}\t{}\t{}\t{}".format(name,age,classs,salary,city))
    
#main program and calling the funtion after defining the function
print("="*50)
print("\tname\tage\tclasss\tsalary\tcity")
print("="*50)
displayinfor("makia", 12 ,"grade1", 50)
displayinfor("makia", 13 ,"grade2", 49)
displayinfor(salary=50, classs= "kinderger", age=14, name="makia")  
displayinfor("makia", 15 ,"grade5", 60) 
displayinfor(salary=50, classs= "kinderger", age=14, name="makia")  #using key parameters 
displayinfor("max", 35,classs="from4", salary= 56) #using position and key parameters 
displayinfor("max", 35,classs="from4", salary= 56, city="buea")   
print("="*50)


#Using multiple varialbe in a function 
def disp(a):
    print(a)
def disp2(a,d):
    print(a,d)
def disp3(a,d,c):
    print(a,d,c)
def disp4(a,d,c,b):
    print(a,d,c,b)
    
#call all funtions 
disp(10)
disp2(10,20)
disp3(10,20,30)
disp4(10,20,30,40)

#using key valriable leght 

def disinfor(**R):
    print(R,type(R))
    
disinfor(name="makia",salary="60")
disinfor(name="makia",salary="60",age=50)
disinfor(name="makia",salary=60,age=60,city="fiango")
disinfor(salary=70, name="tom", age=80,city=  "kumba")


#using examples in key varable parameters 

def dispinfor(name,classs,salary,**age):
    print("="*50)
    print("workers Name{}".format(name))
    print("workers classs{}".format(classs))
    print("workers salary{}".format(salary))
    print("="*50)
    print("\tenployeename\temployeedate")
    print("="*50)
    total=7
    for sub,marks in age.items():
        print("\t{}\t{}".format(sub,marks))
        total=total+marks
    print("="*50)
    print("Total money={}".format(total))
    print("="*50)
    
dispinfor("makia","grade1",500,tom=78,kel=76,jeo=87,ugo=97)
    

