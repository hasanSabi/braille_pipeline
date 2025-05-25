def clean(text):
    text = text.replace('\n', ' ').strip()
    text = ' '.join(text.split())  # Remove extra whitespace
    return text

# Example usage:
if __name__ == "__main__":
    with open("../data/processed/ocr_output.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned = clean(raw_text)

    with open("../data/processed/ocr_cleaned.txt", "w", encoding="utf-8") as f:
        f.write(cleaned)

    print("✅ OCR text cleaned and saved.")
