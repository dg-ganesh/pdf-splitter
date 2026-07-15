"""
Project : PDF Splitter
Project ID : 008

Application Configuration
"""

from pathlib import Path


# ==========================================================
# Application Information
# ==========================================================

APP_NAME = "PDF Splitter"
APP_VERSION = "1.0.0"

WINDOW_TITLE = f"{APP_NAME} v{APP_VERSION}"


# ==========================================================
# Window Configuration
# ==========================================================

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 550

WINDOW_RESIZABLE = False


# ==========================================================
# Supported File Types
# ==========================================================

SUPPORTED_FILE_TYPES = [
    ("PDF Files", "*.pdf"),
]


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FOLDER = PROJECT_ROOT / "data"
INPUT_FOLDER = DATA_FOLDER / "input"
OUTPUT_FOLDER = DATA_FOLDER / "output"

ASSETS_FOLDER = PROJECT_ROOT / "assets"
ICONS_FOLDER = ASSETS_FOLDER / "icons"
IMAGES_FOLDER = ASSETS_FOLDER / "images"


# ==========================================================
# PDF Settings
# ==========================================================

PDF_EXTENSION = ".pdf"


# ==========================================================
# Application Messages
# ==========================================================

READY_MESSAGE = "Ready"

SUCCESS_TITLE = "Success"
WARNING_TITLE = "Warning"
ERROR_TITLE = "Error"


# ==========================================================
# Exported Constants
# ==========================================================

__all__ = [
    "APP_NAME",
    "APP_VERSION",
    "WINDOW_TITLE",
    "WINDOW_WIDTH",
    "WINDOW_HEIGHT",
    "WINDOW_RESIZABLE",
    "SUPPORTED_FILE_TYPES",
    "PROJECT_ROOT",
    "DATA_FOLDER",
    "INPUT_FOLDER",
    "OUTPUT_FOLDER",
    "ASSETS_FOLDER",
    "ICONS_FOLDER",
    "IMAGES_FOLDER",
    "PDF_EXTENSION",
    "READY_MESSAGE",
    "SUCCESS_TITLE",
    "WARNING_TITLE",
    "ERROR_TITLE",
]