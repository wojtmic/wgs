import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk # type: ignore

class Button(Gtk.Button):
    def __init__(self, label: str):
        Gtk.Button.__init__(self, label=label)
        self.add_events(Gdk.EventMask.SCROLL_MASK)

        self.connect("button-press-event", self.on_press)
        self.connect("scroll-event", self.on_scroll)
    
    def do_propagation(self, event):
        if event.type == Gdk.EventType.SCROLL:
            return True
        else:
            return Gtk.Button.do_propagation(self, event)

    def on_click(self, widget, event):
        "Defines on left click event"
        pass
    
    def on_click_right(self, widget, event, button):
        "Defines on right click event"
        pass

    def on_click_middle(self, widget, event, button):
        "Defines on middle click event"
        pass
    
    def on_press(self, widget, event):
        """!!DO NOT USE!!
        This function is used internally to handle button press events.
        Please use either:
        - on_click
        - on_click_right
        - on_click_middle
        """
        
        if event.button == 1:
            self.on_click(widget, event)
        elif event.button == 3:
            self.on_click_right(widget, event, 3)
        elif event.button == 2:
            self.on_click_middle(widget, event, 2)
        else:
            self.on_click(widget, event)

    def on_scroll_up(self, widget, event):
        pass

    def on_scroll_down(self, widget, event):
        pass

    def on_scroll_left(self, widget, event):
        pass

    def on_scroll_right(self, widget, event):
        pass

    def on_scroll(self, widget, event):
        """!!DO NOT USE!!
        This function is used internally to handle scroll events.
        Please use either:
        - on_scroll_up
        - on_scroll_down
        """

        if event.direction == Gdk.ScrollDirection.UP:
            self.on_scroll_up(widget, event)
        elif event.direction == Gdk.ScrollDirection.DOWN:
            self.on_scroll_down(widget, event)
        elif event.direction == Gdk.ScrollDirection.LEFT:
            self.on_scroll_left(widget, event)
        elif event.direction == Gdk.ScrollDirection.RIGHT:
            self.on_scroll_right(widget, event)
