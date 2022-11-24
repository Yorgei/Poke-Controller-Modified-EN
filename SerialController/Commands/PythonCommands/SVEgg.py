
from Commands.Keys import Button
from Commands.PythonCommandBase import PythonCommand

class SV_Mash_A(PythonCommand):
    NAME = '[SV]Spam A for Eggs'

    def __init__(self):
        super().__init__()

    def do(self):
        while True:
            # Spamming B is less efficient, but I'm unsure if eggs can spawn
            # if a textbox is open, so this hopefully closes them and sends
            # the eggs to your box since you click no on sending them to the
            # academy.
            print('Waiting 3 minutes')
            waited = 0
            while True:
                self.checkIfAlive()
                self.wait(1)
                waited += 1
                if waited >= 180:
                    break
            self.press(Button.A, wait=1)
            self.pressRep(Button.B, repeat=80, interval=0.55)
            
