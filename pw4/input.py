student=[]
course=[]
numcredit=[]
stumark={}
name0=str(0)
sumcredit=0
sortGPA={}
def numcourse():
    ns=input("Enter number of students in a class:") 
def numstudent():
    nc=input("Enter number of students:") 


def Studentinfo():         
 print("Enter 0 for STUDENT NAME if you want to stop inputting\n")
 while(1):
    names=input("Enter STUDENT NAME:")
    if names != name0:
       id=input("Enter student id:")
       dOB=input("Enter stuent dOB:") 
       stuinfo=StudentInfo(dOB)
       stuinfo.set__ID(id)
       stuinfo.set__name(names)
       l=stuinfo.inp()
       student.append(l)
    else :
      student.append(names) 
      break 


def Courseinfo():
  print("Enter 0 for COURSE NAME if you want to stop inputting\n")
  while(1):
    names=input("Enter COURSE NAME:")
    if names != name0:
       id=input("Enter course id:")
       cre=input("Enter course number of credit")
       numcredit.append(cre)
       cour=CourseInfo()
       cour.set__ID(id)
       cour.set__name(names)
       cour.set__credit(cre)
       l=cour.inp()
       course.append(l)
    else :
      course.append(names) 
      break 
  sumcredit=np.sum(numcredit) 

  
def inStudentmark():
  print("Enter 0 for COURSE NAME if you want to stop inputting\n")
  while(1):
    n=input("ENTER STUDENT NAME:")
    if n != name0:
      l=[]
      stumark[n]=l
      for i in range(len(course)):
        m=input("{n} mark for {course[i]} is:")
        l.append(m)
      else:
        break  
