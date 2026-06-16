"""Business lead model."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Business:
    """Business found through Google Places."""

    place_id: str
    name: str
    category: str
    phone: Optional[str] = None
