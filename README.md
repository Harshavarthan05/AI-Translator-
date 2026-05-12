# Translator app

## Project Overview

1. This project is an transformer based and deep learning concept of the project it can translate the  any given sentence of the data, the required language can be translated(japaneses, tamil, hindi, english, german, arabic, chinese, russian, french)

2. The M2M model can be used for translate the data there some million kind of language model stored so it is easy process to access to generate the model

3. And speech recognition, and GTTS(system generate the voice to speak the data), PDF and image can process to translate the model and memory time limit is slitely medium because of cpu process takes time to run it

4. And I use streamlit to create UI frame to any user can access easily to generate the model

## Features

1. Translate text between multiple languages using AI models.

2. Convert voice input into translated text automatically.

3. Extract and translate text from PDFs and images using OCR.

4. Speak translated text with AI-generated voice output.

## Technologies Used

1. Python
2. Streamlit
3. Transformers
4. GTTS
5. Speech Recognition
6. String
7. OS
8. pytesseract
9. PDFReader

## Project Structure

translator/
|
|----app.py
|----clean.py
|----evaluation.py
|----model_load.py
|----PyAudio-0.2.14-cp31
|----README.md
|----requirments.txt
|----speech_input.py
|----speech_output.py
|----text.py
|----translate.py

## How to run project

Step 1. Create the model_load to run the model can be generate and tokenize to pretrain process
Step 2. Create the translate model and generate to give inputs to tokenize input and decode the model
Step 3. Create the preprocessing to clean the model lowercase, remove punctuation, remove numeric values
Step 4. Create the Evaluation process to check the model can run accurate to the process
Step 5. Create Speech input to generate speech recognition user can speak to translator to translate the model
Step 6. Create Speech output System can translate speech to text using GTTs model
Step 7. Create text model to run in compiler
Step 8. Create Streamlit to UI model user can understand easily

## Example

User: Hello! Good Morning
Translator: (German)- Hallo Guten Morgen

## Author

Harshavarthan B