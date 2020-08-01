from microbit import *
from utime import ticks_us, sleep_us, ticks_diff

display.show(Image.HAPPY)


def sonar( ):
    pin13.write_digital(0) # Clear trigger
    sleep_us(10)
    pin13.write_digital(1) # Send 10us Ping pulse
    sleep_us(10)
    pin13.write_digital(0)
    while pin14.read_digital() == 0: # ensure Ping pulse has cleared
        pass
    start = ticks_us() # define starting time
    while pin14.read_digital() == 1:# wait for Echo pulse to return
        pass
    end = ticks_us() # define ending time
    cm = ticks_diff(end, start) // 58   # Distance = Time divided by 58
    return cm

while True:
    
    if sonar() < 15:
                                    #GO BACKWARD AT 100% SPPED
        pin8.write_digital(0)
        pin12.write_digital(1)
        pin0.write_digital(0)
        pin16.write_digital(1)
        sleep (1000)
                                    #SMOOTH TURN RIGHT AR REDUCED SPEED
        pin8.write_digital(0)
        pin12.write_analog(102)
        pin0.write_analog(593)
        pin16.write_digital(0)
        sleep(700)
    else:                           #GO FORWARD AT 100% SPEED
        pin8.write_digital(1)
        pin12.write_digital(0)
        pin0.write_digital(1)
        pin16.write_digital(0)

    
        
        

