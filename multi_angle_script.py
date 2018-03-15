from animate_planet import animate_planet

if __name__=="__main__":

    # Inputs
    star_radius = 10
    planet_radius = 1
    orbit_radius = 100
    frames_per_orbit = 60
    nframes = 60
    background1 = "LightGrey"
    background2 = "k"
    star_color="#ffcc00"
    planet_color="k"

    # overhead view
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,star_color=star_color,
                   planet_color=planet_color,bkgd_color=background1,
                   view_angle=90,filebase="planet_90_overhead_grey")
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,star_color=star_color,
                   planet_color=planet_color,bkgd_color=background2,
                   view_angle=90,filebase="planet_90_overhead_black")

    # side-on view
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,star_color=star_color,
                   planet_color=planet_color,bkgd_color=background1,
                   view_angle=0,filebase="planet_0_edgeon_grey")
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,star_color=star_color,
                   planet_color=planet_color,bkgd_color=background2,
                   view_angle=0,filebase="planet_0_edgeon_black")

    # slightly off edge
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,star_color=star_color,
                   planet_color=planet_color,bkgd_color=background1,
                   view_angle=2,filebase="planet_2_offedge_grey")
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,star_color=star_color,
                   planet_color=planet_color,bkgd_color=background2,
                   view_angle=2,filebase="planet_2_offedge_black")

    # slightly more off edge
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,star_color=star_color,
                   planet_color=planet_color,bkgd_color=background1,
                   view_angle=5,filebase="planet_5_offedge_grey")
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,star_color=star_color,
                   planet_color=planet_color,bkgd_color=background2,
                   view_angle=5,filebase="planet_5_offedge_black")

    # off edge
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,star_color=star_color,
                   planet_color=planet_color,bkgd_color=background1,
                   view_angle=30,filebase="planet_30_offedge_grey")
    animate_planet(star_radius=star_radius,planet_radius=planet_radius,
                   orbit_radius=orbit_radius,frames_per_orbit=frames_per_orbit,
                   nframes=nframes,star_color=star_color,
                   planet_color=planet_color,bkgd_color=background2,
                   view_angle=30,filebase="planet_30_offedge_black")
