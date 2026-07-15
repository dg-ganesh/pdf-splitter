"""
Project : PDF Splitter
Project ID : 008

UI Event Handlers
"""

from pathlib import Path
import customtkinter as ctk

from src.services.file_service import FileService
from src.services.pdf_service import PDFService
from src.core.pdf_splitter import PDFSplitter


class EventHandlers:
    """
    Handles all UI events.
    """

    @staticmethod
    def browse_pdf(widgets: dict) -> None:
        """
        Handles PDF Browse button click.
        """

        pdf_path = FileService.browse_pdf()

        if pdf_path is None:
            return

        widgets["pdf_entry"].delete(0, ctk.END)
        widgets["pdf_entry"].insert(0, str(pdf_path))

        try:

            pdf_info = PDFService.get_pdf_info(pdf_path)

            widgets["file_name_value"].configure(
                text=pdf_info.file_name
            )

            widgets["pages_value"].configure(
                text=str(pdf_info.page_count)
            )

            widgets["size_value"].configure(
                text=f"{pdf_info.file_size_mb} MB"
            )

            EventHandlers.set_status(
                widgets,
                "PDF loaded successfully."
            )

        except Exception as ex:

            widgets["file_name_value"].configure(text="-")
            widgets["pages_value"].configure(text="-")
            widgets["size_value"].configure(text="-")

            EventHandlers.set_status(
                widgets,
                f"Error: {str(ex)}"
            )

    @staticmethod
    def browse_output_folder(widgets: dict) -> None:
        """
        Handles Output Folder Browse button click.
        """

        folder = FileService.browse_output_folder()

        if folder is None:
            return

        widgets["output_entry"].delete(0, ctk.END)
        widgets["output_entry"].insert(0, str(folder))

        EventHandlers.set_status(
            widgets,
            "Output folder selected."
        )

    @staticmethod
    def split_pdf(widgets: dict) -> None:
        """
        Handles Split PDF button click.
        """

        try:

            pdf_file = Path(
                widgets["pdf_entry"].get()
            )

            output_folder = Path(
                widgets["output_entry"].get()
            )

            method = widgets["split_method"].get()

            # --------------------------------------------
            # Disable Split Button
            # --------------------------------------------

            widgets["split_button"].configure(
                state="disabled"
            )

            EventHandlers.set_status(
                widgets,
                "Splitting PDF..."
            )

            # Force the UI to repaint
            widgets["status_label"].update_idletasks()
            widgets["split_button"].update_idletasks()

            # --------------------------------------------
            # Split Logic
            # --------------------------------------------

            if method == "individual":

                count = PDFSplitter.split_individual_pages(
                    pdf_file,
                    output_folder
                )

            elif method == "range":

                start_page = int(
                    widgets["start_entry"].get()
                )

                end_page = int(
                    widgets["end_entry"].get()
                )

                count = PDFSplitter.split_page_range(
                    pdf_file,
                    output_folder,
                    start_page,
                    end_page
                )

            elif method == "extract":

                pages = widgets["extract_entry"].get()

                count = PDFSplitter.extract_pages(
                    pdf_file,
                    output_folder,
                    pages
                )

            elif method == "every":

                pages_per_file = int(
                    widgets["every_entry"].get()
                )

                count = PDFSplitter.split_every(
                    pdf_file,
                    output_folder,
                    pages_per_file
                )

            else:

                raise ValueError(
                    "Invalid split method selected."
                )

            # --------------------------------------------
            # Success
            # --------------------------------------------

            EventHandlers.set_status(
                widgets,
                f"Successfully created "
                f"{count} PDF file(s)."
            )

            FileService.open_folder(
                output_folder
            )

        except Exception as ex:

            EventHandlers.set_status(
                widgets,
                f"Error: {str(ex)}"
            )

        finally:

            widgets["split_button"].configure(
                state="normal"
            )

    @staticmethod
    def open_output_folder(widgets: dict) -> None:
        """
        Opens the selected output folder.
        """

        folder = widgets["output_entry"].get()

        if folder.strip():

            FileService.open_folder(
                Path(folder)
            )

    @staticmethod
    def set_status(
        widgets: dict,
        message: str
    ) -> None:
        """
        Updates the status label.
        """

        widgets["status_label"].configure(
            text=f"Status : {message}"
        )

        widgets["status_label"].update_idletasks()