from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

def load_model():
    model_name = "facebook/m2m100_418M"
    tokenizer = M2M100Tokenizer.from_pretrained(model_name)
    model = M2M100ForConditionalGeneration.from_pretrained(model_name)

    tokenizer.src_lang = 'en'

    return model, tokenizer