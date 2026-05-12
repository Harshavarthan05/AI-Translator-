from translate import trans_data
from model_load import load_model

#testcase sentence
test_case = [
    "hello",
    "how are you",
    "i love AI",
    "what about today's topic",
    "Good morning",
    "what is your name",
    "I am interest to learn artificial intelligence"
]

model, tokenizer = load_model()

#change the language
src_lang = "en"
tgt_lang = "de"

print(f"\nTesting language: {src_lang} -> {tgt_lang}\n")

#run the evaluation
for txt in test_case:
    res = trans_data(src_lang,tgt_lang, txt, model, tokenizer)

    print("input : ", txt)
    print("result : ", res)
    print("-"*40)