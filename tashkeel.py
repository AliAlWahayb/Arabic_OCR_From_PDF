from pyarabic import araby
import arabic_reshaper
from bidi.algorithm import get_display
import mishkal.tashkeel

vocalizer = mishkal.tashkeel.TashkeelClass()

input_file_path = "LM_test.txt"
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    sentences = input_file.readlines()

for sentence in sentences:
    tashkeelWord = vocalizer.tashkeel(sentence)
    reduced = araby.reduce_tashkeel(tashkeelWord)
    output_file_path = "tashkeelWord_test.txt"

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(reduced)


print("tashkeel complete. tashkeel text saved to tashkeelWord_test.txt file.")