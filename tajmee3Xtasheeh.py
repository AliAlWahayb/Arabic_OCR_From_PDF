import os
import re
from ghalatawi.autocorrector import AutoCorrector

autoco = AutoCorrector()

# Path to the folder containing the text files
folder_path = "output/ktabpdf.com_الجرائم_الأبجدية"

# Output file where the combined content will be saved
output_file = f"{folder_path}/corrected_files.txt"

# Function to combine text files after autocorrecting the file names
def combine_files_with_autocorrect(folder_path, output_file):
    with open(output_file, "w", encoding="utf-8") as outfile:
        file_names = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
        file_names_sorted = sorted(file_names, key=lambda x: [int(num) for num in re.findall(r'\d+', x)])
        for file_name in file_names_sorted:
            if file_name.endswith(".txt"):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, "r", encoding="utf-8") as infile:
                    content = infile.read()
                    content = content.replace("إنَّى", "إنَّي")
                    content = content.replace("صفحتَّى", "صفحتَّي")
                    content = autoco.adjust_typo(autoco.adjust_typo(autoco.spell(content)))
                    Page_number = re.findall(r'\d+', file_name)
                    Page_number = ''.join(Page_number)
                    outfile.write(f"Page#{Page_number}\n")
                    outfile.write(content)
                    outfile.write("\n\n")

# Example usage
combine_files_with_autocorrect(folder_path, output_file)
print("Text files autocorrected and combined successfully!")