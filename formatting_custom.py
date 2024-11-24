import os
import re

def open_and_clean(file_path, output_path):
    """
    Removes specific characters and formats text in the given file, 
    saving the cleaned output to the specified output path.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()


    # Remove page numbers
    text = re.sub(r'\s*\d+\s*$', '', text)

    # the custom formatting for each book
    text = text.replace('•', '')
    text = text.replace('', '')
    text = text.replace('', '')


    # Write cleaned text to the output file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text)


def formatting_custom(folder_path):
    """
    Processes all .txt files in the specified folder by removing specific characters.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, f"{filename}")
            open_and_clean(file_path, output_path)
