#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "sysadgui.ui"


class SysadguiApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("frame1", master)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = SysadguiApp(root)
    app.run()
