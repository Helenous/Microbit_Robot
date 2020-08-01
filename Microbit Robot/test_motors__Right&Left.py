from microbit import *

while True:
                                    #Robot turns right for 2 second
        pin8.write_digital(0)
        pin12.write_digital(1)
        pin0.write_digital(1)
        pin16.write_digital(0)
        sleep(2000)
                                    #Robot turns left for 2 seconds
        pin8.write_digital(1)
        pin12.write_digital(0)
        pin0.write_digital(0)
        pin16.write_digital(1) 
        sleep(2000)    
    
        
        

