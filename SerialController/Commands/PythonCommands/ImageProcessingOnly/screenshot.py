#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.Keys import Button, Direction
from Commands.PythonCommandBase import ImageProcPythonCommand


class ScreenShot(ImageProcPythonCommand):
    NAME = '[DEBUG] Screenshot Example'

    def __init__(self, cam):
        super().__init__(cam)

    def do(self):
        self.camera.saveCapture()
        self.camera.saveCapture(filename="Filename_Example")
        self.camera.saveCapture(filename="4Coords_Example", crop=1,
                                crop_ax=[500, 300, 800, 500])
        self.camera.saveCapture(filename="Starting_Point_Size_example",
                                crop=2, crop_ax=[500, 300, 300, 300])
