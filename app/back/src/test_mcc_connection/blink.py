# import board
# from digitalio import *
# from time import sleep


class Blink:
    def __init__(self):
        print('SETUP')
        # self.led = DigitalInOut(board.LED)
        # self.led.direction = Direction.OUTPUT

    def blink(self):
        print('WORK')
        for _ in range(5):
            print('\tBLINK')
            # self.led.value = True
            # sleep(.5)
            # self.led.value = False
            # sleep(.5)

        print('DONE')
