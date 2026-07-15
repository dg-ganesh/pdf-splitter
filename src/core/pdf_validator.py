"""
Project : PDF Splitter
Project ID : 008

PDF Validator
"""

from pathlib import Path

from src.models.pdf_info import PDFInfo


class PDFValidator:
    """
    Provides validation methods for PDF operations.
    """

    @staticmethod
    def validate_pdf_file(file_path: Path) -> None:
        """
        Validates the selected PDF file.

        Args:
            file_path: Path to the PDF.

        Raises:
            ValueError: If validation fails.
        """

        if file_path is None:
            raise ValueError("Please select a PDF file.")

        if not file_path.exists():
            raise ValueError("The selected file does not exist.")

        if not file_path.is_file():
            raise ValueError("The selected path is not a file.")

        if file_path.suffix.lower() != ".pdf":
            raise ValueError("Only PDF files are supported.")

    @staticmethod
    def validate_output_folder(folder_path: Path) -> None:
        """
        Validates the output folder.

        Args:
            folder_path: Output folder.

        Raises:
            ValueError: If validation fails.
        """

        if folder_path is None:
            raise ValueError("Please select an output folder.")

        if not folder_path.exists():
            raise ValueError("The output folder does not exist.")

        if not folder_path.is_dir():
            raise ValueError("The selected output location is not a folder.")

    @staticmethod
    def validate_pdf_info(pdf_info: PDFInfo) -> None:
        """
        Validates PDF metadata.

        Args:
            pdf_info: PDF information model.

        Raises:
            ValueError: If validation fails.
        """

        if pdf_info.page_count <= 0:
            raise ValueError("The PDF does not contain any pages.")

        if pdf_info.file_size <= 0:
            raise ValueError("The PDF file is empty.")

    @staticmethod
    def validate_page_number(
        page_number: int,
        total_pages: int
    ) -> None:
        """
        Validates a single page number.

        Args:
            page_number: Page number (1-based).
            total_pages: Total number of pages.

        Raises:
            ValueError: If validation fails.
        """

        if page_number < 1:
            raise ValueError("Page number must be greater than zero.")

        if page_number > total_pages:
            raise ValueError(
                f"Page number cannot exceed {total_pages}."
            )

    @staticmethod
    def validate_page_range(
        start_page: int,
        end_page: int,
        total_pages: int
    ) -> None:
        """
        Validates a page range.

        Args:
            start_page: First page.
            end_page: Last page.
            total_pages: Total pages in the PDF.

        Raises:
            ValueError: If validation fails.
        """

        PDFValidator.validate_page_number(
            start_page,
            total_pages
        )

        PDFValidator.validate_page_number(
            end_page,
            total_pages
        )

        if start_page > end_page:
            raise ValueError(
                "Start page cannot be greater than end page."
            )

    @staticmethod
    def validate_pages_per_file(
        pages_per_file: int
    ) -> None:
        """
        Validates the 'split every N pages' value.

        Args:
            pages_per_file: Number of pages per output PDF.

        Raises:
            ValueError: If validation fails.
        """

        if pages_per_file <= 0:
            raise ValueError(
                "Pages per file must be greater than zero."
            )