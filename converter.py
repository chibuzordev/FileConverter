# -*- coding: utf-8 -*-
import pandas as pd
import csv
import json
import xlsxwriter

class FileConverter:
    def __init__(self, csv_path: str, json_path: str, xlsx_path: Optional[str] = None, config_path: Optional[str] = None):
        self.csv_path = csv_path
        self.json_path = json_path
        self.xlsx_path = xlsx_path
        self.config_path = config_path
        self.schema = self._load_config() if config_path else None

    def _load_config(self) -> Optional[Dict]:
        if self.config_path:
            with open(self.config_path, 'r') as file:
                return yaml.safe_load(file)
        return None

    def _parse_row(self, row: pd.Series, schema: Dict) -> Dict:
        result = {}
        for key, value in schema.items():
            if isinstance(value, dict):
                if 'column' in value:
                    col_val = row.get(value['column'], None)
                    if pd.notna(col_val):
                        if 'delimiter' in value:
                            result[key] = [x.strip() for x in str(col_val).split(value['delimiter'])]
                        else:
                            result[key] = col_val
                    else:
                        result[key] = None
                else:
                    result[key] = self._parse_row(row, value)
            else:
                result[key] = row.get(value, None) if pd.notna(row.get(value, None)) else None
        return result

    def csv_to_json(self):
        df = pd.read_csv(self.csv_path)
        if self.schema and self.schema.get('mode') == 'structured':
            schema_fields = self.schema.get('fields', {})
            data = [self._parse_row(row, schema_fields) for _, row in df.iterrows()]
        else:
            data = df.to_dict(orient="records")

        with open(self.json_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"✅ JSON saved to: {self.json_path}")

    def xlsx_to_json(self):
        if not self.xlsx_path:
            raise ValueError("Excel file path is not set.")

        xl = pd.ExcelFile(self.xlsx_path)
        all_chunks = []

        for sheet_name in xl.sheet_names:
            df = xl.parse(sheet_name)
            if self.schema and self.schema.get('mode') == 'structured':
                schema_fields = self.schema.get('fields', {})
                for _, row in df.iterrows():
                    parsed = self._parse_row(row, schema_fields)
                    parsed['section'] = sheet_name
                    all_chunks.append(parsed)
            else:
                df['section'] = sheet_name
                all_chunks.extend(df.to_dict(orient="records"))

        with open(self.json_path, 'w') as f:
            json.dump(all_chunks, f, indent=4)

        print(f"✅ Combined JSON saved from Excel to: {self.json_path}")

    def json_to_csv(self, delimiter: str = ','):
        with open(self.json_path, 'r') as json_file:
            data = json.load(json_file)

        if isinstance(data, dict):
            data = [data]

        df = pd.json_normalize(data)
        df.to_csv(self.csv_path, index=False, sep=delimiter)

        print(f"✅ CSV file created at: {self.csv_path}")

    def json_to_xlsx(self):
        with open(self.json_path, 'r') as f:
            data = json.load(f)

        section_groups = {}
        for row in data:
            section = row.get("section", "Unknown")
            section_groups.setdefault(section, []).append(row)

        if not self.xlsx_path:
            raise ValueError("Excel file path is not set.")

        with pd.ExcelWriter(self.xlsx_path, engine='xlsxwriter') as writer:
            for section, rows in section_groups.items():
                df = pd.json_normalize(rows)
                safe_sheet = str(section)[:31].replace('/', '_')
                df.to_excel(writer, sheet_name=safe_sheet, index=False)

        print(f"✅ Multi-sheet Excel saved to: {self.xlsx_path}")
