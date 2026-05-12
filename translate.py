def trans_data(txt, src_lang, tgt_lang, model, tokenizer):

    tokenizer.src_lang = src_lang

    inputs = tokenizer(txt, return_tensors = "pt", padding = True)

    translate = model.generate(**inputs, forced_bos_token_id = tokenizer.get_lang_id(tgt_lang), num_beams = 5, max_length = 200, early_stopping = True)
    
    #decode the process to translate
    result = tokenizer.decode(translate[0], skip_special_tokens = True)

    return result