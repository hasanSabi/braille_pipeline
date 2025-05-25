import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

input_dir = r"C:/Users/SAGEER/Desktop/braille_pipeline/data/raw/"
output_dir = r"C:/Users/SAGEER/Desktop/braille_pipeline/data/processed/"
os.makedirs(output_dir, exist_ok=True)

all_text = []

for file in os.listdir(input_dir):
    if file.lower().endswith((".jpg", ".png")):
        img_path = os.path.join(input_dir, file)
        img = Image.open(img_path)
        text = pytesseract.image_to_string(img)
        all_text.append(text)

with open(os.path.join(output_dir, "ocr_output.txt"), "w", encoding="utf-8") as f:
    f.write("\n---\n".join(all_text))

print("✅ OCR completed for images.")
