# Poke-Controller MODIFIED EN Translation

This is an unofficial English fork of the Poke-Controller Modified Repo by [Moi-Poke](https://github.com/Moi-poke). I'm not fluent so there will probably be a few translation mistakes, I'm only doing this as practice.

I have added some commands that are not present in Moi-poke's version and I have added Discord Webhook support as LINE isn't popular in the West.

The text below is a translation of Moi-Poke's README.

![](https://github.com/Moi-Poke/Poke-Controller/blob/photo/photos/poke-con-modded.png)

## Changes

### ~ver3.0

- Added additional logging functionality\
  Display button inputs in the main window, and logs of each function in the console screen and file output\
  Note: The button input display may occasionally be bugged.
- Added functionality to display a blue border when matching a template\
  When `show_position=False` is passed to `isContainTemplate` the border will not be shown.
- Added some sample scripts
  - InputSwitchKeyboard.py

    Sample code for automatic input of the Switch's keyboard
  - InputSerial.py

    Sample code for automatic input of serial code
  - LoggingSample.py

    Sample code for creating a macro log file

-----

### ~ver2.8

- Updated to Python Version 3.7.x (it should still be compatible with version 3.6)
- Added a FPS setting
- Added an option to change the video size
- Log text book now resizes correctly when the app is resized
- Added joystick functionality

  **Setting the tilt sensitivity of the Joystick**
  - スティックの移動可能な範囲を単位円の内部と考えて、\
    傾き度合いを0以上1以下で設定可能にしました。\
    例えば`Direction(Stick.LEFT, θ, r)`\
    というコマンドは、左スティックのx,y座標が
    ```
    x=r*cosθ
    y=r*sinθ
    ```
    となるような入力をします。この場合は半径rの円となります。
  - r=1.0をデフォルト値としているので\
    `Direction(Stick.LEFT, θ)`
    と書いた場合はr=1として認識されます。\
    より詳しくはサンプルコードを同梱していますので\
    そちらとSwitch内設定のスティックの補正画面を合わせて確認してください

  **Joystick control with a mouse**
  - マウスで直感的な操作ができそうな感じにしています。~~ラグがあるので操作は結構難しいです。~~\
    操作円の半径は変更可能なので、需要があればConfigファイルに載せます。 タッチパネル対応モニタ使用の際などの挙動は不明ですが、そちらのほうが向いているかもしれません。\
    またこの機能の追加に伴い、'Ctrl+左クリック'がクリック点座標表示になっています。
- 画面キャプチャ機能の追加
  - キャプチャしている画面部分を'Ctrl+Shift+左クリック'しながらドラッグした範囲をキャプチャすることができます。
- メニュー機能の追加

  Added new features
  - LINE Notifications\
    Added a LINE Notification command in Python Command. \
    **Usage**
    - Replace `paste_your_token_here` with your LINE API token in the line_token.ini file.
      ```python
      self.LINE_text("Type your message here")
      ```
      It is possible to send images and text at the same time \
      in a command using Image Recognition.
      ```python
      self.LINE_image("Type your message here")
      ```
    - The program will write to the log area LINE Token Check FAILED on startup if the token is invalid.
    - If the LINE Token is correct, the application will display the amount of API uses until the limit is reached and when it will reset \
    You can check it at any time with the Line Token Check in the menu options. Frequent notifications can cause you to reach the API limit.
    - Supports multiple LINE tokens. Add a new line and another token name to the line_token.ini file and pass it as an argument to the LINE functions. Check the sample code for examples.

  - Pokémon Home Link
  
    This may change significantly in the near future.
    Pokémon with different form names (e.g. Rotom) are currently only supported up to the 7th generation.
    You can add the following to `SerialController/db/poke_form_name.csv` to support them

  - Key Configurations added

    Added a key configurator. If multiple keys are pressed at the same time, they will not be sent to the console at the same time. \
    The format for the configuration file has been changed. \
    There is no function to restore the default settings, please read the Setting.py file if needed.
- ~~Button input function display function addition program (by KCT) is incorporated~~ Changed to original input display implementation since ver3.0.
- Cleaned up the GUI a bit
- Code Refactoring

  I have made my code more PEP8 compliant due to my development environment.
  - Changed from tab indentation to 4-space indentation.
  - Removed unnecessary imports, reordered and optimized imports.

## Installation

Added some required and recommend libraries. Please install them.
```python
pygubu
requests
pandas
numpy
```

## Misc

- The code for running OpenCV processing on NVIDIA GPU is included (TemplateMatchingTimeMeasure.py). \
   However, it is not available for libraries installable with `pip install` \
   If you want to use it, you need to build OpenCV for python from the source code with the option corresponding to your GPU. \
   It is quite difficult and takes a lot of time to process, but if you have the time, please try it. \
   `OpenCV + CUDA (+Windows)`
   If you search for such, the explanation page of the build will appear.

Below is the original README
- - -

Pythonで書く！Switchの自動化支援ソフトウェア

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## セットアップと使い方

- まずはモノの準備
  - [Github - wiki](https://github.com/KawaSwitch/Poke-Controller/wiki)

- 準備ができたら進みましょう
  - [Poke-Controllerの使い方](https://github.com/KawaSwitch/Poke-Controller/wiki/Poke-Controller%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9)

  - [デフォルトの実装コマンドの確認](https://github.com/KawaSwitch/Poke-Controller/wiki/%E3%83%87%E3%83%95%E3%82%A9%E3%83%AB%E3%83%88%E3%81%AE%E5%AE%9F%E8%A3%85%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89)

  - [新しいコマンドを作成](https://github.com/KawaSwitch/Poke-Controller/wiki/%E6%96%B0%E3%81%97%E3%81%84Python%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9)

分からないことや改善要望などがあれば遠慮なく[Issue](https://github.com/KawaSwitch/Poke-Controller/issues)まで  
[Q&A](https://github.com/KawaSwitch/Poke-Controller/wiki/Q&A)や[解決済みIssue](https://github.com/KawaSwitch/Poke-Controller/issues?q=is%3Aissue+is%3Aclosed)なども役に立つかもしれません

## クイックビュー

簡単に機能を見てみましょう

### コマンド作成用のライブラリの提供

通常のボタン押下  
`self.press(Button.A) # Aボタンを押して離す`  
`self.press(Button.A, 0.1, 1) # Aボタンを0.1秒間押して離した後, 1秒待機`

左右スティック & HAT(十字)キー  
`self.press(Direction.RIGHT, 5) # 左スティックを右に5秒間倒す`  
`self.press(Hat.LEFT) # 十字キー左を押して離す`

同時押し  
`self.press([Button.A, Button.B]) # AボタンとBボタンを同時に押して離す`

ホールド  
`self.hold([Direction.UP, Direction.R_DOWN], wait=1) # 左スティックを上, 右スティックを下に倒して1秒待つ`  
`self.press(Button.A) # スティックを倒した状態でAボタンを押して離す`

[リファレンス](https://github.com/KawaSwitch/Poke-Controller/wiki/Python%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89_%E4%BD%9C%E6%88%90How_to)やデフォルトのコマンドなども参考にして中身を覗いてみましょう  
作成したコマンドや便利な機能は[プルリク](https://github.com/KawaSwitch/Poke-Controller/pulls)や[Issue](https://github.com/KawaSwitch/Poke-Controller/issues)で頂けると非常に喜びます

### Pythonファイル管理

作成したコマンドのclassは1つのPythonファイルの中にいくつも記述できます  
またPythonCommandsのフォルダ内であればいくつもフォルダを作成可能です  
自由に配置していきましょう

![](https://github.com/KawaSwitch/Poke-Controller/blob/photo/photos/Wiki/PythonCommandHowTo/command_file_location.PNG)

### 実行時のコマンド切替

配置したコマンド群はマウス操作で簡単に切り替えることができます

### リロード機能

Poke-Controllerを動作しながらファイルの変更を再読込して反映することができます  
こつこつデバグしたい方におすすめ！

### 画像認識

キャプチャボードでSwitchの画面を取り込めば, シリアル通信だけでは叶わない操作もできるかも  
これらもライブラリとして機能を提供しています  
`self.isContainTemplate('status.png') # テンプレートマッチング`

現在の機能([実装内容](https://github.com/KawaSwitch/Poke-Controller/wiki/%E7%94%BB%E5%83%8F%E8%AA%8D%E8%AD%98%E3%81%A8%E3%81%AF))は少ないがアップデート予定  
![リリース前GUI](https://github.com/KawaSwitch/Poke-Controller/blob/photo/photos/pokecon_gui_before_release.PNG)

### キーボード操作

キーボードをスイッチのコントローラとして使用することができます

| Switchコントローラ | キーボード |
| ---- | ---- |
| A, B, X, Y, L, R | 'a', 'b', ...キー |
| ZL | 'k'キー |
| ZR | 'e'キー |
| MINUS | 'm'キー |
| PLUS | 'p'キー |
| LCLICK | 'q'キー |
| RCLICK | 'w'キー |
| HOME | 'h'キー |
| CAPTURE | 'c'キー |
| 左スティック | 矢印キー |

## リリース

- 過去リリース
  - [Github - Releases](https://github.com/KawaSwitch/Poke-Controller/releases)

- 進捗状況の確認
  - [Github - Project](https://github.com/KawaSwitch/Poke-Controller/projects)

- ロードマップ
  - [リリースについて](https://github.com/KawaSwitch/Poke-Controller/wiki/About-Releases)

## 貢献

これらの貢献者に感謝します ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/KawaSwitch"><img src="https://avatars3.githubusercontent.com/u/41296626?v=4" width="100px;" alt=""/><br /><sub><b>KawaSwitch</b></sub></a><br /><a href="https://github.com/KawaSwitch/Poke-Controller/commits?author=KawaSwitch" title="Code">💻</a> <a href="#maintenance-KawaSwitch" title="Maintenance">🚧</a> <a href="https://github.com/KawaSwitch/Poke-Controller/commits?author=KawaSwitch" title="Documentation">📖</a> <a href="#question-KawaSwitch" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/Moi-poke"><img src="https://avatars1.githubusercontent.com/u/59233665?v=4" width="100px;" alt=""/><br /><sub><b>Moi-poke</b></sub></a><br /><a href="https://github.com/KawaSwitch/Poke-Controller/commits?author=Moi-poke" title="Code">💻</a> <a href="#question-Moi-poke" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/xv13"><img src="https://avatars2.githubusercontent.com/u/47322147?v=4" width="100px;" alt=""/><br /><sub><b>xv13</b></sub></a><br /><a href="https://github.com/KawaSwitch/Poke-Controller/issues?q=author%3Axv13" title="Bug reports">🐛</a></td>
	<td align="center"><a href="https://github.com/vyPeony"><img src="https://avatars0.githubusercontent.com/u/39150264?v=4" width="100px;" alt=""/><br /><sub><b>vyPeony</b></sub></a><br /><a href="https://github.com/KawaSwitch/Poke-Controller/commits?author=vyPeony" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

このプロジェクトは, [all-contributors](https://github.com/all-contributors/all-contributors)仕様に準拠しています. どんな貢献も歓迎します！

## ライセンス

本プロジェクトはMITライセンスです  
詳細は [LISENCE](https://github.com/KawaSwitch/Poke-Controller/blob/master/LICENSE) を参照ください

また, 本プロジェクトではLGPLライセンスのDirectShowLib-2005.dllを同梱し使用しています  
[About DirectShowLib](http://directshownet.sourceforge.net/)  
