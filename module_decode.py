import module_ws2812

class Decoder:

    def __init__(self):
        
        self.data = ""
        self.array = []
        self.valid_flag = False
        self.value_1 = 0
        self.value_2 = 0

    def res_valid_flag(self):
        self.valid_flag = False

    def get_valid_flag(self):
        return self.valid_flag

    def send_data(self, data):
        self.data = data
        self.data_split()

    def data_split(self):
        self.array = self.data.split(",")
        self.cmd_decode()

    def get_data(self):
        return self.data

    def get_array(self):
        return self.array

    def cmd_decode(self):
        if self.array[0] == "set":
            #print("Command -> Set")
            if self.array[1] == "on":
                print("Parameter -> On")
                
            if self.array[1] == "off":
                print("Parameter -> Off")
            if self.array[1] == "def":
                print("Parameter -> Default")
            if self.array[1] == "bri":
                print("Parameter -> Brightness")
        if self.array[0] == "do":
            #print("Command -> do")
            if self.array[1] == "led":
                #print("Parameter -> led")
                self.value_1 = int(self.array[2])
                self.value_2 = int(self.array[3])                            
                if self.value_2 == 1:
                    #print("LED,1,1")
                    self.valid_flag = True
                    module_ws2812.led_obj[self.value_1 - 1].show_blink()
                    if self.value_1 == 1:
                        module_ws2812.led_obj[10].show_blink()

            if self.array[1] == "all":
                if self.array[2] == "on":
                    #print("do,all,on")
                    self.valid_flag = True
                    module_ws2812.do_all_no_blink()
                    module_ws2812.do_all_on()
                    
                if self.array[2] == "off":
                    #print("do,all,off")
                    self.valid_flag = True
                    module_ws2812.do_all_no_blink()
                    module_ws2812.do_all_off()

                if self.array[2] == "def":
                    #print("do,all,def")
                    self.valid_flag = True
                    module_ws2812.do_all_no_blink()
                    module_ws2812.do_all_def()


def decode_setup():
    
    global cmd_dec
    
    cmd_dec = Decoder()


def decode_test():
    
    test_string = "do,led,10,10"
    
    cmd_dec.send_data(test_string)
    
    test_string = "do,all,on"
    
    cmd_dec.send_data(test_string)

def main():

    decode_setup()

    decode_test()





if __name__ == "__main__":
    main()
