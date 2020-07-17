from matplotlib import pyplot
import math

i=0.1
while (i<=1):
    #a=[math.log(i)]
    a=[i]
    i+=0.1
#a = [ pow(10,i) for i in range(10) ]

pyplot.subplot(2,1,1)
pyplot.plot(a, color='blue', lw=2)
pyplot.yscale('log')
pyplot.show()
