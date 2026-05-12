import speech_recognition as sr

def listen_voice():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening.....")

            recognizer.adjust_for_ambient_noise(source,duration = 1)

            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

            print("Recognition speech....")

            text = recognizer.recognize_google(audio)

            return text
        
    except sr.UnknownValueError:
        return "Could not understand the voice"
    
    except sr.RequestError:
        return "Speech service unavailable"
    
    except Exception as e:
        return f"Error: {e}"
    
if __name__ == "__main__":
    result = listen_voice()

    print("Recognized voice: ", result)