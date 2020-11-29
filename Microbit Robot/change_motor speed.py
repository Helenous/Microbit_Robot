from microbit import *

while True:
                                #forward at 100% speed #testNov29
        pin8.write_digital(0)
        pin12.write_digital(0)
        pin0.write_digital(1)
        pin16.write_digital(0) 
        sleep(2000) 
                                #forward at 40% speed
        pin8.write_analog(410)
        pin12.write_digital(0)
        pin0.write_analog(410)
        pin16.write_digital(0) 
        sleep(2000)
                                #smooth right turn
        pin8.write_digital(0)  
        pin12.write_analog(102)
        pin0.write_analog(593)
        pin16.write_digital(0)       
        sleep(2000)
                                #stop motors
        pin8.write_digital(0)
        pin12.write_digital(0)
        pin0.write_digital(0)
        pin16.write_digital(0)       
        sleep(2000)   
                                #reverse at 100% speed
        pin8.write_digital(0)
        pin12.write_digital(1)
        pin0.write_digital(0)
        pin16.write_digital(1) 
        sleep(2000)   
                                #reverse at 40% speed    
        pin8.write_analog(613)
        pin12.write_digital(1)
        pin0.write_analog(613)
        pin16.write_digital(1) 
        sleep(2000)    
                                #stop motors
        pin8.write_digital(0)
        pin12.write_digital(0)
        pin0.write_digital(0)
        pin16.write_digital(0)       
        sleep(2000)
        

