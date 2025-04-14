# 📊 FileConverter

A lightweight Python utility for converting between Excel (.xlsx), CSV, and structured JSON formats.

## 🚀 Features
- Convert CSV ↔ JSON
- Convert Excel (multi-sheet) ↔ JSON
- Cleanly structured JSON with metadata support
- Intelligent handling of missing fields and formatting
- Command-line interface (CLI) support

---

## 🧩 Installation on Collab
```bash

pip install -r requirements.txt
```

On Colab
```bash
!git clone https://github.com/chibuzordev/FileConverter

import os
os.chdir("FileConverter")

!pip install -r requirements.txt
```

---

## 🛠 Usage

### Python (Programmatic)
```python
from converter import FileConverter

converter = FileConverter(
    csv_path="data.csv",
    json_path="data.json",
    xlsx_path="data.xlsx"
)

converter.csv_to_json()
converter.json_to_csv()
converter.xlsx_to_json()
converter.json_to_xlsx()
```

### CLI
```bash
python cli.py --csv data.csv --json data.json --csv2json
python cli.py --json data.json --csv data.csv --json2csv
python cli.py --xlsx data.xlsx --json data.json --xlsx2json
python cli.py --json data.json --xlsx data.xlsx --json2xlsx
```

---

## 📁 File Structure
```bash
.
├── cli.py                # Command-line entrypoint
├── converter.py          # Core FileConverter class
├── requirements.txt
├── README.md
└── setup.py
```

---

## 🧠 Notes
- Metadata fields like `tags` must be `;` separated in CSV.
- Excel export uses sheet names based on `section` values.

---

## 📜 License
MIT License
