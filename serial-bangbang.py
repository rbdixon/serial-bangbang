#!/usr/bin/env python2

"""
Launches picocom and drops into interactive mode so that you can configure the serial interface. Control-] starts
a loop that sends repeated newlines to stimulate the serial port. Probe around until you find the serial input.
Any output from the device will be printed with a beep to help you to know you've found it. Control-C gets you
back into interactive mode. To exit the script exit picocom while in interactive mode.
"""

import sys
import pexpect
from pexpect.exceptions import *

def beep():
    print('\a')

term = pexpect.spawn("picocom /dev/tty.usbserial-A9048JDJ")

while True:
    print("\n--\nIn interactive mode. Control-] to start return loop. Exit picocom to kill loop.\n--\n")
    term.interact()
    beep()

    print("\n--\nStarting return loop. Control-C to break\n--\n")
    try:
        while True:
            try:
                term.write("\n")
                t = term.read_nonblocking(size=1024, timeout=0.5)
                if len(t) > 0:
                    print(t)
                    beep()
            except (EOF, TIMEOUT):
                pass

    except KeyboardInterrupt:
        pass
    except OSError:
        print("\n--\nExiting.\n--\n")
        sys.exit()
