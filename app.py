import streamlit as st
from model_load import load_model
from translate import trans_data
from voice_speak import listen_voice
from speech_output import speech_text
from PyPDF2 import PdfReader
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image
import io

st.title("Welcom to AI Language Translater System 😊😊")

model, tokenizer = load_model()

Languages = {
    "English": "en",
    "Tamil": "ta",
    "German": "de",
    "Japanese": "ja",
    "Hindi": "hi",
    "French": "fr",
    "Arabic": "ar",
    "Russian": "ru",
    "Chinese": "zh"
}
src_lang_name = st.selectbox("Source Languages: ", list(Languages.keys()))
tgt_lang_name = st.selectbox("Target Languages: ", list(Languages.keys()))

src_lang = Languages[src_lang_name]
tgt_lang = Languages[tgt_lang_name]

uploaded_file = st.file_uploader("Upload file (txt, pdf, image)", type = ["txt", "pdf", "png", 'jpg', "jpeg"])
file_txt = ""

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        pdf_bytes = uploaded_file.read()
        reader = PdfReader(io.BytesIO(pdf_bytes))
        has_txt = False
        for page in reader.pages:
            text = page.extract_text()

            if text:
                has_txt = True
                file_txt += text
        if not has_txt:
                images = convert_from_bytes(pdf_bytes)

                for img in images:
                    file_txt += pytesseract.image_to_string(img)

    elif uploaded_file.type == "text/plain":
        file_txt = uploaded_file.read().decode("utf-8")

    elif "image" in uploaded_file.type:
        image = Image.open(uploaded_file)
        file_txt = pytesseract.image_to_string(image)

simple_txt = st.text_area("Or enter the text: ")
final_txt = file_txt if uploaded_file else simple_txt
final_txt = final_txt.strip().replace("\n", " ")

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Translate"):
    if final_txt.strip() == "":
        st.warning("Please enter the some text sentence...")
    else:
        with st.spinner("Translating..."):
            result = trans_data(final_txt, src_lang, tgt_lang, model, tokenizer)
            st.session_state.history.append((final_txt, result))

if st.button("Speak"):
    with st.spinner("Listening..."):

        voice_txt = listen_voice()

        st.write("Recognized Voice: ", voice_txt)

        result = trans_data(voice_txt, src_lang, tgt_lang, model, tokenizer)

        st.session_state.history.append((voice_txt, result))

if st.button("Audio"):
    with st.spinner("Speaking....."):

        result = trans_data(final_txt, src_lang, tgt_lang, model, tokenizer)

        st.write("Translation: ", result)

        speech_text(result, tgt_lang)

if st.button("Clear history"):
    st.session_state.history = []


for user_text, translated_text in st.session_state.history:
    st.write(f"🧑 You: {user_text[:100]}...")
    st.subheader("🌍 Translation")
    st.write(translated_text)
    st.write("---")