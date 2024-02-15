import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

coeff_poisson = 0.3

def draw_cuboid_fixe_little(ax, l, c):
    # Vertices of the cuboid
    vertices = np.array([[0-c/2, -l/2, -l/2],
                         [0-c/2, l-l/2, -l/2],
                         [c-c/2, l-l/2, -l/2],
                         [c-c/2, -l/2, -l/2],
                         [0-c/2, -l/2, l-l/2],
                         [0-c/2, l-l/2, l-l/2],
                         [c-c/2, l-l/2, l-l/2],
                         [c-c/2, -l/2, l-l/2]])
    
    # Edges of the cuboid
    edges = [[0, 1], [1, 2], [2, 3], [3, 0],
             [4, 5], [5, 6], [6, 7], [7, 4],
             [0, 4], [1, 5], [2, 6], [3, 7]]
    
    for edge in edges:
        ax.plot3D(*zip(*vertices[edge]), color='b')

def draw_cuboid_fixe_big(ax, l, c):
    # Vertices of the cuboid
    vertices = np.array([[0-c/2, -l/2, -l/2],
                         [0-c/2, l-l/2, -l/2],
                         [c-c/2, l-l/2, -l/2],
                         [c-c/2, -l/2, -l/2],
                         [0-c/2, -l/2, l-l/2],
                         [0-c/2, l-l/2, l-l/2],
                         [c-c/2, l-l/2, l-l/2],
                         [c-c/2, -l/2, l-l/2]])
    
    # Edges of the cuboid
    edges = [[0, 1], [1, 2], [2, 3], [3, 0],
             [4, 5], [5, 6], [6, 7], [7, 4],
             [0, 4], [1, 5], [2, 6], [3, 7]]
    
    for edge in edges:
        ax.plot3D(*zip(*vertices[edge]), color='r')

    

def draw_cuboid(ax, l, c, t):
    # Vertices of the cuboid
    vertices = np.array([[0-c/2, -l/2, -l/2],
                         [0-c/2, l-l/2, -l/2],
                         [c-c/2, l-l/2, -l/2],
                         [c-c/2, -l/2, -l/2],
                         [0-c/2, -l/2, l-l/2],
                         [0-c/2, l-l/2, l-l/2],
                         [c-c/2, l-l/2, l-l/2],
                         [c-c/2, -l/2, l-l/2]])
    
    # Edges of the cuboid
    edges = [[0, 1], [1, 2], [2, 3], [3, 0],
             [4, 5], [5, 6], [6, 7], [7, 4],
             [0, 4], [1, 5], [2, 6], [3, 7]]
    
    for edge in edges:
        ax.plot3D(*zip(*vertices[edge]), color='black', linewidth=2)  # Adjust linewidth for edge thickness
    
    # Define the faces of the cuboid
    faces = [[vertices[0], vertices[1], vertices[2], vertices[3]],
             [vertices[4], vertices[5], vertices[6], vertices[7]],
             [vertices[0], vertices[1], vertices[5], vertices[4]],
             [vertices[2], vertices[3], vertices[7], vertices[6]],
             [vertices[1], vertices[2], vertices[6], vertices[5]],
             [vertices[0], vertices[3], vertices[7], vertices[4]]]
    
    # Interpolate color from blue to red based on time
    color = interpolate_color(t)
    
    for face in faces:
        x, y, z = zip(*face)
        verts = [list(zip(x,y,z))]
        #ax.add_collection3d(Poly3DCollection(verts, facecolors=color, edgecolors='k'))  # Adjust edgecolors for edge color
        ax.plot_surface(np.array(x).reshape((2, 2)), np.array(y).reshape((2, 2)), np.array(z).reshape((2, 2)), alpha=0.5)


def interpolate_color(t):
    # Interpolate color from blue (0, 0, 1) to red (1, 0, 0) based on time
    blue = np.array([0, 0, 1])
    red = np.array([1, 0, 0])
    color = blue + (red - blue) * np.sin(t / 10)  # Adjust the range if needed
    color = np.clip(color, 0, 1)  # Clip values to ensure they are within the valid range
    return tuple(color)

def update(frame, ax):
    ax.clear()
    t = frame  # Time values
    c = 5 + np.sin(t/10+np.pi) #  # Side length of the cube (static)
    l = 5 + coeff_poisson * np.sin(t/10)  # Length of the cuboid
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    #cube max traction
    #draw_cuboid_fixe_little(ax, 5 - 0.8, 6)
    #cube max pressions
    #draw_cuboid_fixe_big(ax, 5 + 0.8, 4)
    draw_cuboid(ax, l, c, t)
    
    # Add text
    ax.text(-4, 4, 4, f"(l_max-dl)/(dc-c_max)=(5-{round(l,2)})/({round(c,2)}-5)="+str(round((5-l)/(c-5),2)), color='red')
    
    # Fixing the size of the axes
    ax.set_xlim([-4, 4])
    ax.set_ylim([-4, 4])
    ax.set_zlim([-4, 4])

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ani = FuncAnimation(fig, update, fargs=(ax,), frames=np.arange(0, 100, 1), interval=50)
    #ani.save('animation_centered.gif', writer='imagemagick', fps=20)

    plt.show()


if __name__ == "__main__":
    main()
