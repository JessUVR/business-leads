# Business Leads

A Python application that searches local businesses using the Google Places API and exports the results to Excel.

## Features

- Search businesses by category.
- Retrieve business names and phone numbers.
- Export results to Excel.
- Modular and object-oriented architecture.

---

## Technologies

- Python
- Google Places API
- OpenPyXL

---

## Configuration

Create a `config.py` file in the project root:

```python
GOOGLE_API_KEY = "YOUR_API_KEY"
```

> **Note:** Never commit your API key to GitHub.

---

## Usage

Run the application:

```bash
python main.py
```

The application will:

- Search businesses by category.
- Retrieve available phone numbers.
- Display the results.
- Optionally export them to an Excel file.

---

## Project Structure

```text
business-leads/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── api/
│   │   └── google_places_client.py
│   │
│   ├── exporters/
│   │   └── excel_exporter.py
│   │
│   ├── models/
│   │   └── business.py
│   │
│   └── services/
│       └── business_search_service.py
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Architecture

```text
Google Places API
        │
        ▼
GooglePlacesClient
        │
        ▼
BusinessSearchService
        │
        ▼
Business Model
        │
        ▼
Excel Exporter
```

---

## Future Improvements

- Export directly to Google Sheets.
- Add CSV export.
- Support multiple search locations.
- Build a lightweight CRM workflow.
- Add unit tests.
