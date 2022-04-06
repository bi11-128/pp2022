import scipy
import scipy.signal as sig
import matplotlib.pyplot as plot
import numpy as np 
from math import pi
from scipy import signal
##def f(x):
#return (1/(np.pi*x))*np.sin(np.pi*x/3)*((-1)^(2*x))

#x = np.linspace(-320, 320, 641)
#y=f(x)

#Y=[]
#for i in range(0,10):
#  if i!=0:
#   z=pow(-0.05,i)
#   Y.append(z)  
#freY=np.abs(np.fft.fft(Y)) 
#plot.plot(freY)
#plot.show()
ECG =np.array([
    0, 0.0010593, 0.0021186, 0.003178, 0.0042373, 0.0052966, 0.0063559,
    0.0074153, 0.0084746, 0.045198, 0.081921, 0.11864, 0.15537, 0.19209,
    0.22881, 0.26554, 0.30226, 0.33898, 0.30226, 0.26554, 0.22881, 0.19209,
    0.15537, 0.11864, 0.081921, 0.045198, 0.0084746, 0.0077684, 0.0070621,
    0.0063559, 0.0056497, 0.0049435, 0.0042373, 0.0035311, 0.0028249,
    0.0021186, 0.0014124, 0.00070621, 0, -0.096045, -0.19209, -0.28814,
    -0.073446, 0.14124, 0.35593, 0.57062, 0.78531, 1, 0.73729, 0.47458,
    0.21186, -0.050847, -0.31356, -0.57627, -0.83898, -0.55932, -0.27966, 0,
    0.00073692, 0.0014738, 0.0022108, 0.0029477, 0.0036846, 0.0044215,
    0.0051584, 0.0058954, 0.0066323, 0.0073692, 0.0081061, 0.008843, 0.00958,
    0.010317, 0.011054, 0.011791, 0.012528, 0.013265, 0.014001, 0.014738,
    0.015475, 0.016212, 0.016949, 0.03484, 0.052731, 0.070621, 0.088512,
    0.1064, 0.12429, 0.14218, 0.16008, 0.17797, 0.16186, 0.14576, 0.12966,
    0.11356, 0.097458, 0.081356, 0.065254, 0.049153, 0.033051, 0.016949,
    0.013559, 0.010169, 0.0067797, 0.0033898, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0010593, 0.0021186, 0.003178,
    0.0042373, 0.0052966, 0.0063559, 0.0074153, 0.0084746, 0.045198, 0.081921,
    0.11864, 0.15537, 0.19209, 0.22881, 0.26554, 0.30226, 0.33898, 0.30226,
    0.26554, 0.22881, 0.19209, 0.15537, 0.11864, 0.081921, 0.045198, 0.0084746,
    0.0077684, 0.0070621, 0.0063559, 0.0056497, 0.0049435, 0.0042373,
    0.0035311, 0.0028249, 0.0021186, 0.0014124, 0.00070621, 0, -0.096045,
    -0.19209, -0.28814, -0.073446, 0.14124, 0.35593, 0.57062, 0.78531, 1,
    0.73729, 0.47458, 0.21186, -0.050847, -0.31356, -0.57627, -0.83898,
    -0.55932, -0.27966, 0, 0.00073692, 0.0014738, 0.0022108, 0.0029477,
    0.0036846, 0.0044215, 0.0051584, 0.0058954, 0.0066323, 0.0073692,
    0.0081061, 0.008843, 0.00958, 0.010317, 0.011054, 0.011791, 0.012528,
    0.013265, 0.014001, 0.014738, 0.015475, 0.016212, 0.016949, 0.03484,
    0.052731, 0.070621, 0.088512, 0.1064, 0.12429, 0.14218, 0.16008, 0.17797,
    0.16186, 0.14576, 0.12966, 0.11356, 0.097458, 0.081356, 0.065254, 0.049153,
    0.033051, 0.016949, 0.013559, 0.010169, 0.0067797, 0.0033898, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0010593,
    0.0021186, 0.003178, 0.0042373, 0.0052966, 0.0063559, 0.0074153, 0.0084746,
    0.045198, 0.081921, 0.11864, 0.15537, 0.19209, 0.22881, 0.26554, 0.30226,
    0.33898, 0.30226, 0.26554, 0.22881, 0.19209, 0.15537, 0.11864, 0.081921,
    0.045198, 0.0084746, 0.0077684, 0.0070621, 0.0063559, 0.0056497, 0.0049435,
    0.0042373, 0.0035311, 0.0028249, 0.0021186, 0.0014124, 0.00070621, 0,
    -0.096045, -0.19209, -0.28814, -0.073446, 0.14124, 0.35593, 0.57062,
    0.78531, 1, 0.73729, 0.47458, 0.21186, -0.050847, -0.31356, -0.57627,
    -0.83898, -0.55932, -0.27966, 0, 0.00073692, 0.0014738, 0.0022108,
    0.0029477, 0.0036846, 0.0044215, 0.0051584, 0.0058954, 0.0066323,
    0.0073692, 0.0081061, 0.008843, 0.00958, 0.010317, 0.011054, 0.011791,
    0.012528, 0.013265, 0.014001, 0.014738, 0.015475, 0.016212, 0.016949,
    0.03484, 0.052731, 0.070621, 0.088512, 0.1064, 0.12429, 0.14218, 0.16008,
    0.17797, 0.16186, 0.14576, 0.12966, 0.11356, 0.097458, 0.081356, 0.065254,
    0.049153, 0.033051, 0.016949, 0.013559, 0.010169, 0.0067797, 0.0033898, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0.0010593, 0.0021186, 0.003178, 0.0042373, 0.0052966, 0.0063559, 0.0074153,
    0.0084746, 0.045198, 0.081921, 0.11864, 0.15537, 0.19209, 0.22881, 0.26554,
    0.30226, 0.33898, 0.30226, 0.26554, 0.22881, 0.19209, 0.15537, 0.11864,
    0.081921, 0.045198, 0.0084746, 0.0077684, 0.0070621, 0.0063559, 0.0056497,
    0.0049435, 0.0042373, 0.0035311, 0.0028249, 0.0021186, 0.0014124,
    0.00070621, 0, -0.096045, -0.19209, -0.28814, -0.073446, 0.14124, 0.35593,
    0.57062, 0.78531, 1, 0.73729, 0.47458, 0.21186, -0.050847, -0.31356,
    -0.57627, -0.83898, -0.55932, -0.27966, 0, 0.00073692, 0.0014738,
    0.0022108, 0.0029477, 0.0036846, 0.0044215, 0.0051584, 0.0058954,
    0.0066323, 0.0073692, 0.0081061, 0.008843, 0.00958, 0.010317, 0.011054,
    0.011791, 0.012528, 0.013265, 0.014001, 0.014738, 0.015475, 0.016212,
    0.016949, 0.03484, 0.052731, 0.070621, 0.088512, 0.1064, 0.12429, 0.14218,
    0.16008, 0.17797, 0.16186, 0.14576, 0.12966, 0.11356, 0.097458, 0.081356,
    0.065254, 0.049153, 0.033051, 0.016949, 0.013559, 0.010169, 0.0067797,
    0.0033898, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0.0010593, 0.0021186, 0.003178, 0.0042373, 0.0052966,
    0.0063559, 0.0074153, 0.0084746, 0.045198, 0.081921, 0.11864, 0.15537,
    0.19209, 0.22881, 0.26554, 0.30226, 0.33898, 0.30226, 0.26554, 0.22881,
    0.19209, 0.15537, 0.11864, 0.081921, 0.045198, 0.0084746, 0.0077684,
    0.0070621, 0.0063559, 0.0056497, 0.0049435, 0.0042373, 0.0035311,
    0.0028249, 0.0021186, 0.0014124, 0.00070621, 0, -0.096045, -0.19209,
    -0.28814, -0.073446, 0.14124, 0.35593, 0.57062, 0.78531, 1, 0.73729,
    0.47458, 0.21186, -0.050847, -0.31356, -0.57627, -0.83898, -0.55932,
    -0.27966, 0, 0.00073692, 0.0014738, 0.0022108, 0.0029477, 0.0036846,
    0.0044215, 0.0051584, 0.0058954, 0.0066323, 0.0073692, 0.0081061, 0.008843,
    0.00958, 0.010317, 0.011054, 0.011791, 0.012528, 0.013265, 0.014001,
    0.014738, 0.015475, 0.016212, 0.016949, 0.03484, 0.052731, 0.070621,
    0.088512, 0.1064, 0.12429, 0.14218, 0.16008, 0.17797, 0.16186, 0.14576,
    0.12966, 0.11356, 0.097458, 0.081356, 0.065254, 0.049153, 0.033051,
    0.016949, 0.013559, 0.010169, 0.0067797, 0.0033898, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])




