#!/usr/bin/python3
from statemachine import IdleState, StandbyState, CruiseState, EmergencyState
import sys
import time
import FaBo9Axis_MPU9250
import Adafruit_BMP.BMP085 as BMP085

class airplane:
    def __init__(self):
        self.state = IdleState()
    
    def on_event(self, event):
        self.state = self.state.on_event(event)
        self.state.run
    

    
    
if __name__ == "__main__":
    drone = airplane()
    time.sleep(1)
    drone.on_event('EngOnBtn')
    print(str(drone.state))
    
    time.sleep(1)
    drone.on_event('Cruise')
    print(drone.state)
    
    time.sleep(1)
    drone.on_event('Lost')
    print(drone.state)
    
    time.sleep(1)
    drone.on_event('Signal')
    print(drone.state)
    