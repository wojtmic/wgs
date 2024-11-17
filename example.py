from __init__ import WidgetWindow
from widgets.button import Button

import subprocess

class MyButton(Button):
    def __init__(self, label: str):
        Button.__init__(self, label)
    
    def on_click(self):
        print("Pressed!")
    
    def on_click_right(self):
        win.close()
        subprocess.run(['pavucontrol'])
    
    def on_click_middle(self):
        print("Middle click!")
    
    def on_scroll_down(self):
        print("Scrolled down!")
    
    def on_scroll_up(self):
        print("Scrolled up!")

win = WidgetWindow()
win.expand(True, False)
win.snap_window("left", "top")
button = MyButton("My Button")
button2 = MyButton("My Button 2")
win.add(button)
win.add(button2)

win.run()
