# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = True
    inc_serial          = True


class Global_WS2812:

    #seg_len            = 8             # Testaufbau 8
    seg_len             = 31            # Modell 31

    numpix_1            = seg_len * 2   # Anzahl LEDs im 1. Stripe
    numpix_2            = seg_len * 2   # Anzahl LEDs im 2. Stripe
    numpix_3            = seg_len * 3   # Anzahl LEDs im 3. Stripe
    numpix_4            = seg_len * 3   # Anzahl LEDs im 4. Stripe

    seg_01_strip        = 0             #  1. Ledsegment -> Stripe
    seg_01_start        = 0             #  1. Ledsegment -> Start
    seg_01_count        = seg_len       #  1. Ledsegment -> Anzahl
    seg_02_strip        = 0             #  2. Ledsegment -> Stripe
    seg_02_start        = seg_len       #  2. Ledsegment -> Start
    seg_02_count        = seg_len       #  2. Ledsegment -> Anzahl

    seg_03_strip        = 1             #  3. Ledsegment -> Stripe
    seg_03_start        = 0             #  3. Ledsegment -> Start
    seg_03_count        = seg_len       #  3. Ledsegment -> Anzahl
    seg_04_strip        = 1             #  4. Ledsegment -> Stripe
    seg_04_start        = seg_len       #  4. Ledsegment -> Start
    seg_04_count        = seg_len       #  4. Ledsegment -> Anzahl

    seg_05_strip        = 2             #  5. Ledsegment -> Stripe
    seg_05_start        = 0             #  5. Ledsegment -> Start
    seg_05_count        = seg_len       #  5. Ledsegment -> Anzahl
    seg_06_strip        = 2             #  6. Ledsegment -> Stripe
    seg_06_start        = seg_len       #  6. Ledsegment -> Start
    seg_06_count        = seg_len       #  6. Ledsegment -> Anzahl
    seg_07_strip        = 2             #  7. Ledsegment -> Stripe
    seg_07_start        = seg_len * 2   #  7. Ledsegment -> Start
    seg_07_count        = seg_len       #  7. Ledsegment -> Anzahl

    seg_08_strip        = 3             #  8. Ledsegment -> Stripe
    seg_08_start        = 0             #  8. Ledsegment -> Start
    seg_08_count        = seg_len       #  8. Ledsegment -> Anzahl
    seg_09_strip        = 3             #  9. Ledsegment -> Stripe
    seg_09_start        = seg_len       #  9. Ledsegment -> Start
    seg_09_count        = seg_len       #  9. Ledsegment -> Anzahl
    seg_10_strip        = 3             # 10. Ledsegment -> Stripe
    seg_10_start        = seg_len * 2   # 10. Ledsegment -> Start
    seg_10_count        = seg_len       # 10. Ledsegment -> Anzahl

    color_def           = (  0,  0, 10)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
    color_dot           = ( 50, 50, 50)
    color_blink_on      = (100,100,100)
    color_blink_off     = ( 50, 50, 50)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz
    

def main():

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.numpix_2)
    print(mg.seg_01_strip, mg.seg_01_start, mg.seg_01_count)
    print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
