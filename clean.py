import string

def clean_data(txt):
    # remove space and convert lowercase
    txt = txt.strip().lower()
    # remove special characters
    txt = str.maketrans('','', string.punctuation())
    # remove normalize
    txt = txt.split()
    # remove numeric
    txt = " ".join(ch for ch in txt if ch.isdigit())

    return txt