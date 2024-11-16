import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk # type: ignore

class Label(Gtk.Label):
    def __init__(self, text: str):
        Gtk.Label.__init__(self, label=text)
    
    def set_text(self, text: str):
        """Sets the text of the label"""
        self.set_text(text)
    