import sys
import signal
from random import random,choice
from math import floor
from time import sleep
from subprocess import call

def cleanup():
    call( [ "/etc/init.d/rainbow", "restart" ])

# odchyt signalu interrupt
def trap_sigint( signal, frame ):
    sys.stderr.write( "Chycen SIGINT, uklizim a koncim.\n")
    uklid()
    sys.exit(0)

#signal.signal( signal.SIGINT, trap_sigint )


usage = """USAGE:
    %s
""" % sys.argv[0]

# list of Turris leds
leds = [ 'wan', 'lan1', 'lan2', 'lan3', 'lan4', 'lan5', 'wifi', 'pwr' ]

# seznam barev, ktere ma stridat
colors = [
            "00FF00",
            "0000AA",
            "FF6600",
            "FF0000",
            "009900"
         ]

if ( len(sys.argv) < 1 ):
    sys.stderr.write(usage)
    exit(1)

call([ "rainbow", "all", "disable" ])
call([ "rainbow", "all", "red" ])


for idx, i in enumerate(leds):
    ranval = random()
    print(ranval)
    if ranval >= 0.4:
        #print("rainbow", i, "enable")
        call(["rainbow", i, "enable"])
        sleep(1 + (0.3 * idx))
    else:
        #call(["rainbow", "all", "disable"])
        for i in range(5):
            call(["rainbow", "all", choice(colors)])
            sleep(0.25)
        call(["rainbow", "all", "red"])
        sys.exit()
for i in range(25):
    call(["rainbow", "all", choice(colors)])
    sleep(0.15)
call(["rainbow", "all", "disable"])
#cleanup()
