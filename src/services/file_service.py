"""
Project : PDF Splitter
Project ID : 008

File Service
"""

from pathlib import Path
import os
import subprocess
import tkinter as tk
from tkinter import filedialog

from src.config import SUPPORTED_FILE_TYPES


class FileService:
    """
    Provides file and folder related operations.
    """

    @staticmethod
    def browse_pdf() -> Path | None:
        """
        Displays a file selection dialog for choosing a PDF.

        Returns:
            Path | None
        """

        root = tk.Tk()
        root.withdraw()

        filename = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=SUPPORTED_FILE_TYPES
        )

        root.destroy()

        if not filename:
            return None

        return Path(filename)

    @staticmethod
    def browse_output_folder() -> Path | None:
        """
        Displays a folder selection dialog.

        Returns:
            Path | None
        """

        root = tk.Tk()
        root.withdraw()

        folder = filedialog.askdirectory(
            title="Select Output Folder"
        )

        root.destroy()

        if not folder:
            return None

        return Path(folder)

    @staticmethod
    def file_exists(file_path: Path) -> bool:
        """
        Checks whether the specified file exists.
        """

        return file_path.is_file()

    @staticmethod
    def folder_exists(folder_path: Path) -> bool:
        """
        Checks whether the specified folder exists.
        """

        return folder_path.is_dir()

    @staticmethod
    def create_folder(folder_path: Path) -> None:
        """
        Creates a folder if it does not already exist.
        """

        folder_path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def get_file_size(file_path: Path) -> int:
        """
        Returns the file size in bytes.
        """

        return file_path.stat().st_size

    @staticmethod
    def open_folder(folder_path: Path) -> None:
        """
        Opens the specified folder in Windows Explorer.
        """

        if not folder_path.exists():
            return

        if os.name == "nt":
            os.startfile(folder_path)
        else:
            subprocess.run(["xdg-open", str(folder_path)], check=False)