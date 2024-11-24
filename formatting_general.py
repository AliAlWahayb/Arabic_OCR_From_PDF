import os


def clean_arabic_text(text):
    """
    Cleans Arabic text by correcting numbers, punctuation, and common spelling errors.
    """
    corrections = [
        # Numbers (Arabic to English)
        ("١", "1"), ("٢", "2"), ("٣", "3"), ("٤", "4"), ("٥", "5"),
        ("٦", "6"), ("٧", "7"), ("٨", "8"), ("٩", "9"), ("٠", "0"),

        # Punctuation (Arabic to English)
        ("«", '"'), ("»", '"'),

        # Common spelling errors
        ("اخطىء", "اخطئ"), ("يبدىء", "يبدأ"),
        ("يقرىء", "يقرأ"), ("سيؤىء", "سيؤيد"),
        ("نبدىء", "نبدأ"), ("يسمىء", "يسمو"),
        ("يخطىء", "يخطئ"), ("ينشىء", "ينشئ"),
        ("يقضىء", "يقضي"), ("يرجىء", "يرجئ"),
        ("سيأتىء", "سيأتي"), ("يخطىء", "يخطئ"),
        ("بدأىء", "بدأ"), ("قرىء", "قرأ"),
        ("يسمىء", "يسمى"), ("يتدفىء", "يتدفأ"),
        ("ملجىء", "ملجأ"), ("يفترىء", "يفتري"),
        ("يخشىء", "يخشى"), ("سينشىء", "سينشئ"),
        ("مبدىء", "مبدأ"), ("يتطوىء", "يتطوى"),
        ("مأوىء", "مأوى"), ("تجربىء", "تجربة"),
        ("يجزىء", "يجزي"), ("ينهىء", "ينهي"),
        ("يخلىء", "يخلي"), ("تقربىء", "تقربة"),
        ("يبنىء", "يبني"), ("ترجىء", "ترجئ"),
        ("ينبئء", "ينبئ"), ("يشرىء", "يشري"),
        ("يعطىء", "يعطي"), ("ينهىء", "ينهي"),
        ("يزدرىء", "يزدري"), ("يستدلىء", "يستدل"),
        ("مجلىء", "مجلى"), ("يتربىء", "يتربى"),
        ("يسعىء", "يسعى"), ("يجلىء", "يجلي"),
        ("تبدىء", "تبدأ"), ("يرضىء", "يرضى"),
        ("يحلَىء", "يحلي"), ("يقتضىء", "يقتضي"),
        ("يطمأنَىء", "يطمئن"), ("يستعلىء", "يستعلي"),
        ("يقترىء", "يقترى"),

        # remove
        ("ཙ", ""), ("\n", " "),("  ", " "),("   ", " "),("•", ""),

    ]

    for wrong, correct in corrections:
        text = text.replace(wrong, correct)

    return text


def open_and_clean(file_path, output_path):
    """
    Removes specific characters and formats text in the given file, 
    saving the cleaned output to the specified output path.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    text = clean_arabic_text(text)

    # Write cleaned text to the output file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text)


def formatting_general(folder_path):
    """
    Processes all .txt files in the specified folder by removing specific characters.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, f"{filename}")
            open_and_clean(file_path, output_path)
