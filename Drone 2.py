from djitellopy import tello
from time import sleep

Mi = tello.Tello()
Mi.connect()
print(Mi.get_battery())

Mi.takeoff()

# Takeoff Point
Mi.move_up(95)
Mi.move_forward(325)
sleep(.5)
Mi.move_forward(325)
sleep(1)

# Moving in to the must fly zone
Mi.rotate_counter_clockwise(90)
Mi.move_forward(325)
sleep(1)

# Going to the start I think
Mi.rotate_counter_clockwise(90)
Mi.move_forward(325)
sleep(.5)
Mi.move_forward(325)
sleep(1)

# Landing zone, probably, maybe
Mi.rotate_counter_clockwise(90)
Mi.move_forward(325)
sleep(1)

Mi.land()
