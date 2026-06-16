"""Command-line entry point for generating business leads."""

from config import GOOGLE_PLACES_API_KEY
from api.google_places_client import GooglePlacesClient
from services.business_search_service import BusinessSearchService
from exporters.excel_exporter import ExcelExporter


def main() -> None:
    print("=" * 40)
    print("Business Leads Generator")
    print("=" * 40)

    city = input("\nEnter city: ")

    client = GooglePlacesClient(GOOGLE_PLACES_API_KEY)
    service = BusinessSearchService(client)
    exporter = ExcelExporter()

    businesses = service.search_city(city)

    print(f"\nBusinesses found: {len(businesses)}")
    print("Getting phone numbers...")

    businesses = service.enrich_with_phone_numbers(
        businesses,
        limit=len(businesses),
    )

    export_choice = input("\nExport results to Excel? (y/n): ").strip().lower()

    if export_choice == "y":
        file_path = "data/processed/business_leads.xlsx"

        exporter.export(
            businesses=businesses,
            file_path=file_path,
        )

        print(f"\nExport completed: {file_path}")
    else:
        print("\nExport skipped.")

    print("\nDone.")


if __name__ == "__main__":
    main()
