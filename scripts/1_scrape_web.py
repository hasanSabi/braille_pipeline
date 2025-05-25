import requests
from bs4 import BeautifulSoup
import os

urls = [
    "https://en.wikipedia.org/wiki/Braille",
    "https://www.geeksforgeeks.org/introduction-to-django/",
    "https://www.bbc.com/news/science-environment-56901261",
    "https://www.tutorialspoint.com/artificial_intelligence/index.htm",
    "https://www.who.int/news-room/questions-and-answers/item/blindness-and-vision-impairment",
    "https://www.nature.com/articles/d41586-022-00753-z",
    "https://opensource.com/article/20/5/python-ocr",
    "https://en.wikipedia.org/wiki/Screen_reader",
    "https://en.wikipedia.org/wiki/Optical_character_recognition",
    "https://en.wikipedia.org/wiki/Assistive_technology"
]

output_dir = r"C:/Users/SAGEER/Desktop/braille_pipeline/data/processed/"
os.makedirs(output_dir, exist_ok=True)

for i, url in enumerate(urls, start=1):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)
    
    with open(os.path.join(output_dir, f"web_page_{i}.txt"), 'w', encoding='utf-8') as f:
        f.write(text)

print("✅ Web scraping complete: 10 pages saved.")
