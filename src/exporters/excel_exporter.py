"""Excel export helpers."""

import pandas as pd

from src.models.business import Business


class ExcelExporter:
    """Export business leads to Excel."""

    def export(
        self,
        businesses: list[Business],
        file_path: str,
    ) -> None:
        """Export businesses to an Excel file."""

        rows = []

        for business in businesses:
            rows.append(
                {
                    "Name": business.name,
                    "Phone": business.phone,
                    "Category": business.category,
                    "Place ID": business.place_id,
                }
            )

        df = pd.DataFrame(rows)

        df.to_excel(file_path, index=False)
