from microbit import *
import radio
radio.config(channel=20)
radio.on()
radio.config(power=7)


while True:
    incoming = radio.receive()
    if incoming == "left":              # SMOOTH LEFT TURN
        display.show(Image.ARROW_E)
        pin8.write_analog(593)          # Right motor (Motor A) at 58% spped
        pin12.write_digital(0)
        pin0.write_digital(0)
        pin16.write_analog(102)         # Left motor(Motor B) at 10% spped
        sleep(100)
    elif incoming == "right":           # SMOOTH RIGHT TURN
        display.show(Image.ARROW_W)
        pin8.write_digital(0)
        pin12.write_analog(102)         # Right motor (Motor A) at 10% spped
        pin0.write_analog(593)          # Left motor (Motor B) at 58% spped
        pin16.write_digital(0)
    elif incoming == "forward":         #MOVE FORWARD AT 100% speed
        display.show(Image.ARROW_N)
        pin8.write_digital(1)
        pin12.write_digital(0)
        pin0.write_digital(1)
        pin16.write_digital(0)
        
    elif incoming == "reverse":
        display.show(Image.ARROW_S)     #REVERSE AT 100% spped
        pin8.write_digital(0)
        pin12.write_digital(1)
        pin0.write_digital(0)
        pin16.write_digital(1)
        
    elif incoming == "stop":            #STOP MOTORS
        display.show(Image.ASLEEP)
        pin8.write_digital(0)
        pin12.write_digital(0)
        pin0.write_digital(0)
        pin16.write_digital(0)
        

    
    
        
        

