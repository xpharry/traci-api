#!/usr/bin/env python

# @file    runner.py
# @author  Peng Xu
# @date    2019-01-31
# @version 0.0

"""
This script is to command an ego car to move.
"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import subprocess


# the directory in which this script resides
THISDIR = os.path.dirname(__file__)


# we need to import python modules from the $SUMO_HOME/tools directory
# If the the environment variable SUMO_HOME is not set, try to locate the python
# modules relative to this script
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")
import traci  # noqa
import traci.constants as tc
from sumolib import checkBinary  # noqa
import randomTrips  # noqa


def run():
    """execute the TraCI control loop"""

    #subscribing to variables that we want to be printed once the copy has run
    traci.vehicle.subscribe("ego", (tc.VAR_SPEED, tc.VAR_ROAD_ID, tc.VAR_LANE_ID, tc.VAR_LANEPOSITION))
    traci.vehicle.subscribe("car1", (tc.VAR_SPEED, tc.VAR_ROAD_ID, tc.VAR_LANE_ID, tc.VAR_LANEPOSITION))
    traci.vehicle.subscribe("car2", (tc.VAR_SPEED, tc.VAR_ROAD_ID, tc.VAR_LANE_ID, tc.VAR_LANEPOSITION))

    #using traci.movetoXY to position car1 and car2 on network
    traci.vehicle.moveToXY(vehID="ego", edgeID="entry_1", lane=0, x=50, y=0, keepRoute=0)
    traci.vehicle.moveToXY(vehID="car1", edgeID="2_3", lane=0, x=220, y=0, keepRoute=0)
    traci.vehicle.moveToXY(vehID="car2", edgeID="4_3", lane=0, x=350, y=0, keepRoute=0)

    # main loop. do something every simulation step until no more vehicles are
    # loaded or running
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        step += 1

        if "ego" in traci.vehicle.getIDList():
            traci.vehicle.setSpeed("ego", 5.0)
            # print(traci.vehicle.getSubscriptionResults("ego"))
            if step % 10 == 0:
                print(traci.vehicle.getSpeed("ego"), traci.vehicle.getPosition("ego"))

    sys.stdout.flush()
    traci.close()


def get_options():
    """define options for this script and interpret the command line"""
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    # load whether to run with or without GUI
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, '-c', os.path.join('data', 'example.sumocfg')])
    run()
