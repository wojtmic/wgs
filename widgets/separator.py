import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk # type: ignore

class Separator(Gtk.Separator):
    def __init__(self, orientation: Gtk.Orientation):
        Gtk.Separator.__init__(self, orientation=orientation)
    
    def set_size(self, width: int, height: int):
        """Sets the size of the separator"""
        self.set_size_request(width, height)
        
    def set_orientation(self, orientation: Gtk.Orientation):
        """Sets the orientation of the separator"""
        self.set_orientation(orientation)
