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
    csv_path="path/to/data.csv",
    json_path="path/to/data.json",
    xlsx_path="path/to/data.xlsx"
)

converter.csv_to_json()
converter.json_to_csv()
converter.xlsx_to_json()
converter.json_to_xlsx()
```

### CLI
```bash
python converter.py --csv input.csv --json output.json

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
