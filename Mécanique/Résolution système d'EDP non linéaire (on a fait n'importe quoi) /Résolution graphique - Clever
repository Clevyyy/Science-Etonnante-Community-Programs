import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint

g = 9.81
k = 1000
m = 1
l0 = 0.2
 
def edp(X,t):
    dt=np.array([X[1],
                 X[3]**2*X[0]+g*np.cos(X[2])-k/m*(X[0]-l0),
                 X[3],
                 (-g*np.sin(X[2])-2*X[1]*X[3])/X[0]])
    return dt
 
n = 500
t = np.linspace(0, 5, n)
 
x0 = l0 + 0.1
v0 = 0
theta0 = np.pi/4
dtheta0 = 100
 
X0 = np.array([x0, v0, theta0, dtheta0])
 
res = odeint(edp, X0, t)
 
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
 
# Matrice des graphiques
axs[0, 0].set_position([0.1, 0.55, 0.35, 0.35]) 
axs[0, 1].set_position([0.55, 0.55, 0.35, 0.35])
axs[1, 0].set_position([0.1, 0.1, 0.35, 0.35])
axs[1, 1].axis('off')
 
axs[0, 0].set_xlim(-l0 - 0.5, l0 + 0.5)
axs[0, 0].set_ylim(-l0 - 0.5, 0.5)
axs[0, 0].set_xlabel('Position en x')
axs[0, 0].set_ylabel('Position en y')
 
axs[0, 1].set_xlim(5, 0)
axs[0, 1].set_ylim(-l0 - 0.5, 0.5)
axs[0, 1].set_xlabel('Temps (s)')
axs[0, 1].set_ylabel('Position en y')
 
axs[1, 0].set_xlim(-l0 - 0.5, l0 + 0.5)
axs[1, 0].set_ylim(0, 5)
axs[1, 0].set_xlabel('Position en x')
axs[1, 0].set_ylabel('Temps (s)')
 
line, = axs[0, 0].plot([], [], 'b-')
dot, = axs[0, 0].plot([], [], 'ro')
trail, = axs[0, 0].plot([], [], 'g-', linewidth=0.5)
 
line2, = axs[0, 1].plot([], [], 'b-')
line3, = axs[1, 0].plot([], [], 'b-')
segment_yytrace, = axs[0, 1].plot([], [], linestyle='--',color='black')
segment_xxtrace, = axs[1, 0].plot([], [], linestyle='--',color='black')
 
segment_ytrace, = axs[0, 0].plot([], [], linestyle='--',color='black')
segment_xtrace, = axs[0, 0].plot([], [], linestyle='--',color='black')
 
 
def update(frame):
    a = np.sin(res[frame, 2])
    b = -np.cos(res[frame, 2])
 
    line.set_data([a * (l0 + res[frame, 0]), 0], [b * (l0 + res[frame, 0]), 0])
    dot.set_data(a * (l0 + res[frame, 0]), b * (l0 + res[frame, 0]))
    trail.set_data(np.sin(res[:frame, 2]) * (l0 + res[:frame, 0]), -np.cos(res[:frame, 2]) * (l0 + res[:frame, 0]))
    line2.set_data(t[:frame], -np.cos(res[:frame, 2]) * (l0 + res[:frame, 0]))
    line3.set_data(np.sin(res[:frame, 2]) * (l0 + res[:frame, 0]), t[:frame])  # Courbe pour le graphique en dessous
 
    segment_y = -np.cos(res[frame, 2]) * (l0 + res[frame, 0])
    segment_yytrace.set_data([t[frame],5], [segment_y, segment_y])
 
    segment_x = np.sin(res[frame, 2]) * (l0 + res[frame, 0])
    segment_xxtrace.set_data([segment_x, segment_x], [5, t[frame]])
 
    segment_x = np.sin(res[frame, 2]) * (l0 + res[frame, 0])
    segment_y = -np.cos(res[frame, 2]) * (l0 + res[frame, 0])
    segment_ytrace.set_data([segment_x,segment_x], [-0.8, segment_y])
    segment_xtrace.set_data([0.8, segment_x], [segment_y,segment_y])
 
    return line, dot, trail, line2, line3, segment_yytrace,segment_xxtrace,segment_ytrace,segment_xtrace
 
 
#Animation
ani = FuncAnimation(fig, update, frames=n, interval=50, blit=True)
#Sauvegarde
#ani.save('animation.gif', writer='pillow', fps=n)
 
plt.show()
