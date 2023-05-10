import speech_recognition as sr

def record_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("I'm trying to hear you: ")
        audio = recognizer.listen(source)
        try:
            phrase = recognizer.recognize_google(audio, language='en')
            return phrase
        except sr.UnknownValueError:
            return "I didn't understand what you said"

if __name__ == '__main__':
    phrase = record_voice()
    with open('you_said_this.txt', 'w') as file:
        file.write(phrase)
        print('The last sentence you spoke was saved in you_said_this.txt')




        
        
        