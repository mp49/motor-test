#!/usr/bin/python

import sys
import time

from epics import caput, caget

from motor_lib import motor_lib
from motor_globals import motor_globals
    
def main():

    pv = str(sys.argv[1])

    print "Test reversing a move in progress on motor " + pv
    
    lib = motor_lib()
    g = motor_globals()
    
    moves = range(0,1000)
    
    ntm = pv + ".NTM"
    caput(ntm, 1, wait=True)

    for move in moves:
        
        print "Test " + str(move) 

        position = 100
        print "Moving to " + str(position)
        caput(pv, position, wait=False)

        time.sleep(15)
        
        #Check we are still moving
        pos1 = caget(pv + ".RBV")
        time.sleep(2)
        pos2 = caget(pv + ".RBV")
        if (pos1 == pos2):
            print "ERROR: RBV is not changing!"
            print "pos1: " + str(pos1)
            print "pos2: " + str(pos2)
            sys.exit(lib.testComplete(g.FAIL))

        position = -100
        print "Moving to " + str(position)
        caput(pv, position, wait=False)

        time.sleep(15)
        #Check we are still moving
        pos1 = caget(pv + ".RBV")
        time.sleep(2)
        pos2 = caget(pv + ".RBV")
        if (pos1 == pos2):
            print "ERROR: RBV is not changing!"
            print "pos1: " + str(pos1)
            print "pos2: " + str(pos2)
            sys.exit(lib.testComplete(g.FAIL))
        
    caput(ntm, 0, wait=True)

    sys.exit(lib.testComplete(g.SUCCESS))
   

if __name__ == "__main__":
        main()
