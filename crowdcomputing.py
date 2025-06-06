#crowd computing
# collective opinion is always better than expert opinion

from statistics import mean

Estimates = [1000,1010,1786,2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
# to calclate trimmed mean
Estimates.sort()
tv=int(0.1*len(Estimates))              # 0.1* len(Estimates) - 10% of 75 values is 7.5, so we take 7
Estimates=Estimates[tv:]                # remove first 10% values i.e. 7 values - smallest 10% values
Estimates=Estimates[:len(Estimates)-tv] # remove last 10% values i.e. 7 values - largest 10% values
print(mean(Estimates))                  # 351.59016393442624

# alternative way to calculate trimmed mean using stats library

from statistics import mean
from scipy import stats

Estimates = [1000,1010,1786,2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
Estimates.sort()
m = stats.trim_mean(Estimates,0.1)
print(m)                                # 351.59016393442624



#to plot croud computing estimates

import matplotlib.pyplot as plt
import statistics
Estimates = [1000,1010,1786,2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
y=[]                                              # keeping constant y values for all estimates
Estimates.sort()
tv=int(0.1*len(Estimates)) 
Estimates=Estimates[tv:]                
Estimates=Estimates[:len(Estimates)-tv] 
for i in range(len(Estimates)):
               y.append(5)                        # appending const y value 5 
plt.plot(Estimates,y,'r--')
plt.plot([statistics.mean(Estimates)],[5],'ro')   # mean
plt.plot([statistics.median(Estimates)],[5],'bs') # median
plt.plot([375],[5],'g^')                          # trimmed mean
plt.show()

#to plot crowd computing estimates (with no x values)

import matplotlib.pyplot as plt
Estimates = [1000,1010,1786,2000,1500,1500,100,120,150,150,150,170,175,180,197,200,200,200,200,200,200,220,220,220,220,234,250,250,250,250,250,250,250,250,250,263,270,275,275,286,300,300,300,300,300,300,300,300,320,350,350,350,400,400,400,400,400,450,467,500,500,500,500,500,500,500,550,550,600,600,600,650,700,700,720]
plt.plot(Estimates)
plt.show()
