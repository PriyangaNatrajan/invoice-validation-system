##  Project Overview

This project implements a Python-based invoice validation system that processes structured invoice data and performs multiple validation checks.

The system identifies inconsistencies, missing values, arithmetic mismatches, and statistical outliers, and generates a structured validation report.

## Validation Checks Implemented

The system performs the following validations:

1. **Missing Value Detection**
   - Identifies null or corrupted entries in any column.

2. **Field Consistency Validation**
   - Checks if due_date is earlier than invoice_date.

3. **Cross-Field Validation**
   - Validates whether:
     - `subtotal = qty × unit_price`

4. **Total Amount Reconciliation**
   - Validates whether:
     - `total_amount = subtotal + tax_amount`
   - Uses a tolerance value for floating-point comparison.

5. **Negative Value Detection**
   - Flags rows with negative quantity.

6. **Statistical Outlier Detection**
   - Uses IQR (Interquartile Range) method to detect abnormal values in `qty`.


## Project Structure

invoice-validation-system/
│
├── data/
│ └── sample_invoices.csv
│
├── reports/
│ └── validation_report.json
│
├── notebooks/
│ └── eda.ipynb
│
├── src/
│ ├── config.py
│ ├── data_loader.py
│ ├── data_cleaning.py
│ ├── validators.py
│ ├── outlier_detection.py
│ ├── report_generator.py
│ └── main.py
│
├── requirements.txt
└── README.md

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd invoice-validation-system
2.  Create Virtual Environment
Windows:

python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

->> Running the Project
From the project root directory:
python src/main.py

Output
After execution:

Validation report is generated at:

reports/validation_report.json
The report contains structured details of detected issues:

[
    {
        "invoice_id": "INV002",
        "row_index": 1,
        "issue": "Due date is before invoice date"
    }
]

EDA (Exploratory Data Analysis)
EDA is provided in:

notebooks/eda.ipynb
It includes:

Missing value analysis

Distribution plots

Outlier visualization

Correlation matrix

Business rule sanity checks

Statistical Reasoning
IQR method is used for outlier detection due to robustness against skewed financial data.

A tolerance value is used during total reconciliation to avoid floating-point precision issues.

Corrupted numeric entries are coerced to NaN to ensure pipeline robustness.

Dependencies

pandas

numpy

matplotlib

seaborn

// Author
Priyanga N
CIT – Data Science