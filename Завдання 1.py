from cProfile import label

import matplotlib.pyplot as p
import numpy as n

x=n.linspace(0,4,51)
y=5*n.sin(10*x)*n.sin(3*x)
p.plot(x,y,label='5*sin(10*x)*sin(3*x)',color="blue",linewidth=4)
p.title('My plot',fontsize=15)
p.xlabel('x',fontsize=10,color='red')
p.ylabel('y',fontsize=10,color='red')
p.legend()
p.grid(True)
p.show()