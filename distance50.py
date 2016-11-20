import math
import matplotlib.pyplot as plt
import numpy as np
import progagation_model

f = 900.0
hb = 50.0
hm = 1.5
scenario = 3

d_end = 200
n = 200
d = np.linspace(1.0, d_end, num= n)
d_extender_position = 16.0
d_extender = np.linspace(d_extender_position + 1.0, d_end, num= n)

plot_power = 33.0
plot_power_extender = 23.0

receive_power = np.zeros(n)

gain = 17.0

for i in range(0, n):
    receive_power[i] = plot_power + gain - progagation_model.okumura_model_path_loss(d[i], f, hb, hm, scenario)

for i in range(0, n):
    receive_power[i] = plot_power_extender + gain - progagation_model.okumura_model_path_loss(d_extender[i]- d_extender_position, f, hb, hm, scenario)


x = d
y = receive_power

tt = "Site Height :" + str(hb) + " \n" + "Scenario:" + str(scenario)

plt.plot(x, y, label =tt,  linewidth = 2)
x = d_extender
plt.plot(x, y, color = "red", linewidth = 2)

plt.xlim(0, 100)
plt.ylim(-105, -50)
plt.grid()
plt.legend()
plt.savefig("distance.png" ,dpi = 200)


