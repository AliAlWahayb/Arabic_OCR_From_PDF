from ghalatawi.autocorrector import AutoCorrector
autoco = AutoCorrector()

input_file_path = "LM_test.txt"

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    sentences = input_file.readlines()


for sentence in sentences:
    corrected_sentences = autoco.spell(sentence)
    corrected_sentences = autoco.adjust_typo(sentence)


    output_file_path = "Corrector_text.txt"

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(corrected_sentences)


print("Correction complete. Corrected text saved to Corrector_test.txt file.")
