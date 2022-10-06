import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-np.pi,np.pi,0.01)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel('x values from -pi to pi')
plt.ylabel('sin(x)')
plt.title('Plot of sin(x)')
plt.legend(['sin(x)'])
plt.grid(axis='both', color='0.95')
plt.show()

