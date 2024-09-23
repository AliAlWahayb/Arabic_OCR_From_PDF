import re
import time
from datetime import datetime, timedelta
import ocrspace
import os
from pdf2image import convert_from_path
from io import BytesIO
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

the_api_key = os.getenv('API_KEY')

api = ocrspace.API(api_key=the_api_key,
                   language=ocrspace.Language.Arabic, scale=True)


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
    # replace تجيثه with تجيئه
    text = text.replace('تجيثه', 'تجيئه')
    # replace القارىء with القارئ
    text = text.replace('القارىء', 'القارئ')
    # replace إن with إنَّ
    text = text.replace('إن', 'إنَّ')
    # replace للحاق with للَّحاق
    text = text.replace('للحاق', 'لِلَّحاق')
    # replace التي with الَّتي
    text = text.replace('التي', 'الَّتي')
    # replace أنه with أنَّه
    text = text.replace('أنه', 'أنَّه')
    # replace إنه with إنَّه
    text = text.replace('إنه', 'إنَّه')
    # replace أنها with أنَّها
    text = text.replace('أنها', 'أنَّها')
    # replace إنها with إنَّها
    text = text.replace('إنها', 'إنَّها')
    # replace أنهم with أنَّهم
    text = text.replace('أنهم', 'أنَّهم')
    # replace أنهن with أنَّهن
    text = text.replace('أنهن', 'أنَّهن')
    # replace أنهما with أنَّهما
    text = text.replace('أنهما', 'أنَّهما')
    # replace إنهما with إنَّهما
    text = text.replace('إنهما', 'إنَّهما')
    # replace أنهنا with أنَّهنا
    text = text.replace('أنهنا', 'أنَّهنَّا')
    # replace قائلا  with قائلاً
    text = text.replace('قائلا', 'قائلاً')
    # replace حتى   with حتَّى
    text = text.replace('حتى', 'حتَّى')
    # replace سينه    with سيئه
    text = text.replace('سينه', 'سيئه')
    # replace الكئاب     with الكتاب
    text = text.replace('الكئاب', 'الكتاب')
    # replace إنَّنى     with إنَّني
    text = text.replace('إنَّنى', 'إنَّني')
    # remove watermarks'
    text = text.replace('@ketab_n :Twitter', '')

    return text


def Api_limit(api_calls, max_calls_per_hour):
    if api_calls == max_calls_per_hour:
        print("API rate limit reached. Waiting for 1 hour...")
        time.sleep(3600)  # 1 hour
        api_calls = 0
        print("Resuming extraction...")


def process_page(page, index):

    print(f"Processing page {index+1}")
    try:
        ocr_text = api.ocr_file(page)
    except Exception as e:
        print(f"Error processing page {index+1}: {e}")
        current_time = datetime.now()
        next_hour = (current_time.replace(minute=0, second=0, microsecond=0) +
                     timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')
        print(
            f"API rate limit reached. Waiting until the next hour at {next_hour}...")
        time.sleep((((current_time.replace(minute=0, second=0, microsecond=0) +
                   timedelta(hours=1) - current_time).total_seconds())+120))
        print("Resuming extraction...")
        ocr_text = api.ocr_file(page)

    ocr_text = transform_arabic_text(ocr_text)

    with open(f'{output_dir}{index+1}__{pdf_file_name[:-4]}.txt', 'w', encoding='utf-8') as file:
        file.write(ocr_text + '\n')
        print(f"Extracted text from Page {index+1}.")


def split_and_process_pdf(pdf_file_path):
    print('convert to image...')
    images = convert_from_path(pdf_file_path, use_cropbox=True, thread_count=4)
    print('convert Done!')
    # api_calls = 0

    for image in images:

        output_pdf_path = f"temp_img.png"  # Define the path to save the current page
        image.save(output_pdf_path, "PNG")

        # Process the current page
        process_page(output_pdf_path, images.index(image))

        # # Introduce a delay between API calls to stay within rate limits
        # Api_limit(api_calls, 179)
        # api_calls += 1
        # Delete the temporary file after processing if needed
        os.remove(output_pdf_path)

    print("split and process Done!")


# Set the path to your input PDF file
pdf_file_path = 'PDF/المقامر رواية لـ دوستويفسكي-7-9_DONE_DONE.pdf'

pdf_file_name = os.path.basename(pdf_file_path)

# Define the directory path
output_dir = f'output/{pdf_file_name[:-4]}/'
# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Extract text from the scaled images and write to a text file
print("Extracting text from images...")

split_and_process_pdf(pdf_file_path)


# Create the new file name with "done" appended
new_pdf_file_path = os.path.join(os.path.dirname(
    pdf_file_path), os.path.splitext(pdf_file_name)[0] + '_DONE.pdf')
# Rename the PDF file
os.rename(pdf_file_path, new_pdf_file_path)

print("Extracting Done!")


#   File "C:\Users\alisa\Documents\gethubfiles\Arabic_OCR_From_PDF\venv\lib\site-packages\ocrspace\main.py", line 55, in _parse
#     raise Exception(raw)
# Exception: You may only perform this action upto maximum 180 number of times within 3600 seconds
