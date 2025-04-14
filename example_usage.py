# example_usage.py

from converter import FileConverter

# Define file paths
csv_file = "data.csv"
json_file = "data.json"
xlsx_file = "data.xlsx"

# Create an instance of the converter
converter = FileConverter(
    csv_path=csv_file,
    json_path=json_file,
    xlsx_path=xlsx_file
)

# Convert CSV to JSON
converter.csv_to_json()

# Convert JSON to CSV
converter.json_to_csv()

# Convert XLSX to JSON
converter.xlsx_to_json()

# Convert JSON to XLSX
converter.json_to_xlsx()
