from ghalatawi.autocorrector import AutoCorrector
autoco = AutoCorrector()

input_file_path = "output/المقامر رواية لـ دوستويفسكي_PDF/66__المقامر رواية لـ دوستويفسكي.txt"

with open(input_file_path, 'r', encoding='utf-8') as input_file:
    sentences = input_file.readlines()


for sentence in sentences:
    corrected_sentences = autoco.spell(sentence)
    corrected_sentences = autoco.adjust_typo(corrected_sentences)


    output_file_path = "Corrector_text.txt"

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(corrected_sentences)


print("Correction complete. Corrected text saved to Corrector_test.txt file.")
