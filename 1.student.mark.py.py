course=[]
student=[]
nc=0
ns=0
name0=str(0)
stumark={}

#input number of students in a class
def numcourse():
    ns=input("Enter number of students in a class:") 
    

#input number of courses
def numcourse():
    nc=input("Enter number of courses:")

# input course info      
def Courseinfo():
        print("Enter 0 for COURSE NAME if you want to stop inputting\n")
        while(1):
          name=input("Enter COURSE NAME:")
          #name1 = str(name) : không cần đổi name thành string kể cả khi là 0
          if name != name0: 
             id=input("Enter course id:")
             linec = f"{name}-{id}"
             course.append(linec)
          else :
             break   


# input studnet info
def Studentinfo():
        print("Enter 0 for STUDENT NAME if you want to stop inputting\n")
        while(1):
          names=input("Enter STUDENT NAME:")
          if names != name0:
             id=input("Enter student id:")
             dOB=input("Enter stuent dOB:") 
             lines = f"{names}-{id}-{dOB}"
             student.append(lines)
          else :
             break                 


#listing courses 
def Courselist():
    print("THE COURSE LIST :")
    for i in range(len(course)):
        print(course[i])


#listing students
def Studentlist():
    print("THE STUDENTS LIST :")
    for i in range(len(student)):
        print(student[i])    


#input student's marks for a course
def Studentmark():
    s = input("Input the subject:")                                      
    mark=[]
    stumark[s]=mark
    for i in range(len(student)):
        m=input(f"{student[i]}'s mark in {s} is:")   
        mark.append(m)  

#show student marks list         
def ListStudentmark():
    s = input("Input the subject:")
    if s in stumark:
     print(f"LIST OF  STUDENT's {s} MARK:")
     for i in range(len(student)):
        print(f"{student[i]}-mark:{stumark[s][i]}")    
    else:
        print("Subject not found,please use Studentmark() to add new course")

Courseinfo()
Studentinfo()
Courselist()
Studentlist()
Studentmark()
ListStudentmark()
