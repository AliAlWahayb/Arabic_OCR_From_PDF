import os
from pylibtashkeel import tashkeel

def get_diacritized_text(text):
    """
    Applies tashkeel (diacritization) to the given text.
    Handles potential UTF-8 issues and ensures the text is valid.
    """
    try:
        # Normalize text to ensure valid UTF-8 characters
        text = text.encode('utf-8').decode('utf-8')  # Re-encode to catch encoding issues
        return tashkeel(text)
    except Exception as e:
        print(f"Error during diacritization: {e}")
        return None

def clean_text(text):
    """
    Cleans the text by removing control characters and ensuring proper formatting.
    """
    import unicodedata

    # Normalize and remove control/invisible characters
    cleaned_text = ''.join(c for c in unicodedata.normalize('NFKC', text) if unicodedata.category(c)[0] != 'C')
    return cleaned_text

def harakat(folder_path):
    """
    Processes all .txt files in the given folder path and applies tashkeel.
    Overwrites files with their diacritized content.
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)

            try:
                # Read the content of the file
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Clean and process the text
                content = clean_text(content)
                diacritized_content = get_diacritized_text(content)

                if diacritized_content:
                    # Save the diacritized content into the same file
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(diacritized_content)
                else:
                    print(f"Failed to process: {filename} - Diacritized content is None.")

            except Exception as e:
                print(f"Error processing file '{filename}': {e}")
