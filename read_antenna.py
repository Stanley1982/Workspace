import numpy as np
import matplotlib.pyplot as plt

file_dir = "F:\\01 Workspace\\CPX308R\\"
file_name = "CPX308R_Port 1 +45_02DT_0890.msi"

antenna_vertical = np.zeros((360, 2))
vertical = 0
gain = 0.0

f = open(file_dir + file_name, 'r')
for line in f.readlines():
    line = line.split()
    if line[0] == "GAIN":
        gain = float(line[1]) + 2.15
    elif line[0] == "VERTICAL":
        vertical = 1
        i = 0
        next
        
    elif vertical == 1:
        antenna_vertical[i][0] = float(line[0])
        antenna_vertical[i][1] = gain - float(line[1])
        i += 1

f.close()
for i in range(0, 360):
    print (antenna_vertical[i])
    print ("\n")

x = antenna_vertical[:, 0]
y = antenna_vertical[:, 1]

plt.plot(x, y, label = "Vertical" + file_name )
plt.legend()
plt.show()

