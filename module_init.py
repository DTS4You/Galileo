# #############################################################################
# ### MyGlobal
# #############################################################################

class Global_WS2812:

    numpix_1            = 31 * 2        # Anzahl LEDs im 1. Stripe
    numpix_2            = 31 * 2        # Anzahl LEDs im 2. Stripe
    numpix_3            = 31 * 3        # Anzahl LEDs im 3. Stripe
    numpix_4            = 31 * 3        # Anzahl LEDs im 4. Stripe

    seg_01_strip        = 0             #  1. Ledsegment -> Stripe
    seg_01_start        = 0             #  1. Ledsegment -> Start
    seg_01_count        = 31            #  1. Ledsegment -> Anzahl
    seg_02_strip        = 0             #  2. Ledsegment -> Stripe
    seg_02_start        = 31            #  2. Ledsegment -> Start
    seg_02_count        = 31            #  2. Ledsegment -> Anzahl

    seg_03_strip        = 1             #  3. Ledsegment -> Stripe
    seg_03_start        = 0             #  3. Ledsegment -> Start
    seg_03_count        = 31            #  3. Ledsegment -> Anzahl
    seg_04_strip        = 1             #  4. Ledsegment -> Stripe
    seg_04_start        = 31            #  4. Ledsegment -> Start
    seg_04_count        = 31            #  4. Ledsegment -> Anzahl

    seg_05_strip        = 2             #  5. Ledsegment -> Stripe
    seg_05_start        = 0             #  5. Ledsegment -> Start
    seg_05_count        = 31            #  5. Ledsegment -> Anzahl
    seg_06_strip        = 2             #  6. Ledsegment -> Stripe
    seg_06_start        = 31            #  6. Ledsegment -> Start
    seg_06_count        = 31            #  6. Ledsegment -> Anzahl
    seg_07_strip        = 2             #  7. Ledsegment -> Stripe
    seg_07_start        = 62            #  7. Ledsegment -> Start
    seg_07_count        = 31            #  7. Ledsegment -> Anzahl

    seg_08_strip        = 3             #  8. Ledsegment -> Stripe
    seg_08_start        = 0             #  8. Ledsegment -> Start
    seg_08_count        = 31            #  8. Ledsegment -> Anzahl
    seg_09_strip        = 3             #  9. Ledsegment -> Stripe
    seg_09_start        = 31            #  9. Ledsegment -> Start
    seg_09_count        = 31            #  9. Ledsegment -> Anzahl
    seg_10_strip        = 3             # 10. Ledsegment -> Stripe
    seg_10_start        = 62            # 10. Ledsegment -> Start
    seg_10_count        = 31            # 10. Ledsegment -> Anzahl

class Global_Color:

    color_def           = (  0,  0, 20)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
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