def f(x):
   return (1/(np.pi*x))*np.sin(np.pi*x/4)

x = np.linspace(-320, 320, 641)
y=f(x)
y[320]=0.25
chop=[]
blackaddarr=[]
for i in range(641):
  if ((i>=295)and(i<=345)):
    chop.append(1)
  else:
    chop.append(0)
  blackaddarr.append(0.0067)  
chopImp=np.multiply(y,chop)
#--------------  
chop2=[]
for i in range(641):
  if chopImp[i] !=0 :
    chop2.append(chopImp[i])
N=590
Imp=np.pad(chop2,(0,N),'constant')    
freImp=np.abs(np.fft.fft(ECG))
M=1
fullfreECG=np.pad(freImp,(0,M),'constant')
black=np.blackman(641)
BlackmanImp=np.multiply(Imp,black)
freBlackmanImp=np.abs(np.fft.fft(BlackmanImp))
opfreBlackmanImp=np.multiply(-1,freBlackmanImp)
addarr=np.add(opfreBlackmanImp,blackaddarr)
chop3=[]
for i in range(641):
  if ((i>=70)and(i<=571)):
    chop3.append(1)
  else:
    chop3.append(0)  
mul=np.multiply(addarr,chop3)
output=np.multiply(fullfreECG,chop3)
plot.figure(1)
plot.plot(freBlackmanImp)
plot.figure(2)
plot.plot(opfreBlackmanImp)
plot.show()

#np.multiply(fullfreECG,mul)