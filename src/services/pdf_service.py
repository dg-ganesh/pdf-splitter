"""
Project : PDF Splitter
Project ID : 008

PDF Service
"""

from pathlib import Path

from pypdf import PdfReader, PdfWriter

from src.models.pdf_info import PDFInfo


class PDFService:
    """
    Provides PDF read and write operations.
    """

    @staticmethod
    def get_pdf_info(file_path: Path) -> PDFInfo:
        """
        Reads a PDF and returns its metadata.

        Args:
            file_path: Path to the PDF file.

        Returns:
            PDFInfo
        """

        reader = PdfReader(file_path)

        return PDFInfo(
            file_path=file_path,
            page_count=len(reader.pages),
            file_size=file_path.stat().st_size
        )

    @staticmethod
    def load_reader(file_path: Path) -> PdfReader:
        """
        Loads and returns a PdfReader instance.

        Args:
            file_path: Path to the PDF file.

        Returns:
            PdfReader
        """

        return PdfReader(file_path)

    @staticmethod
    def save_pdf(
        reader: PdfReader,
        page_numbers: list[int],
        output_file: Path
    ) -> None:
        """
        Saves the specified pages to a new PDF.

        Args:
            reader: Source PdfReader.
            page_numbers: Zero-based page numbers.
            output_file: Output PDF path.
        """

        writer = PdfWriter()

        for page_number in page_numbers:
            writer.add_page(reader.pages[page_number])

        with output_file.open("wb") as pdf_file:
            writer.write(pdf_file)