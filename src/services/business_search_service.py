"""Search businesses with Google Places."""

from src.api.google_places_client import GooglePlacesClient
from src.models.business import Business


class BusinessSearchService:
    """Search and enrich business leads."""

    CATEGORIES = [
        "restaurants",
        "cafes",
        "hotels",
        "gyms",
        "dentists",
        "clothing stores",
        "print shops",
    ]

    def __init__(self, client: GooglePlacesClient):
        self.client = client

    def search_city(self, city: str) -> list[Business]:
        """Search all supported business categories in a city."""

        businesses: list[Business] = []
        seen_place_ids: set[str] = set()

        for category in self.CATEGORIES:
            results = self.search_by_category(city, category)

            for business in results:
                if business.place_id not in seen_place_ids:
                    seen_place_ids.add(business.place_id)
                    businesses.append(business)

        return businesses

    def search_by_category(
        self,
        city: str,
        category: str,
    ) -> list[Business]:
        """Search businesses in a city by category."""

        query = f"{category} in {city}"

        data = self.client.search_places(query)

        businesses: list[Business] = []

        for place in data.get("places", []):
            place_id = place.get("id")
            name = place.get("displayName", {}).get("text")

            if place_id and name:
                businesses.append(
                    Business(
                        place_id=place_id,
                        name=name,
                        category=category,
                    )
                )

        return businesses

    def enrich_with_phone_numbers(
        self,
        businesses: list[Business],
        limit: int = 5,
    ) -> list[Business]:
        """Add phone numbers to matching businesses."""

        for business in businesses[:limit]:
            details = self.client.get_place_details(
                business.place_id
            )

            business.phone = details.get(
                "nationalPhoneNumber"
            )

        return businesses
