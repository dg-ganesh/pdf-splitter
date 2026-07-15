"""
Project : PDF Splitter
Project ID : 008

PDF Information Model
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class PDFInfo:
    """
    Represents the metadata of a selected PDF document.
    """

    file_path: Path
    page_count: int
    file_size: int

    @property
    def file_name(self) -> str:
        """Returns the PDF file name."""
        return self.file_path.name

    @property
    def file_stem(self) -> str:
        """Returns the PDF file name without extension."""
        return self.file_path.stem

    @property
    def file_extension(self) -> str:
        """Returns the PDF file extension."""
        return self.file_path.suffix

    @property
    def parent_folder(self) -> Path:
        """Returns the folder containing the PDF."""
        return self.file_path.parent

    @property
    def file_size_kb(self) -> float:
        """Returns the file size in KB."""
        return round(self.file_size / 1024, 2)

    @property
    def file_size_mb(self) -> float:
        """Returns the file size in MB."""
        return round(self.file_size / (1024 * 1024), 2)