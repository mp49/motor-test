#!/usr/bin/python

import sys
import time

from motor_lib import motor_lib
from motor_globals import motor_globals
    
def main():
    
    pv = str(sys.argv[1]) 

    print "Set position test on motor " + pv

    lib = motor_lib()
    g = motor_globals()

    positions = [0, 1, 1.234, -1.1, 0]

    for pos in positions:
        print "Set position to " + str(pos)
        stat = lib.setPosition(pv, pos, g.TIMEOUT)
        if (stat == g.FAIL):
            sys.exit(lib.testComplete(g.FAIL))

    sys.exit(lib.testComplete(g.SUCCESS))


if __name__ == "__main__":
    main()
