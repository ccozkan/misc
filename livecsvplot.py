import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib import style

style.use('dark_background')
#style.use('bmh')

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)


def animate(i):
	xs, ys = np.loadtxt('dnm.csv', delimiter=';', unpack=True,skiprows=1,usecols=(0, 2) )
	ax1.clear()
	ax2.clear()
	
	x2, y2 =xs[-9:],ys[-9:]
	ax1.grid()
	ax1.plot(xs,ys)
	
	ax2.plot(x2,y2)
	ax2.grid()
	print('heallloo')
	

ani = animation.FuncAnimation(fig, animate, interval= 100)

plt.show()
