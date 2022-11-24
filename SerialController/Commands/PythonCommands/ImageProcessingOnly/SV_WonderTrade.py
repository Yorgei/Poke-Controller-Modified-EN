from Commands.PythonCommandBase import PythonCommand
from Commands.Keys import Button, Direction, Hat
from Commands.PythonCommandBase import ImageProcPythonCommand

import time


class WonderTrade(ImageProcPythonCommand):
    NAME = "[EN] [SV] Wonder Trade v0.1"
    CAPTURE_DIR = "Screenshot/swsh_wondertrade/"

    def __init__(self, cam):
        super().__init__(cam)
        self.row = 5
        self.col = 6
        self.boxes = 1
        self.cam = cam
        self.pkm = 112

    def check_trade_complete_en(self):
        return self.isContainTemplate("/sv/check.png", 0.8)

    def check_pokeportal(self):
        return self.isContainTemplate('/sv/pokeportal.png')
    
    def check_surprise_selected(self):
        return self.isContainTemplate('/sv/selected_surprise.png', use_gray=False, threshold=0.9)

    def check_pokedex(self):
        return self.isContainTemplate('/sv/pokedex.png', use_gray=True, threshold=0.9)

    def do(self):
        # TODO: Check for Online Connection
        # TODO: Add dialog for Pokedex count etc
        # Open Menu
        self.press(Button.X, wait=1)
        # Move over to Pokemon to reset
        self.pressRep(Hat.LEFT, repeat=3, interval=0.5, wait=1)
        # Move to PokePortal
        self.press(Hat.RIGHT, wait=0.8)
        self.pressRep(Hat.BTM, repeat=3, interval=0.5, wait=1)
        self.press(Button.A)
        
        wait_amnt = 0
        while not self.check_pokeportal():
            self.wait(1)
            wait_amnt += 1
            if wait_amnt >= 30:
                print('Timed out looking for pokeportal')
                return
        
        while not self.check_surprise_selected():
            self.press(Hat.BTM, wait=1)
        
        # Actually start trading here
        self.press(Button.A, wait=8)
        trade_count = 0
        new_pokemon = 0
        # TODO: Add dialog box to set how many boxes / "infinite" mode
        # TODO: Add options for screenshotting and create a "Pokedex" mode
        for b in range(0, self.boxes):
            for r in range(0, self.row):
                for c in range(0, self.col):
                    if not self.cam.isOpened():
                        print('Camera not available')
                        return
                    else:
                        # Comment out to loop over same box (for pokedex i guess?)
                        # if b > 0:
                        #     self.pressRep(Button.R, repeat=b, interval=0.5, wait=3)
                        if c > 0:
                            self.pressRep(Hat.RIGHT, repeat=c, interval=0.5, wait=0.5)
                        if r > 0:
                            self.pressRep(Hat.BTM, repeat=r, interval=0.5, wait=0.5)
                        # Extra A presses here because for some reason I would get communication
                        # error that didn't discconect me? Gamefreak please...
                        self.pressRep(Button.A, repeat=10, interval=1, wait=1)
                        # print('Waiting for trade to complete')
                        while not self.check_trade_complete_en():
                            self.wait(0.5)
                        trade_count += 1
                        self.press(Button.Y, wait=9)
                        self.press(Button.A, wait=24)
                        print(f'Finished Trade {trade_count}')
                        self.camera.saveCapture()
                        self.wait(8)
                        if self.check_pokedex():
                            self.wait(5)
                            self.pkm += 1
                            print(f'New Pokemon! You now have {self.pkm} registered in your Pokedex!')
                            new_pokemon += 1
                            self.camera.saveCapture(filename=f'new_pokemon_{new_pokemon}.png')
                            self.press(Button.A, wait=7)
                        self.press(Button.A, wait=4)
        
        return