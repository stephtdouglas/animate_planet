import matplotlib
matplotlib.use("Cairo")
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def draw_star(star_color="Red",star_radius=10,
             ax=None):

    if ax is None:
        fig = plt.figure(figsize=(9,9))
        ax = fig.add_subplot(111,projection='3d')

    phi = np.linspace(0,2*np.pi,256)
    theta = np.linspace(0,np.pi,128)

    r = star_radius

    x = r*np.outer(np.cos(phi),np.sin(theta))
    y = r*np.outer(np.sin(phi),np.sin(theta))
    z = r*np.outer(np.ones(np.size(phi)),np.cos(theta))


    ax.plot_surface(x,y,z,color=star_color,
                    rstride=1,cstride=1)

    ax._axis3don = False

def draw_planet(planet_color="c",planet_radius=1,
                orbit_radius=20,orbit_phi=np.pi/4,
                ax=None):

    if ax is None:
        fig = plt.figure(figsize=(9,9))
        ax = fig.add_subplot(111,projection='3d')

    phi = np.linspace(0,2*np.pi,256)
    theta = np.linspace(0,np.pi,128)

    r = planet_radius

    s = orbit_radius 
    orbit_x = s*np.cos(orbit_phi)
    orbit_y = s*np.sin(orbit_phi)

    x = r*np.outer(np.cos(phi),np.sin(theta)) + orbit_x
    y = r*np.outer(np.sin(phi),np.sin(theta)) + orbit_y
    z = r*np.outer(np.ones(np.size(phi)),np.cos(theta))

    ax.plot_surface(x,y,z,color=planet_color,
                   rstride=1,cstride=1)


if __name__=="__main__":

    fig = plt.figure(figsize=(9,9))
    ax = fig.add_subplot(111,projection='3d')
    draw_star(ax=ax)
    draw_planet(ax=ax)

    ax.set_xlim(-16,16)
    ax.set_ylim(-16,16)
    ax.set_zlim(-16,16)

    plt.savefig("demo_planet.png")
    plt.close()
