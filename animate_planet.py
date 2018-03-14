import matplotlib
matplotlib.use("Cairo")
import matplotlib.pyplot as plt
import numpy as np

from draw_orbs import draw_star, draw_planet

def animate_planet(star_radius=10,planet_radius=1,orbit_radius=20,
                   frames_per_orbit=360,nframes=20,view_angle=90,
                   filebase="planet",star_color="r",planet_color="c",
                   bkgd_color="w"):



    phi_orbit = np.linspace(0,2*np.pi,frames_per_orbit)

    for i in range(nframes):
        fig = plt.figure(figsize=(9,9))
        ax = fig.add_subplot(111,projection='3d')
        ax.view_init(view_angle,0)
        ax.set_facecolor(bkgd_color)

        lim = orbit_radius + 1
        ax.set_xlim(-1*lim,lim)
        ax.set_ylim(-1*lim,lim)
        ax.set_zlim(-1*lim,lim)

        draw_star(ax=ax,star_radius=star_radius,star_color=star_color)
        draw_planet(ax=ax,planet_radius=planet_radius,orbit_radius=orbit_radius,
                    orbit_phi=phi_orbit[i],planet_color=planet_color)
        plt.savefig("{0}_{1:0>3}.png".format(filebase,i+1),dpi=600,
                    bbox_inches="tight")

        plt.close("all")

        print("done frame",i+1)




if __name__=="__main__":
    # animate_planet(nframes=2,planet_color="k",orbit_radius=100,
    #                bkgd_color="k",view_angle=1)
    # print("done first)")
    #
    # print ("going to second")
    animate_planet(nframes=4,frames_per_orbit=8,planet_color="k",
                   orbit_radius=100,
                   bkgd_color="lightgrey",view_angle=90,filebase="overhead")
