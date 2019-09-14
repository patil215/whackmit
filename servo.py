import wiringpi
import time

class Whacker:
    UP_POS = 5
    DOWN_POS = 140
    
    def __init__(self):
        self.initialized = False

    def initialize(self):
        wiringpi.wiringPiSetupGpio()

        wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

        wiringpi.pwmSetClock(192)
        wiringpi.pwmSetRange(2000)

    def strike(self):
        wiringpi.pwmWrite(18, self.DOWN_POS)
        time.sleep(1)

    def reset(self):
        wiringpi.pwmWrite(18, self.UP_POS)
        time.sleep(1)