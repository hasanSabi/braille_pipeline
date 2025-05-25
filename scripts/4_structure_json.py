import json
import os

output_file = r"C:/Users/SAGEER/Desktop/braille_pipeline/data/processed/structured_data.json"

paragraphs = []

with open(r"C:/Users/SAGEER/Desktop/braille_pipeline/data/processed/ocr_output.txt", "r", encoding="utf-8") as f:
    text = f.read()

for para in text.split('. '):  # Basic split by sentence/paragraph
    if para.strip():
        paragraphs.append({
            "text": para.strip(),
            "metadata": {
                "source": "ocr_scanned",
                "page": None
            }
        })

structured = {
    "id": "doc_001",
    "paragraphs": paragraphs
}

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(structured, f, indent=2)

print("✅ JSON structure created.")
