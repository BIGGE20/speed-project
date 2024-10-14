# A simple App that fills an empty drum to 25 litres. The drum will be filled at 5 liter increments every 1 second untill it fills up.

import time

drum = 0

while drum < 25:
    start_time = time.time()
    print(f"Drum containt {drum} liters")
    drum = drum + 5
    time.sleep(1)
end_time = time.time
print(f"drum is full. volume:{drum}.\nTime of completion {end_time}")
