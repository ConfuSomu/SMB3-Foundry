#!/usr/bin/env python3
import os
import sys

from PySide2.QtWidgets import QApplication

# change into the tmp directory pyinstaller uses for the data
if hasattr(sys, "_MEIPASS"):
    print(f"Changing current dir to {getattr(sys, '_MEIPASS')}")
    os.chdir(getattr(sys, "_MEIPASS"))

from foundry.gui.MainWindow import MainWindow


def main():
    app = QApplication()
    MainWindow()
    app.exec_()


if __name__ == "__main__":
    main()