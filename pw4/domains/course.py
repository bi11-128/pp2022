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
