# -*- coding: utf-8 -*-
import re
import time
from unittest import skip
import openai
import os

# Set the base URL and API key for the OpenAI client
openai.api_base = "http://localhost:1234/v1"
openai.api_key = "not-needed"

def api_response(text):

# إنشاء كود التفاعل
    system = """
    حسناً. أريد فقط تصحيح الأخطاء الإملائية في النص العربي دون أي إضافات أو تحديثات أخرى بدون تغيير او تبديل اي كلمه.
    """

    user_input = text


    promot = user_input + "\n" + "صحح كل الاغلاط الاملائية" 

    # Create a chat completion
    completion = openai.ChatCompletion.create(
        model="local-model",  # this field is currently unused
        temperature=0,
        
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": promot}
        ],
        request_timeout=100,
        timeout=100,
        
    )

    # Print the chatbot's response
    # print(completion.choices[0].message.content)


    # # Write the chatbot's response to a file
    # with open(f'LM_test_tasheeh.txt', 'w', encoding='utf-8') as file:
    #     file.write(completion.choices[0].message.content)
    #     print(f"LM_test_tasheeh.txt created successfully")

    return completion.choices[0].message.content

# Path to the folder containing the text files
folder_path = "output/ktabpdf.com_الجرائم_الأبجدية"

output_dir = f'{folder_path}/tasheeh/'
# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)


# Function to combine text files based on name order
def tasheeh_text_files(folder_path,skipTo):
    file_names = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    file_names_sorted = sorted(file_names, key=lambda x: [int(num) for num in re.findall(r'\d+', x)])
    
    for file_name in file_names_sorted:
        if file_names_sorted.index(file_name) < skipTo:
            print(f"Skipping to file: {skipTo}")
            continue
        print(f"start tasheeh text from file {file_name}.")
        with open(os.path.join(folder_path, file_name), "r", encoding="utf-8") as infile:
            with open(f'{folder_path}/tasheeh/{file_name[:-4]}_tasheeh.txt', 'w', encoding='utf-8') as file:
                try:
                    text = api_response(infile.read())
                except Exception as e:
                    print(f"Error processing file {file_name}: {e}")
                    print("Waiting for 2 seconds...")
                    time.sleep(2)
                    print("Retrying...")
                    text = api_response(infile.read())

                file.write(text)
                print(f"done tasheeh text from file {file_name}.")
                time.sleep(1)

               
# Example usage
skipTo = 0
tasheeh_text_files(folder_path,skipTo)
print("tasheeh Done!")




