# Med-Safe1

Python application for managing drug-drug interactions with a user-friendly interface using Streamlit.

![Python](https://img.shields.io/badge/python-3.x-blue)
![Coverage](https://img.shields.io/badge/coverage-87%25-brightgreen)

## Features
- Search drug interactions
- Load data from CSV
- User-friendly Streamlit interface
- Drug interaction warnings and information

## Requirements
- Python 3.8+

## Dependencies
- `streamlit` - Web interface framework
- `pandas` - CSV data processing
- `pytest` - Testing framework
- `pytest-cov` - Test coverage reporting

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Med-Safe1.git
cd Med-Safe1
```

2. Create and activate virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install streamlit pandas pytest pytest-cov
```

## Usage

Run the Streamlit app:
```bash
streamlit run checker.py
```

## Data Setup
Place drug interaction CSV file in the project directory.

CSV Structure:
- Column A: DDInterID_A (ID for Drug A)
- Column B: Drug_A (Drug A name)
- Column C: DDInterID_B (ID for Drug B)
- Column D: Drug_B (Drug B name)
- Column E: Level (Interaction severity: Minor, Moderate, etc.)

## Running Tests
```bash
pytest --cov=. --cov-report=html
```

View coverage report:
```bash
start htmlcov/index.html
```

## Project Structure
```
Med-Safe1/
├── checker.py              # Main Streamlit application
├── drug_interaction.csv    # CSV data files
├── tests/                  # Test files
├── requirements.txt        # Dependencies
└── README.md
```

## Test Pairs
- Phenylpropanolamine, Linagliptin
- Theophylline, Aminoglutethimide
- Salmeterol, Rilpivirine