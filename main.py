######################################################
### Main-Program                                   ###
### Version: 1.00                                  ###
######################################################
from machine import Pin, Timer                              # RaspberryPi Pico2040 -> Hardware-Library
from module_init import Global_WS2812 as MyGlobal           # Modul Init    -> Globale Vorgabewerte
import module_ws2812_v2 as MyWS2812                         # Modul WS2812  -> WS2812-Ansteuerung
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
            MyWS2812.do_blink()

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

    # WS2812 Setup
    print("WS2812 -> Setup")
    MyWS2812.setup_ws2812()
    print("WS2812 -> Run self test")
    MyWS2812.self_test()
    print("WS2812 -> Blink Test")
    MyWS2812.do_blink_test()

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

    print("End of Main !")

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
