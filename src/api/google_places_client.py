"""Google Places API client."""

import requests


class GooglePlacesClient:
    """Client for Google Places requests."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.search_url = "https://places.googleapis.com/v1/places:searchText"
        self.details_base_url = "https://places.googleapis.com/v1/places"

    def search_places(self, query: str) -> dict:
        """Search places by text query."""

        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": self.api_key,
            "X-Goog-FieldMask": "places.id,places.displayName",
        }

        body = {
            "textQuery": query,
            "languageCode": "en",
            "maxResultCount": 20,
        }

        response = requests.post(
            self.search_url,
            headers=headers,
            json=body,
        )

        response.raise_for_status()

        return response.json()

    def get_place_details(self, place_id: str) -> dict:
        """Get details for a place."""

        url = f"{self.details_base_url}/{place_id}"

        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": self.api_key,
            "X-Goog-FieldMask": "nationalPhoneNumber",
        }

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        return response.json()
