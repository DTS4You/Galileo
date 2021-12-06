### Main-Program ###
from machine import Pin, Timer
import module_init
import module_ws2812
#import module_serial
#import module_decode
#import time

# led = Pin(25, Pin.OUT)        # Debug LED
flag = False

blink_freq = 3.0        # Blink Frequenz

def tick(timer):
    global flag
    flag = True


def do_loop():
    # --------------------------------------------------------------------------
    # --- Loop forever
    # --------------------------------------------------------------------------
    while True:

        # Blink Timer Flag
        if flag:
            flag = False
            module_ws2812.do_blink()

            # Serialread Data
            if module_serial.sercon.read():
                # print(module_serial.sercon.get_string())
                module_decode.cmd_dec.send_data(module_serial.sercon.get_string())
                if module_decode.cmd_dec.get_valid_flag():
                    module_serial.sercon.write("ack\n")
                    module_decode.cmd_dec.res_valid_flag()
                else:
                    module_serial.sercon.write("error\n")

            # Loop-Delay !!!
        time.sleep(0.05)
        # --------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    global mg

    # Global-Init
    mg = module_init.MyGlobal
    print(mg.seg_01_strip)

    # WS2812 Setup
    module_ws2812.setup_ws2812()
    module_ws2812.self_test()
    module_ws2812.do_blink_test()

    # Serial-COM
    #module_serial.sercon_setup()
    #module_serial.sercon_write_test()

    # Decode
    #module_decode.decode_setup()
    #module_decode.decode_test()

    # Timer definieren
    #timer_blink = Timer()
    #timer_blink.init(freq=blink_freq, mode=Timer.PERIODIC, callback=tick)

    # LEDs auf Startbild
    #module_ws2812.do_all_def()


# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":
    main()

# Normal sollte das Programm hier nie ankommen !
print("End of Programm !!!")

# ##############################################################################
