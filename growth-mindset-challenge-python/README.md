# Data Sweeper

Data Sweeper is a Python app that cleans, visualizes, and converts CSV/Excel files.  It offers duplicate removal, missing value filling, and basic bar chart visualizations.

## Features

- Upload CSV/Excel files.
- Remove duplicates.
- Fill missing values.
- Visualize data with bar charts.
- Convert between CSV and Excel formats.

## Installation (using uv)

1. Install Python 3.7+ (if needed).
2. Create and activate a virtual environment:
    ```bash
    uv venv .venv  # Create the environment
    source .venv/bin/activate  # Activate (macOS/Linux)
    .venv\Scripts\activate  # Activate (Windows)
    ```
3. Install dependencies:
    ```bash
    uv pip install streamlit pandas openpyxl
    ```

## Usage

1. Run the app: `streamlit run app.py`
2. Open in your browser: `http://localhost:8501`
3. Upload your file.
4. Use the cleaning and visualization options.
5. Convert and download the file.

## Technologies

- Python
- Streamlit
- Pandas
- Openpyxl

## Author

GitHub: Arsalan4work