#!/usr/bin/python

import sys
import time

from motor_lib import motor_lib
from motor_globals import motor_globals
    
def main():

    pv = str(sys.argv[1])

    print "Test move sequence on motor " + pv
    
    lib = motor_lib()
    g = motor_globals()
    
    positions = range(10)
    
    for pos in positions:
        print "Move to " + str(pos)
        stat = lib.move(pv, pos, g.TIMEOUT)
        if (stat == g.FAIL):
            sys.exit(lib.testComplete(g.FAIL))

    sys.exit(lib.testComplete(g.SUCCESS))
   

if __name__ == "__main__":
        main()
