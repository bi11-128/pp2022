# nhập vào số tín chỉ của từng môn
# tính tổng số điểm của từng môn học
# tính GPA 
import curses 
from curses import wrapper
import numpy as np
import math as mat
import time


student=[]
course=[]
numcredit=[]
stumark={}
name0=str(0)
sumcredit=0
sortGPA={}
class CourseInfo:
  def __init__(self):
    self.__name=0
    self.__ID=0
    self.__credit=0
  def get__name(self):
    return self.__name
  def set__name(self,t):
    self.__name=t
  def get__ID(self):
    return self.__ID
  def set__ID(self,i):
    self.__ID=i  
  def get__credit(self):
    return self.__credit  
  def set__credit(self,c):
    self.__credit=c  
  def inp(self):
    return f"Name:{self.__name}|ID:{self.__ID}|Credit:{self.__credit}"
class StudentMark(CourseInfo):             
  def __init__(self,s,m):
    CourseInfo.__init__(self)
    self.subj=s
    self.mark=m
  def inp(self):
    super().inp()
    return f"Name:{self.get__name()}|ID:{self.get__ID()}|Mark on {self.subj}:{self.mark}"
class StudentInfo(CourseInfo):
  def __init__(self,doB):
    CourseInfo.__init__(self)
    self.DOB=doB
  def inp(self):
    super().inp()
    return f"Name:{self.get__name()}|ID:{self.get__ID()}|doB:{self.DOB}"


#input number of students in a class
def numcourse():
    ns=input("Enter number of students in a class:") 


#input number of courses
def numstudent():
    nc=input("Enter number of students:") 


#Input student information: id, name, DoB   
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


#List students
def Studentlist():
  i=0
  print("THE STUDENTS LIST :")
  while(1):
    if student[i] != name0:
      print(student[i])
      i=i+1
    else:
      break

#Input course information: id, name  
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

# List courses
def Courselist():
  i=0
  print("THE COURSE LIST :")
  while(1):
    if course[i] != name0:
      print(course[i])
      i=i+1
    else:
      break  


#Select a course, input marks for student in this course   
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

#Show student marks for a given course
def ListStudentmark():
  s = input("Input the subject:")
  if s in stumark:
    print(f"LIST OF  STUDENT's {s} MARK:")
    for i in range(len(stumark[s])):
      print(stumark[s][i]) 
  else:
      print("Subject not found,please use Studentmark() to add new course")



def GPAcount(n):
  print("Enter 0 for STUDENT NAME TO END TO LOOP")
  while(1):  
   n=input("Enter STUDENT NAME:")
   if n!=name0:
    if n in stumark:
     t=np.multiply(stumark[n],numcredit)
     m=sumcredit
     GPA=round(t/m,2)
     return GPA
    else:
     print("NO student name {n},Please Enter STUDENT NAME again")
   else:
     break  



def sortStudentList():
  for n in stumark:
    aGPA=GPAcount(n)
    sortGPA[n]=aGPA
  finalsortGPA=sorted(sortGPA.items(),key=lambda x:x[1],reverse=True)
  for i in range(finalsortGPA):
    print(finalsortGPA[i])


##Studentinfo()
#Studentlist()
#Courseinfo()
#Courselist()
inStudentmark()
ListStudentmark()

def main(stdscr):
  stdscr.addstr("Input a student name")
  key=stdscr.getstr(0,0,4)
  GPAm=GPAcount(key)
  stdscr.addstr(f"key's GPA:{GPAm}")
  stdscr.refresh()
  stdscr.getch()

wrapper(main)


