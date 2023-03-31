import eyes17.eyes          # uncomment these two lines while running stand-alone
p = eyes17.eyes.open()

p.set_pv1(5)

from pylab import *


time = 2 # seconds
dt = 1000 # micro seconds

x,y = p.capture1('A1',int(time*1000000/dt),int(dt))

plot(x,y)
show()
