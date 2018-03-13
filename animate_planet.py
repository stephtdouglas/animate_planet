import matplotlib
matplotlib.use("Cairo")
import matplotlib.pyplot as plt
import numpy as np

from draw_orbs import draw_star, draw_planet

def animate_planet(star_radius=10,planet_radius=1,orbit_radius=20,
                   frames_per_orbit=20,nframes=20,filebase="planet"):



    phi_orbit = np.linspace(0,2*np.pi,frames_per_orbit)

    for i in range(nframes):
        fig = plt.figure(figsize=(9,9))
        ax = fig.add_subplot(111,projection='3d')

        lim = planet_radius + orbit_radius + 1
        ax.set_xlim(-1*lim,lim)
        ax.set_ylim(-1*lim,lim)
        ax.set_zlim(-1*lim,lim)

        draw_star(ax=ax,star_radius=star_radius)
        draw_planet(ax=ax,planet_radius=planet_radius,orbit_radius=orbit_radius,
                    orbit_phi=phi_orbit[i])
        plt.savefig("{0}_{1:0>3}.png".format(filebase,i+1))

        plt.close("all")


if __name__=="__main__":
    animate_planet(nframes=5)
