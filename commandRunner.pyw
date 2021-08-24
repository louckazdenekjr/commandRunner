#!/usr/bin/python
# -*- coding: utf-8 -*-

import gi
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class mainwindow(Gtk.Window):

    def __init__(self):
        
        Gtk.Window.__init__(self, title="commandRunner")
        Gtk.Window.set_default_size(self, 200,100)
        Gtk.Window.set_resizable(self, False)
        Gtk.Window.set_position(self, Gtk.WindowPosition.CENTER)

        box1 = Gtk.VButtonBox(spacing=10)

        self.entry = Gtk.Entry()
        self.entry.set_alignment(xalign=0.5)

        button1 = Gtk.Button.new_with_mnemonic("Run")
        button1.connect("clicked", self.whenbutton1_clicked)
        button1.set_property("width-request", 300)
		
        box1.pack_start(self.entry, True, True, 0)
        box1.pack_start(button1, True, True, 0)
        box1.set_border_width(20)

        self.add(box1)
        
    def whenbutton1_clicked(self, button):
        bashCommand=self.entry.get_text() 
        output = subprocess.check_output(['bash','-c', bashCommand])
    
window = mainwindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
