"""
Project : PDF Splitter
Project ID : 008

Main Application Window
"""

import customtkinter as ctk

from src.ui.widgets import WidgetFactory
from src.ui.event_handlers import EventHandlers


class MainWindow(ctk.CTk):
    """
    Main application window.
    """

    def __init__(self):
        super().__init__()

        self.widgets = WidgetFactory.create_widgets(self)

        self._layout_widgets()
        self._bind_events()

    # =====================================================
    # Layout
    # =====================================================

    def _layout_widgets(self):
        """
        Arrange all widgets on the window.
        """

        row = 0

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        self.widgets["title_label"].grid(
            row=row,
            column=0,
            columnspan=3,
            pady=(15, 20)
        )

        row += 1

        # -------------------------------------------------
        # PDF Selection
        # -------------------------------------------------

        self.widgets["pdf_label"].grid(
            row=row,
            column=0,
            padx=10,
            sticky="w"
        )

        row += 1

        self.widgets["pdf_entry"].grid(
            row=row,
            column=0,
            padx=(10, 5),
            pady=5,
            sticky="ew"
        )

        self.widgets["browse_pdf_button"].grid(
            row=row,
            column=1,
            padx=(5, 10),
            pady=5
        )

        row += 1

        # -------------------------------------------------
        # PDF Information
        # -------------------------------------------------

        info = self.widgets["info_frame"]

        info.grid(
            row=row,
            column=0,
            columnspan=2,
            padx=10,
            pady=15,
            sticky="ew"
        )

        self.widgets["file_name_label"].grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

        self.widgets["file_name_value"].grid(
            row=0,
            column=1,
            sticky="w"
        )

        self.widgets["pages_label"].grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

        self.widgets["pages_value"].grid(
            row=1,
            column=1,
            sticky="w"
        )

        self.widgets["size_label"].grid(
            row=2,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )

        self.widgets["size_value"].grid(
            row=2,
            column=1,
            sticky="w"
        )

        row += 1

        # -------------------------------------------------
        # Split Options
        # -------------------------------------------------

        split = self.widgets["split_frame"]

        split.grid(
            row=row,
            column=0,
            columnspan=2,
            padx=10,
            pady=10,
            sticky="ew"
        )

        self.widgets["individual_radio"].grid(
            row=0,
            column=0,
            sticky="w",
            padx=10,
            pady=5
        )

        self.widgets["range_radio"].grid(
            row=1,
            column=0,
            sticky="w",
            padx=10,
            pady=5
        )

        self.widgets["start_entry"].grid(
            row=1,
            column=1,
            padx=5
        )

        self.widgets["end_entry"].grid(
            row=1,
            column=2,
            padx=5
        )

        self.widgets["extract_radio"].grid(
            row=2,
            column=0,
            sticky="w",
            padx=10,
            pady=5
        )

        self.widgets["extract_entry"].grid(
            row=2,
            column=1,
            columnspan=2,
            padx=5,
            sticky="ew"
        )

        self.widgets["every_radio"].grid(
            row=3,
            column=0,
            sticky="w",
            padx=10,
            pady=5
        )

        self.widgets["every_entry"].grid(
            row=3,
            column=1,
            padx=5,
            sticky="w"
        )

        row += 1

        # -------------------------------------------------
        # Output Folder
        # -------------------------------------------------

        self.widgets["output_label"].grid(
            row=row,
            column=0,
            padx=10,
            sticky="w"
        )

        row += 1

        self.widgets["output_entry"].grid(
            row=row,
            column=0,
            padx=(10, 5),
            pady=5,
            sticky="ew"
        )

        self.widgets["browse_output_button"].grid(
            row=row,
            column=1,
            padx=(5, 10),
            pady=5
        )

        row += 1

        # -------------------------------------------------
        # Split Button
        # -------------------------------------------------

        self.widgets["split_button"].grid(
            row=row,
            column=0,
            columnspan=2,
            pady=20
        )

        row += 1

        # -------------------------------------------------
        # Status
        # -------------------------------------------------

        self.widgets["status_label"].grid(
            row=row,
            column=0,
            columnspan=2,
            padx=10,
            pady=(5, 15),
            sticky="w"
        )

        self.columnconfigure(0, weight=1)

    # =====================================================
    # Event Binding
    # =====================================================

    def _bind_events(self):
        """
        Connect widget events to handlers.
        """

        self.widgets["browse_pdf_button"].configure(
            command=lambda:
            EventHandlers.browse_pdf(self.widgets)
        )

        self.widgets["browse_output_button"].configure(
            command=lambda:
            EventHandlers.browse_output_folder(
                self.widgets
            )
        )

        self.widgets["split_button"].configure(
            command=lambda:
            EventHandlers.split_pdf(
                self.widgets
            )
        )