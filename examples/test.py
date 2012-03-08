from gi.repository import Gtk

w = Gtk.Window()
w.connect('destroy', lambda x: Gtk.main_quit())
b = Gtk.Button("Click Me")
w.add(b)
w.show_all()

Gtk.main()
