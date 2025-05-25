# Braille AI Data Pipeline

## Objective
Convert unstructured data (images and web text) into structured JSON for Braille AI.

## Tools Used
- Python, Tesseract OCR, BeautifulSoup

## Steps

### 1. Collection
- Collected 10 web pages and 5 image scans.

### 2. Extraction
- Used BeautifulSoup for web scraping.
- Used Tesseract OCR for images.

### 3. Cleaning
- Removed noisy characters, normalized spacing.

### 4. Structuring
- Output in JSON with paragraph-wise metadata.

## Output
- `structured_data.json`
