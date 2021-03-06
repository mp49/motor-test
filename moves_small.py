#!/usr/bin/python

import sys
import time

from motor_lib import motor_lib
from motor_globals import motor_globals
    
def main():

    pv = str(sys.argv[1])

    print "Test small move sequence on motor " + pv
    
    lib = motor_lib()
    g = motor_globals()
    
    positions = range(0,100)
    
    for pos in positions:
        pos = float(pos)/100.0
        print "Move to " + str(pos)
        stat = lib.move(pv, pos, g.TIMEOUT)
        if (stat == g.FAIL):
            sys.exit(lib.testComplete(g.FAIL))

    positions = range(0,100)
    for pos in positions:
        pos = float(pos)/1000
        print "Move to " + str(pos)
        stat = lib.move(pv, pos, g.TIMEOUT)
        if (stat == g.FAIL):
            sys.exit(lib.testComplete(g.FAIL))

    sys.exit(lib.testComplete(g.SUCCESS))
   

if __name__ == "__main__":
        main()
