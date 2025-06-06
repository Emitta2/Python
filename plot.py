# to plot no.s or any data import matplotlib.pyplot library

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])              # to plot different no.s,here it gives a line graph,
                                 # here it takes y values and python automatically generates x values if not given
                                 
plt.show()                       # necessary to show the plot


# to plot a graph with x and y values

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16])  # [1,2,3,4] x values, [1,4,9,16] y values
plt.ylabel("some values")         # to label y axis
plt.show()

# to plot a graph with x and y values and customize the appearance

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'g^') # ro red dots,r-- red dashed line,bs blue squares,g^ green triangles              
plt.ylabel("some values")         
plt.show()

