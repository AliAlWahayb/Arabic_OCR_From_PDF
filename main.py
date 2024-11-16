import os
from pdf_splitter import split_pdf
from OCR_google import process_document_sample
from combine import combine_text_files, combine_text_files_to_word


if __name__ == "__main__":
    input_pdf = "" # path to pdf
    book_name = input_pdf.replace("PDF/", "").replace(".pdf", "")
    output_paths = split_pdf(input_pdf)

    for output_path in output_paths:
        print(f"Processing {output_path}...")

        text = process_document_sample(
            project_id="" ,# replace with your google document ai project id
            location="", # replace with your google document ai location
            processor_id="", # replace with your google document ai processor id
            file_path=f"split/{output_path}",
            mime_type="application/pdf",
        )

        print(f"Finished Processing {output_path}")

        print(f"Saving {output_path}")

        os.makedirs(f"output/{book_name}", exist_ok=True)
        with open(f"output/{book_name}/{output_path[:-4]}.txt", "w", encoding="utf-8") as file:
            file.write(text)

        print(f"Finished Saving {output_path}")

        print(f"Deleting {output_path}")

        os.remove(f"split/{output_path}")

        print(f"Finished Deleting {output_path}")

        print(f"Done with {output_path}")

    
    combine_text_files(f"output/{book_name}", f"output/{book_name}/{book_name}.txt")
    print("All Done!")

