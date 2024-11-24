# Arabic OCR from PDF

This project provides a Python-based solution to extract Arabic text from PDF documents using Google Document AI. It processes PDFs to generate formatted `.txt` files containing the extracted text.

## Features

- **Arabic Text Extraction**: Utilizes Google Document AI to accurately extract Arabic text from PDF files.
- **Formatted Output**: Saves the extracted text into well-structured `.txt` files for easy readability and further processing.
- **Tashkeel Support**: Adds diacritical marks (Tashkeel) to the extracted Arabic text for enhanced readability.

## Requirements

Ensure the following dependencies are installed:

- `pylibtashkeel`
- `google-cloud-documentai`
- `PyPDF2`

Install these dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

*Note*: Ensure that you have access to Google Document AI and have set up the necessary authentication credentials.

## Usage

1. **Set Up Google Document AI Credentials**: Follow the [Google Cloud documentation](https://cloud.google.com/document-ai/docs/setup) to set up authentication and obtain your credentials.

2. **Run the Scripts**:
   - Use `main.py` to extract text from PDF files. The extracted and formatted text will be saved as `.txt` files in the specified output directory.
   - If you want to **add Tashkeel**, format the text, and combine it, use `step2.py`.

3. **Configure the Scripts**:
   - Specify the path to your input PDF file in `main.py`.

## Output

- **Text Files**: `.txt` files containing the extracted Arabic text, formatted for readability and ease of use.

## Example

Here's how to set the input PDF path and output directory in the scripts:

```python
# Set the path to the input PDF file in main.py
input_pdf = '/path/to/your/input.pdf'

# Run step2.py to add Tashkeel and format the text
```

After running the scripts, the extracted and processed text files will be saved in the specified output directory.

## Notes

- Ensure that your Google Cloud credentials are correctly set up and that you have the necessary permissions to use Document AI.
- The script is designed to handle PDFs containing Arabic text. For other languages, adjust the Document AI settings accordingly.

For more details and updates, visit the [GitHub repository](https://github.com/AliAlWahayb/Arabic_OCR_From_PDF).
