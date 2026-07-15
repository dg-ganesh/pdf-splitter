"""
Project : PDF Splitter
Project ID : 008

PDF Splitter
"""

from pathlib import Path

from src.core.page_parser import PageParser
from src.core.pdf_validator import PDFValidator
from src.services.file_service import FileService
from src.services.pdf_service import PDFService


class PDFSplitter:
    """
    Provides business logic for splitting PDF documents.
    """

    @staticmethod
    def split_individual_pages(
        pdf_file: Path,
        output_folder: Path
    ) -> int:
        """
        Splits every page into a separate PDF.

        Returns:
            Number of PDF files created.
        """

        PDFValidator.validate_pdf_file(pdf_file)
        PDFValidator.validate_output_folder(output_folder)

        pdf_info = PDFService.get_pdf_info(pdf_file)
        PDFValidator.validate_pdf_info(pdf_info)

        FileService.create_folder(output_folder)

        reader = PDFService.load_reader(pdf_file)

        for page in range(pdf_info.page_count):

            output_file = output_folder / (
                f"{pdf_info.file_stem}_Page_{page + 1}.pdf"
            )

            PDFService.save_pdf(
                reader,
                [page],
                output_file
            )

        return pdf_info.page_count

    @staticmethod
    def split_page_range(
        pdf_file: Path,
        output_folder: Path,
        start_page: int,
        end_page: int
    ) -> int:
        """
        Creates a PDF containing the specified page range.

        Returns:
            Number of PDF files created.
        """

        PDFValidator.validate_pdf_file(pdf_file)
        PDFValidator.validate_output_folder(output_folder)

        pdf_info = PDFService.get_pdf_info(pdf_file)

        PDFValidator.validate_page_range(
            start_page,
            end_page,
            pdf_info.page_count
        )

        FileService.create_folder(output_folder)

        reader = PDFService.load_reader(pdf_file)

        pages = PageParser.parse_range(
            start_page,
            end_page,
            pdf_info.page_count
        )

        output_file = output_folder / (
            f"{pdf_info.file_stem}_{start_page}-{end_page}.pdf"
        )

        PDFService.save_pdf(
            reader,
            pages,
            output_file
        )

        return 1

    @staticmethod
    def extract_pages(
        pdf_file: Path,
        output_folder: Path,
        page_selection: str
    ) -> int:
        """
        Extracts selected pages into a new PDF.

        Example:
            1,3,8
            1-5,8,10-12

        Returns:
            Number of PDF files created.
        """

        PDFValidator.validate_pdf_file(pdf_file)
        PDFValidator.validate_output_folder(output_folder)

        pdf_info = PDFService.get_pdf_info(pdf_file)

        FileService.create_folder(output_folder)

        reader = PDFService.load_reader(pdf_file)

        pages = PageParser.parse(
            page_selection,
            pdf_info.page_count
        )

        output_file = output_folder / (
            f"{pdf_info.file_stem}_Extract.pdf"
        )

        PDFService.save_pdf(
            reader,
            pages,
            output_file
        )

        return 1

    @staticmethod
    def split_every(
        pdf_file: Path,
        output_folder: Path,
        pages_per_file: int
    ) -> int:
        """
        Splits the PDF every N pages.

        Returns:
            Number of PDF files created.
        """

        PDFValidator.validate_pdf_file(pdf_file)
        PDFValidator.validate_output_folder(output_folder)

        pdf_info = PDFService.get_pdf_info(pdf_file)

        PDFValidator.validate_pages_per_file(
            pages_per_file
        )

        FileService.create_folder(output_folder)

        reader = PDFService.load_reader(pdf_file)

        page_groups = PageParser.split_every(
            pdf_info.page_count,
            pages_per_file
        )

        file_count = 0

        for index, pages in enumerate(page_groups, start=1):

            output_file = output_folder / (
                f"{pdf_info.file_stem}_Part_{index}.pdf"
            )

            PDFService.save_pdf(
                reader,
                pages,
                output_file
            )

            file_count += 1

        return file_count