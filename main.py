######################################################
### Main-Program                                   ###
### Version: 1.00                                  ###
######################################################
from machine import Pin, Timer                              # RaspberryPi Pico2040 -> Hardware-Library
from module_init import Global_Module as MyModule
#import module_serial
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

    read_loop = MySerial.sercon.read_loop

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

    if MyModule.inc_ws2812:
        print("WS2812 -> Load-Module")
        import module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        print("WS2812 -> Run self test")
        MyWS2812.self_test()
        print("WS2812 -> Blink Test")
        MyWS2812.do_blink_test()
        print("WS2812 -> Dot-Test")
        MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        print("Decode -> Load-Module")
        import module_decode as MyDecode
        print("Decode -> Setup")
        MyDecode.decode_setup()
        print("Decode -> Test")
        MyDecode.decode_test("Test")

    if MyModule.inc_serial:
        print("Serial-COM -> Load-Module")
        import module_serial as MySerial
        print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        print("Serial-Con -> Test")
        MySerial.sercon_write_out("Test")


    print("End of Main !")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":
    main()

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
