# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import Pub_pressure
import Pub_pressure_int
import Pub_passenger
import Pub_control
import Pub_pilot

import multiprocessing

p1 = multiprocessing.Process(target=Pub_pressure.run)
p2 = multiprocessing.Process(target=Pub_pressure_int.run)
p3 = multiprocessing.Process(target=Pub_passenger.run)
p4 = multiprocessing.Process(target=Pub_pilot.run)
p5 = multiprocessing.Process(target=Pub_control.run)

if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()








