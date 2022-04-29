######################################################
### Main-Program                                   ###
### Version: 1.00                                  ###
######################################################
from machine import Pin, Timer                              # RaspberryPi Pico2040 -> Hardware-Library
from module_init import Global_Module as MyModule
#import module_serial
import time


def blink_func():
    pass

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main ===")
    
    blink_couter = 0
       
    while MySerial.sercon_read_flag():

        if blink_couter > 20:
            blink_func()
        MySerial.sercon_read_line()
        if MySerial.get_ready_flag():       # Zeichenkette empfangen
            #print(MySerial.get_string())
            MyDecode.decode_input(str(MySerial.get_string()))
            #MyDecode.decode_printout()
            if MyDecode.get_valid_flag() == True:
                print("Valid Command")
                if MyDecode.get_cmd_1() == "do":
                    print("do")
                    if MyDecode.get_cmd_2() == "all":
                        print("all")
                        if MyDecode.get_value_1() == 0:
                            print("off")
                            MyWS2812.do_all_off()
                        if MyDecode.get_value_1() == 2:
                            print("def")
                            MyWS2812.do_all_def()
        

        blink_couter = blink_couter + 1
        # Loop-Delay !!!
        time.sleep(0.01)
        
        

        



    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_ws2812:
        print("WS2812 -> Load-Module")
        import module_ws2812_v2 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        ### Test ###
        #print("WS2812 -> Run self test")
        #MyWS2812.self_test()
        #print("WS2812 -> Blink Test")
        #MyWS2812.do_blink_test()
        #print("WS2812 -> Dot-Test")
        #MyWS2812.do_dot_test()

    if MyModule.inc_decoder:
        print("Decode -> Load-Module")
        import module_decode as MyDecode
        print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")

    if MyModule.inc_serial:
        print("Serial-COM -> Load-Module")
        import module_serial as MySerial
        print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        print("Serial-Con -> Test")
        MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################
