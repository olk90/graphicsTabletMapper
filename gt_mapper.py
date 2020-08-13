#!/usr/bin/python
from subprocess import run, call, PIPE

# get device ID
xinput = str(run(["xinput"], stdout=PIPE))

# note that it is the Pen, which has to be mapped
search_expression = "Slim Tablet Pen (0)\\tid="
start = xinput.index(search_expression) + len(search_expression)
end = xinput.find("\\t", start)

device_id = xinput[start:end]

# get primary display ID
xrandr = str(run(["xrandr"], stdout=PIPE))

# map the pen to the primary display
search_expression = " connected primary"
lines = xrandr.split("\\n")

display_id = ""
for line in lines:
    if search_expression in line:
        end = line.index(search_expression)
        display_id = line[0:end]
        break

# finally bring all pieces together and execute command
map_to_display = "xinput map-to-output %s %s" % (device_id, display_id)
call(map_to_display, shell=True)
