import matplotlib.pyplot as plot
import numpy as np 

i=0
h=[]
p=[]
while(i<=700):
    h.append(i)
    i+=25
i=0
while(i<=100):
    while(i<=10):
        while(i<=1):
            p.append(i)
            i+=0.1
        p.append(i)
        i+=1
    p.append(i)
    i+=10
print(p)
print(len(h),len(p))
    

# Display grid
plot.grid(True, which="both") 

# Linear X axis, Logarithmic Y axis
plot.semilogy(h, p )
#plot.ylim([10,21000])
#plot.xlim([1900,2020]) 

# Provide the title for the semilog plot
plot.title('Y axis in Semilog using Python Matplotlib') 

# Give x axis label for the semilog plot
plot.xlabel('Year')

# Give y axis label for the semilog plot
plot.ylabel('Stock market index') 

# Display the semilog plot
plot.show()
