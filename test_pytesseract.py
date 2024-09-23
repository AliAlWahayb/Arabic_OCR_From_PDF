import os
import re
import pytesseract
from PIL import Image
from pdf2image import convert_from_path


def transform_arabic_text(text):
    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Replace non-breaking space (U+00A0) with a regular space
    text = text.replace('\u00A0', ' ')
    # Replace ellipsis (...) with three dots (...)
    text = text.replace('...', '...')
    # Replace comma (،) with their standard counterparts
    text = text.replace('،', ',')
    # Replace Arabic quotes with parentheses
    text = text.replace('»', ')').replace('«', '(')
    # Replace 'اال' with 'ال)'
    text = text.replace('اال', 'ال')

    # remove watermarks'
    text = text.replace('@ketab_n :Twitter', '')

    return text



pytesseract.pytesseract.tesseract_cmd = r"C:\Instal Hub\tesseract-OCR\tesseract.exe"


# Set the path to your input PDF file
pdf_file_path = 'PDF/المقامر رواية لـ دوستويفسكي_DONE_DONE.pdf'

pdf_file_name = os.path.basename(pdf_file_path)


# Define the directory path
output_dir = f'output/{pdf_file_name[:-4]}/'
# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Extract text from the scaled images and write to a text file
print("Extracting text from images...")

images = convert_from_path(pdf_file_path, use_cropbox=True, thread_count=4, grayscale=True)

for image in images:
    index = images.index(image)
    ocr_text = pytesseract.image_to_string(image, lang='ara')
    ocr_text = transform_arabic_text(ocr_text)
    with open(f'{output_dir}{index+1}__{pdf_file_name[:-4]}.txt', 'w', encoding='utf-8') as file:
        file.write(ocr_text + '\n')
        print(f"Extracted text from Page {index+1}.")