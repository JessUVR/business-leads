"""Application configuration."""

import os

from dotenv import load_dotenv

load_dotenv()

GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

if not GOOGLE_PLACES_API_KEY:
    raise ValueError(
        "GOOGLE_PLACES_API_KEY was not found. "
        "Please add it to your .env file."
    )
