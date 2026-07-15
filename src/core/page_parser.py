"""
Project : PDF Splitter
Project ID : 008

Page Parser
"""

from typing import List


class PageParser:
    """
    Parses user-specified page selections.
    """

    @staticmethod
    def parse(page_text: str, total_pages: int) -> List[int]:
        """
        Parses a page selection string.

        Examples:
            1-5
            1,3,8
            1-3,7,10-12

        Args:
            page_text: User entered page selection.
            total_pages: Total pages in the PDF.

        Returns:
            Sorted list of unique zero-based page numbers.

        Raises:
            ValueError: If the page selection is invalid.
        """

        if not page_text.strip():
            raise ValueError("Page selection cannot be empty.")

        pages = set()

        sections = page_text.split(",")

        for section in sections:

            section = section.strip()

            if "-" in section:

                start_text, end_text = section.split("-", maxsplit=1)

                if not start_text.isdigit() or not end_text.isdigit():
                    raise ValueError(f"Invalid page range: {section}")

                start = int(start_text)
                end = int(end_text)

                if start > end:
                    raise ValueError(f"Invalid page range: {section}")

                if start < 1 or end > total_pages:
                    raise ValueError(
                        f"Page range {section} is outside the document."
                    )

                for page in range(start, end + 1):
                    pages.add(page - 1)

            else:

                if not section.isdigit():
                    raise ValueError(f"Invalid page number: {section}")

                page = int(section)

                if page < 1 or page > total_pages:
                    raise ValueError(
                        f"Page number {page} is outside the document."
                    )

                pages.add(page - 1)

        return sorted(pages)

    @staticmethod
    def parse_range(
        start_page: int,
        end_page: int,
        total_pages: int
    ) -> List[int]:
        """
        Parses a start/end page range.

        Returns:
            Zero-based page numbers.
        """

        if start_page < 1 or end_page < 1:
            raise ValueError("Page numbers must be greater than zero.")

        if start_page > end_page:
            raise ValueError("Start page cannot be greater than end page.")

        if end_page > total_pages:
            raise ValueError("Page range exceeds document length.")

        return list(range(start_page - 1, end_page))

    @staticmethod
    def split_every(
        total_pages: int,
        pages_per_file: int
    ) -> List[List[int]]:
        """
        Splits the document into groups of pages.

        Example:
            total_pages = 10
            pages_per_file = 3

        Returns:
            [
                [0,1,2],
                [3,4,5],
                [6,7,8],
                [9]
            ]
        """

        if pages_per_file <= 0:
            raise ValueError(
                "Pages per file must be greater than zero."
            )

        groups = []

        for start in range(0, total_pages, pages_per_file):

            end = min(start + pages_per_file, total_pages)

            groups.append(list(range(start, end)))

        return groups