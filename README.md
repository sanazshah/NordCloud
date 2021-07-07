This repo contains a function that solves the most suitable (with most power) link station for a device at given point [x,y].

This problem is in 2-dimensional space.
Link stations have reach and power.

A link station’s power can be calculated:

      power = (reach - device's distance from linkstation)^2
      if distance > reach, power = 0

Function receives list of link stations and the point where the device is located.

# output #
Function outputs following line:

“Best link station for point x,y is x,y with power z”

or:

“No link station within reach for point x,y”

----------------------------------------

# Running: #

    python -m src.task

-----------------------------
