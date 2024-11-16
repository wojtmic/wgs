import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkLayerShell', '0.1')
from gi.repository import Gtk, GtkLayerShell, Gdk # type: ignore

class WidgetWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="My Widget")
        self.set_default_size(200, 100)
        
        # Initialize as layer shell window
        GtkLayerShell.init_for_window(self)
        
        # Set layer shell properties
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.TOP)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, False)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, False)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, False)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, False)
        
        # Make window floating
        self.set_decorated(False)
        
        # Connect destroy signal
        self.connect("destroy", Gtk.main_quit)
        self.connect("delete-event", self.on_delete_event)

        self.set_can_focus(True)
        self.grab_focus()
        GtkLayerShell.set_keyboard_interactivity(self, True)
        
        # Close on Escape
        self.connect("key-press-event", self.on_key_press)
    
    def set_size(self, width: int, height: int):
        """Sets the size of the window"""
        self.set_default_size(width, height)
    
    def set_window_pos(self, x: int, y: int):
        """Sets the position of the window"""
        self.move(x, y)

    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_Escape:
            self.destroy()  # Use destroy instead of main_quit
            return True
        return False
        
    def on_delete_event(self, widget, event):
        self.destroy()
        return True

    def run(self):
        self.show_all()
        Gtk.main()
