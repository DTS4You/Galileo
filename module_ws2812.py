# Module WS2812 V1.01
import time
import module_neopixel
import module_init

class LedState:
    def __init__(self):
        self.state = False
        self.blink_state = False

    def set(self, set):
        self.state = set

    def get(self):
        return self.state
    
    def do_blink(self):
        self.blink_state = not self.blink_state

    def get_blink(self):
        return self.blink_state

    def refresh(self):
        self.state = False
        for strips in strip_obj:
            strips.show()


class Ledsegment:

    def __init__(self, neopixel, start, count):
        self.neopixel = neopixel
        self.start = start
        self.stop = self.start + count - 1
        self.count = count
        self.blink_state = False
        self.color_on = (0,0,0)
        self.color_default = (0,0,0)
        self.color_off = (0,0,0)
        self.color_blink_on = (0,0,0)
        self.color_blink_off = (0,0,0)
        self.color_show = (0,0,0)

    def set_color_on(self, color_on):
        self.color_on = color_on

    def set_color_def(self, color_default):
        self.color_default = color_default
        
    def set_color_off(self, color_off):
        self.color_off = color_off

    def set_color_blink_off(self, color_blink_off):
        self.color_blink_off = color_blink_off

    def set_color_blink_on(self, color_blink_on):
        self.color_blink_on = color_blink_on

    def show_on(self):
        self.color_show = self.color_on
        self.blink_state = False
        self.set_pixel()

    def show_def(self):
        self.color_show = self.color_default
        self.blink_state = False
        self.set_pixel()

    def show_off(self):
        self.color_show = self.color_off
        self.blink_state = False
        self.set_pixel()

    def show_blink(self):
        self.blink_state = True
        if ledstate.get_blink():
            self.color_show = self.color_blink_on
        else:
            self.color_show = self.color_blink_off
        self.set_pixel()

    def get_blink_state(self):
        return self.blink_state

    def set_pixel(self):
        self.neopixel.set_pixel_line(self.start, self.stop, self.color_show)

    def show_stripe(self):
        self.neopixel.show()



def setup_ws2812():

    mg = module_init.Global_WS2812

    global strip_obj
    global led_obj
    global ledstate
    
    led_obj = []
    strip_obj = []

    ledstate = LedState()
    
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_1, 0, 2, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_2, 1, 3, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_3, 2, 4, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_4, 3, 5, "GRB"))
    
    led_obj.append(Ledsegment(strip_obj[mg.seg_01_strip], mg.seg_01_start, mg.seg_01_count))      #  0 (01) -> LED Position -> # 01 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_02_strip], mg.seg_02_start, mg.seg_02_count))      #  1 (02) -> LED Position -> # 02 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_03_strip], mg.seg_03_start, mg.seg_03_count))      #  2 (03) -> LED Position -> # 03 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_04_strip], mg.seg_04_start, mg.seg_04_count))      #  3 (04) -> LED Position -> # 04 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_05_strip], mg.seg_05_start, mg.seg_05_count))      #  4 (05) -> LED Position -> # 05 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_06_strip], mg.seg_06_start, mg.seg_06_count))      #  5 (06) -> LED Position -> # 06 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_07_strip], mg.seg_07_start, mg.seg_07_count))      #  6 (07) -> LED Position -> # 07 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_08_strip], mg.seg_08_start, mg.seg_08_count))      #  7 (08) -> LED Position -> # 08 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_09_strip], mg.seg_09_start, mg.seg_09_count))      #  8 (09) -> LED Position -> # 09 #
    led_obj.append(Ledsegment(strip_obj[mg.seg_10_strip], mg.seg_10_start, mg.seg_10_count))      #  9 (10) -> LED Position -> # 10 #
    
    my_color = module_init.Global_Color

    for strips in strip_obj:
        strips.brightness(255)
   
    # Alle Leds auf Vorgabewert -> aus
    for strips in strip_obj:
        strips.set_pixel_line(0, strips.num_leds - 1, my_color.color_off)
    for strips in strip_obj:
        strips.show()

    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.set_color_off(my_color.color_off)
        leds.set_color_def(my_color.color_def)
        leds.set_color_on(my_color.color_on)
        leds.set_color_blink_on(my_color.color_blink_on)
        leds.set_color_blink_off(my_color.color_blink_off)
    
    # Blinken aus
    do_all_no_blink()


def do_all_on():
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_on()
    ledstate.refresh()

def do_all_off():
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_off()
    ledstate.refresh()

def do_all_def():
    # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_def()
    ledstate.refresh()

def do_all_no_blink():
    for leds in led_obj:
        leds.blink_state = False

def do_blink():
    ledstate.do_blink()
    for leds in led_obj:
        if leds.get_blink_state():
            leds.show_blink()
        else:
            pass
    
    ledstate.set(True)
    ledstate.refresh()

def do_refresh():

    ledstate.refresh()

def do_get_state():

    return ledstate.get()
    
def set_all_def():                              # Setze Farbwerte in alle LED-Objekte
    for leds in led_obj:
        leds.show_def()
    ledstate.refresh()

def self_test():                                # Pro Stripe einmal Aus-RGB (25%) -Aus 
    for strips in strip_obj:
        # Alle Aus
        strips.set_pixel_line(0, strips.num_leds - 1, (0,0,0))
        strips.show()
        time.sleep(0.3)
        # Alle Rot
        strips.set_pixel_line(0, strips.num_leds - 1, (50,0,0))
        strips.show()
        time.sleep(0.3)
        # Alle Grün
        strips.set_pixel_line(0, strips.num_leds - 1, (0,50,0))
        strips.show()
        time.sleep(0.3)
        # Alle Blau
        strips.set_pixel_line(0, strips.num_leds - 1, (0,0,50))
        strips.show()
        time.sleep(0.3)
        # Alle Aus
        strips.set_pixel_line(0, strips.num_leds - 1, (0,0,0))
        strips.show()
        time.sleep(0.3)


def do_blink_test():
    loops = 4
    looptime = 0.15
    #print(len(led_obj))
    for x in range(len(led_obj)):
        led_obj[x].show_blink()
        for i in range(loops):
            do_blink()
            time.sleep(looptime)
        led_obj[x].show_off()
        do_refresh()


def main():

    print("WS2812 -> Setup")
    setup_ws2812()
        
    print("WS2812 -> Run self test")
    self_test()
    
    print("Blink Test")
    do_blink_test()
    
    #print("Ende")
    #print("WS2812 Run")
    #run_ws2812()


# End

# ------------------------------------------------------------------------------
# --- Main
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# ##############################################################################