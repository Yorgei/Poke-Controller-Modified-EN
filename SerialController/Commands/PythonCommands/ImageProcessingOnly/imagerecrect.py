#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Commands.PythonCommandBase import ImageProcPythonCommand


class ImageRecRect(ImageProcPythonCommand):
    NAME = '[DEBUG] Image Recognition Overlay Example'

    def __init__(self, cam, gui=None):
        # ← [EN] Required arguments [JP] ← 必須の変更点です 引数が追加されています。
        super().__init__(cam, gui)
        self.cam = cam
        # [EN] This line isn't required, but just to be safe. [JP] この行はなくても動きますが一応
        self.gui = gui

    def do(self):
        for i in range(1):
            result = self.isContainTemplate("shiny_mark.png", 0.7, show_value=True,
                                            show_position=True,  # このオプションをFalseにすると枠が非表示になります
                                            show_only_true_rect=True,  # このオプションをFalseにすると、
                                            # 認識できなかった場合に最も近い部分に赤枠を表示します
                                            # 枠の表示時間(ミリ秒)  デフォルトは2000msです
                                            ms=1000
                                            )
            # self.wait(1)
