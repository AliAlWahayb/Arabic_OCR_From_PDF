import os
from pdf_splitter import split_pdf
from OCR_google import process_document_sample
from combine import combine_text_files
from tashkeel import harakat
from formatting_general import formatting_general
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Access variables
project_id = os.getenv('project_id') # replace with your project id
location = os.getenv('location') # replace with your location
processor_id = os.getenv('processor_id') # replace with your processor id


if __name__ == "__main__":
    input_pdf = "" # pdf path

    book_name = input_pdf.replace("PDF/", "").replace(".pdf", "")
    output_paths = split_pdf(input_pdf)

    for output_path in output_paths:
        print(f"Processing {output_path}...")

        text = process_document_sample(
            project_id=project_id,
            location=location,
            processor_id=processor_id,
            file_path=f"split/{output_path}",
            mime_type="application/pdf",
        )

        print(f"Finished Processing {output_path}")

        os.makedirs(f"output/{book_name}", exist_ok=True)
        with open(f"output/{book_name}/{output_path[:-4]}.txt", "w", encoding="utf-8") as file:
            file.write(text)

        os.remove(f"split/{output_path}")


    formatting_general(f"output/{book_name}")
    # harakat(f"output/{book_name}") # uncomment this line if you want to add tashkeel
    # combine_text_files(f"output/{book_name}", f"output/{book_name}/{book_name}.txt") # uncomment this line if you want to combine the text files
    print("All Done!")
