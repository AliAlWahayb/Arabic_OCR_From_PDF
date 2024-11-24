from math import e
import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, max_pages=1):
    input_path = os.path.abspath(input_pdf)
    file_name, file_extension = os.path.splitext(os.path.basename(input_path))

    output_paths = []

    with open(input_path, 'rb') as input_file:
        pdf_reader = PdfReader(input_file)

        total_pages = len(pdf_reader.pages)

        for start in range(0, total_pages, max_pages):
            end = min(start + max_pages, total_pages)
            output_pdf = PdfWriter()

            for page_num in range(start, end):
                output_pdf.add_page(pdf_reader.pages[page_num])

            if start == end:
                output_path = f"{file_name}_pages_{start + 1}{file_extension}"
            else:
                output_path = f"{file_name}_pages_{start + 1}-{end}{file_extension}"
                
            output_paths.append(output_path)

            os.makedirs('split', exist_ok=True)
            with open(f"split/{output_path}", 'wb') as output_file:
                output_pdf.write(output_file)

    return output_paths