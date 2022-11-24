from Commands.PythonCommandBase import PythonCommand
from Commands.Keys import Button, Direction, Hat
from Commands.PythonCommandBase import ImageProcPythonCommand

import time


class WonderTrade(ImageProcPythonCommand):
    NAME = "[EN] [SwSh] Wonder Trade v0.1"
    CAPTURE_DIR = "Screenshot/swsh_wondertrade/"

    def __init__(self, cam):
        super().__init__(cam)
        self.row = 5
        self.col = 6
        self.boxes = 32
        self.cam = cam

    def check_ycomm_local_en(self):
        return self.isContainTemplate("/swsh_wondertrade/local_communication_en.png", 0.8)

    def check_ycomm_open(self):
        return self.isContainTemplate("/swsh_wondertrade/ycomm_menu.png", 0.8)

    def check_connected_internet(self):
        return self.isContainTemplate("/swsh_wondertrade/ycomm_connected.png", 0.8)

    def check_ycomm_internet_en(self):
        return self.isContainTemplate("/swsh_wondertrade/internet_en.png", 0.8)

    def check_trade_complete_en(self):
        return self.isContainTemplate("/swsh_wondertrade/trade_complete_en.png", 0.8)

    def open_ycomm(self):
        print('Pressing Y...')
        self.press(Button.Y)
        self.wait(2)
        print('Checking if Y-COMM is open...')
        if not self.check_ycomm_open():
            print('Y-COMM not open, restarting loop.')
            return False
        print('Checking Connection Type')
        if self.check_ycomm_local_en():
            print('Connecting to the internet')
            self.press(Button.PLUS, wait=10)
            if not self.check_connected_internet():
                print(
                    "Timed out while trying to confirm internet connection. Aborting script.")
                return False
            self.press(Button.A, wait=2)
        elif self.check_ycomm_internet_en():
            print('Connected to internet')
            return True
        else:
            print('Something went wrong, aborting...')
            return False

    def trade_pokemon(self):
        print('Pressing A to trade')
        wait_count = 0
        for _ in range(10):
            self.press(Button.A, wait=1)
        while not self.check_trade_complete_en():
            wait_count += 1
            self.wait(3)
        # Opens trade complete
        self.press(Button.Y, wait=15.5)
        # print('Saving screenshot, checking for hacked name')
        self.camera.saveCapture()
        self.wait(9)
        return

    def do(self):
        while True:
            curr_box = 0
            for b in range(0, self.boxes):
                for i in range(0, self.row):
                    for j in range(0, self.col):
                        if not self.cam.isOpened():
                            print('Camera not available, aborting...')
                            return
                        if not self.open_ycomm():
                            print('Ycomm error, aborting')
                            return
                        self.press(Direction.DOWN, wait=0.4)
                        self.press(Button.A)
                        print(
                            f'Trading Pokemon from Box {b} Row {i} Column {j}')
                        self.wait(4)
                        if curr_box != b:
                            curr_box = b
                            print('Changing boxes.')
                            self.press(Button.R, wait=1)
                        self.pressRep(Direction.DOWN,
                                      repeat=i, wait=0.4)
                        self.pressRep(Direction.RIGHT, repeat=j, wait=0.4)
                        self.trade_pokemon()
                        # TODO: Check if new pokedex entry then exit
