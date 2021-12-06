from machine import Pin, Timer

led = Pin(25, Pin.OUT)
flag = False

def tick(timer):
    global flag
    flag = True

def main():
    global led
    global flag

    tim = Timer()
    tim.init(freq=3.0, mode=Timer.PERIODIC, callback=tick)

    #--------------------------------------------------------------------------
    #--- Loop forever
    #--------------------------------------------------------------------------
    while True:
        if flag:
            flag = False
            led.toggle()
    #--------------------------------------------------------------------------
    
###############################################################################
### Main                                                                    ###
###############################################################################

if __name__ == "__main__":
    main()

# Normal sollte das Programm hier nie ankommen !
print("End of Programm !!!")
###############################################################################