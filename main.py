"""
Project : PDF Splitter
Project ID : 008

Application Entry Point
"""

import customtkinter as ctk

from src.ui.main_window import MainWindow


def main() -> None:
    """
    Application entry point.
    """

    # --------------------------------------------------
    # CustomTkinter Configuration
    # --------------------------------------------------

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # --------------------------------------------------
    # Create Main Window
    # --------------------------------------------------

    app = MainWindow()

    # --------------------------------------------------
    # Start Application
    # --------------------------------------------------

    app.mainloop()


if __name__ == "__main__":
    main()