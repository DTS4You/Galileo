# Module Serial
from machine import UART
import time

debug = False

class SERCON:

    def __init__(self):

        self.uart = UART(0, baudrate=9600, bits=8, parity=None, stop=1)
        #self.rxData = bytes()
        self.txData = bytes()
        self.flag = True
        self.read_string = ""

    def write(self, string):
        self.txData = str.encode(string)
        self.uart.write(self.txData)

    def read(self):
        self.rxData = bytes()
        while self.uart.any() > 0:
            #print("Read Start")
            self.rxData += self.uart.read(1)
            #rint("Read Byte")
            time.sleep(0.01)
            
        if self.rxData.decode('utf-8') > "":
            self.read_string = self.rxData.decode('utf-8').strip()
            #print(self.read_string)
            return True
        else:
            return False
    
    def get_string(self):
        return self.read_string

def sercon_setup():
    
    global sercon
    sercon = SERCON()

def sercon_write_test():
    
    string_start = "Sercon is starting...\n"
    sercon.write(string_start)

def main():
    
    sercon_setup()
    
    print("Write Test")
    sercon_write_test()

    time.sleep(0.3)

    print("Read Loop")
    
    while True:
        if sercon.read():
            print(sercon.read_string)
            sercon.write("ack\n")
            
        
        # Loop-Delay !!!
        time.sleep(0.01)
        

    print("Ende")


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
