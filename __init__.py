import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkLayerShell', '0.1')
from gi.repository import Gtk, GtkLayerShell, Gdk, GLib # type: ignore

class WidgetWindow(Gtk.Window):
    def __init__(self, orientation=Gtk.Orientation.VERTICAL):
        Gtk.Window.__init__(self, title="My Widget")
        self.set_default_size(200, 100)

        self._container = Gtk.Box(orientation=orientation, spacing=6)
        Gtk.Window.add(self, self.container)

        self._expand_x = False
        self._expand_y = False
        
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
        GtkLayerShell.set_keyboard_mode(self, GtkLayerShell.KeyboardMode.ON_DEMAND)
        
        # Close on Escape
        self.connect("key-press-event", self.on_key_press)
    
    def set_size(self, width: int, height: int):
        """Sets the size of the window"""
        self.set_default_size(width, height)
    
    def set_window_pos(self, x: int, y: int):
        """Sets the position of the window"""
        self.move(x, y)
    
    def snap_window(self, wherex: str, wherey: str):
        """Snaps the window to the edge of the screen"""
        valid_x = ['left', 'right', 'center']
        valid_y = ['top', 'bottom', 'center']
        if wherex not in valid_x or wherey not in valid_y:
            raise ValueError(f"Invalid position. X must be in {valid_x}, Y must be in {valid_y}")

        # Only apply X anchoring if not expanded
        if not self._expand_x:
            if wherex == "left":
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, True)
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, False)
                GtkLayerShell.set_margin(self, GtkLayerShell.Edge.LEFT, 0)
            elif wherex == "right":
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, True)
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, False)
                GtkLayerShell.set_margin(self, GtkLayerShell.Edge.RIGHT, 0)
            else:  # center
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, False)
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, False)

        # Only apply Y anchoring if not expanded
        if not self._expand_y:
            if wherey == "top":
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, True)
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, False)
                GtkLayerShell.set_margin(self, GtkLayerShell.Edge.TOP, 0)
            elif wherey == "bottom":
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, True)
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, False)
                GtkLayerShell.set_margin(self, GtkLayerShell.Edge.BOTTOM, 0)
            else:  # center
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, False)
                GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, False)

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
    
    def close(self):
        self.destroy()
        return True
    
    def on_focus_lost(self, widget, event):
        """Handle focus loss event"""
        GLib.idle_add(self.destroy)  # Schedule destroy on main thread
        return False  # Allow event propagation
    
    def apply_css(self, css: str):
        """Applies CSS from a string"""
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(css.encode())
        context = self.get_style_context()
        context.add_provider_for_screen(self.get_screen(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def apply_css_file(self, path: str):
        """Applies CSS from a file"""
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(path)
        context = self.get_style_context()
        context.add_provider_for_screen(self.get_screen(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    
    def expand(self, x: bool, y: bool):
        """Autoexpands to fit the entire X or Y axis"""
        self._expand_x = x
        self._expand_y = y
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, x)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, x)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, y)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, y)
    
    @property
    def container(self):
        return self._container

    def add(self, widget):
        self.container.pack_start(widget, False, False, 0)
    
    def add_start(self, widget):
        self.container.pack_start(widget, False, False, 0)
    
    def add_end(self, widget):
        self.container.pack_end(widget, False, False, 0)
