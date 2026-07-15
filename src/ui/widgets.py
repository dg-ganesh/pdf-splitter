"""
Project : PDF Splitter
Project ID : 008

UI Widget Factory
"""

import customtkinter as ctk

from src.config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    READY_MESSAGE
)


class WidgetFactory:
    """
    Creates all widgets required by the main window.
    """

    @staticmethod
    def create_widgets(window):

        widgets = {}

        # --------------------------------------------------
        # Window
        # --------------------------------------------------

        window.title("PDF Splitter")
        window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        window.resizable(False, False)

        # --------------------------------------------------
        # Title
        # --------------------------------------------------

        widgets["title_label"] = ctk.CTkLabel(
            window,
            text="PDF Splitter",
            font=("Arial", 22, "bold")
        )

        # --------------------------------------------------
        # PDF Selection
        # --------------------------------------------------

        widgets["pdf_label"] = ctk.CTkLabel(
            window,
            text="PDF File"
        )

        widgets["pdf_entry"] = ctk.CTkEntry(
            window,
            width=420
        )

        widgets["browse_pdf_button"] = ctk.CTkButton(
            window,
            text="Browse"
        )

        # --------------------------------------------------
        # PDF Information
        # --------------------------------------------------

        widgets["info_frame"] = ctk.CTkFrame(window)

        widgets["file_name_label"] = ctk.CTkLabel(
            widgets["info_frame"],
            text="File Name :"
        )

        widgets["file_name_value"] = ctk.CTkLabel(
            widgets["info_frame"],
            text="-"
        )

        widgets["pages_label"] = ctk.CTkLabel(
            widgets["info_frame"],
            text="Pages :"
        )

        widgets["pages_value"] = ctk.CTkLabel(
            widgets["info_frame"],
            text="-"
        )

        widgets["size_label"] = ctk.CTkLabel(
            widgets["info_frame"],
            text="Size :"
        )

        widgets["size_value"] = ctk.CTkLabel(
            widgets["info_frame"],
            text="-"
        )

        # --------------------------------------------------
        # Split Method
        # --------------------------------------------------

        widgets["split_method"] = ctk.StringVar(
            value="individual"
        )

        widgets["split_frame"] = ctk.CTkFrame(window)

        widgets["individual_radio"] = ctk.CTkRadioButton(
            widgets["split_frame"],
            text="Individual Pages",
            variable=widgets["split_method"],
            value="individual"
        )

        widgets["range_radio"] = ctk.CTkRadioButton(
            widgets["split_frame"],
            text="Page Range",
            variable=widgets["split_method"],
            value="range"
        )

        widgets["start_entry"] = ctk.CTkEntry(
            widgets["split_frame"],
            width=60,
            placeholder_text="From"
        )

        widgets["end_entry"] = ctk.CTkEntry(
            widgets["split_frame"],
            width=60,
            placeholder_text="To"
        )

        widgets["extract_radio"] = ctk.CTkRadioButton(
            widgets["split_frame"],
            text="Extract Pages",
            variable=widgets["split_method"],
            value="extract"
        )

        widgets["extract_entry"] = ctk.CTkEntry(
            widgets["split_frame"],
            width=250,
            placeholder_text="1-5,8,10"
        )

        widgets["every_radio"] = ctk.CTkRadioButton(
            widgets["split_frame"],
            text="Every N Pages",
            variable=widgets["split_method"],
            value="every"
        )

        widgets["every_entry"] = ctk.CTkEntry(
            widgets["split_frame"],
            width=60,
            placeholder_text="N"
        )

        # --------------------------------------------------
        # Output Folder
        # --------------------------------------------------

        widgets["output_label"] = ctk.CTkLabel(
            window,
            text="Output Folder"
        )

        widgets["output_entry"] = ctk.CTkEntry(
            window,
            width=420
        )

        widgets["browse_output_button"] = ctk.CTkButton(
            window,
            text="Browse"
        )

        # --------------------------------------------------
        # Action
        # --------------------------------------------------

        widgets["split_button"] = ctk.CTkButton(
            window,
            text="Split PDF",
            width=180
        )

        # --------------------------------------------------
        # Status
        # --------------------------------------------------

        widgets["status_label"] = ctk.CTkLabel(
            window,
            text=f"Status : {READY_MESSAGE}",
            anchor="w"
        )

        return widgets