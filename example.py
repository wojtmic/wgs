from __init__ import WidgetWindow
from widgets.button import Button

class MyButton(Button):
    def __init__(self, label: str):
        Button.__init__(self, label)
    
    def on_click(self):
        print("Pressed!")
    
    def on_click_right(self):
        print("Right click!")
    
    def on_click_middle(self):
        print("Middle click!")
    
    def on_scroll_down(self):
        print("Scrolled down!")
    
    def on_scroll_up(self):
        print("Scrolled up!")

win = WidgetWindow()
win.snap_window("left", "top")
button = MyButton("My Button")
win.add(button)

win.run()
