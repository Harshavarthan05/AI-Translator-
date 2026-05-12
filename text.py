from translate import trans_data
from model_load import load_model

#taken the lang model input

model, tokenizer = load_model() 

src_lang = input("Enter the language(en, ja, hi, ta, de, zh, ru, ar, fr): ")
tgt_lang = input("Enter the languages(en, ja, hi, ta, de, zh, ru, ar, fr): ")

if model is None:
    print("Invalid language")
    exit()

while True:
    #take the input of the txt value
    txt = input("Enter the text data: ")

    if txt == "exit":
        break

    # return the result recall from the translate
    result = trans_data(src_lang, tgt_lang, txt, model, tokenizer)

    print("Translated: ", result)