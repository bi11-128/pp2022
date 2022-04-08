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
def Studentlist():
  i=0
  print("THE STUDENTS LIST :")
  while(1):
    if student[i] != name0:
      print(student[i])
      i=i+1
    else:
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
