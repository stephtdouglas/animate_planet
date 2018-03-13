from animate_planet import animate_planet

if __name__=="__main__":

    # Inputs
    star_radius = 10
    planet_radius = 1
    orbit_radius = 45
    frames_per_orbit = 50
    nframes = 50

    # overhead view
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,
                   view_angle=90,filebase="planet_90_overhead")

    # side-on view
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,
                   view_angle=90,filebase="planet_0_edgeon")
