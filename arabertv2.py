# -*- coding: utf-8 -*-
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load pre-trained Arabic GPT model and tokenizer
model_name = "aubmindlab/bert-base-arabertv2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def arabic_spell_checker(text):
    # Tokenize the input text
    input_ids = tokenizer.encode(text, return_tensors="pt")

    # Generate context-sensitive predictions
    with torch.no_grad():
        outputs = model.generate(input_ids, max_length=500, num_return_sequences=1)

    # Decode the predicted text
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return corrected_text

# Example usage
input_text = 'ثم انطلق فجأة يص ـ إنَّهم أولاد تعساء, نعم نعم يا عزيزي, إنَّهم أولاد تعساء. وردد هذه العبارة مرارا في تلك السهرة: اإنَّهم أولاد تعساء). ولما أردت أن أكلمه في أمر باولين ثار حنقه وصاح يقول: ـ إنَّها بنت عقوق! بنت شريرة وعقوق! لقد لطخت شرف الأسرة! ولو كان هنالك قوانين إذن لروضتها وأذبتها. نعم نعما. . أما دي جريو فقد كان الجنرال لا يطيق أن يذكر له اسمه؛ فكان ذبحا. .. كان يقول : ـ لقد دمرني. .. جزدني من كل شيء. . كابوسي الرهيب سنتين كاملتين, كان يجثم على صدري في أحلامي أشهرا برمتها. .. إنَّه .. ولا تكلمني عنه بعد الآن قط! ولاحظت أن ثمة اتفاقا كان يتم بينهما, ولكنني صمت على عادتي لا أقول شيئا. ثم أطلعتني بلانش على ما تم اتفاقهما عليه, وكان ذلك قبل رحيلي بثمانية أيام على وجه التحديد. قالت تفضي إلي بسرها: - إنَّ للجنرال أملا في ميراث الجدة, فهي الآن مريضة حقا تنتظر منيتها من لحظة إلى أخرى. لقد أرسل إلينا مستر آستلي برقية بهذا المعنى. والجنرال هو وريثها طبعا. وهبه لم يرثها, فإنَّه لن يزعجني في شيء. فهو أولا يملك معاشه التقاعدي, وهو ثانيا سيقيم في الحجرة الَّتي تقع في آخر المنزل سعيدا بذلك كل السعادة؛ وسيكون اسمي أنا (مدام الجنرال), فأدخل المجتمع الراقي (كان ذلك حلم بلانش). وسأصبح عدا ذلك من الروس أصحاب الأطيان, لي قصر, ولي.فلاحون (موجيك), ثم يكون لي مليوني  الذي أريده! 219 '
corrected_text = arabic_spell_checker(input_text)
print(corrected_text)
