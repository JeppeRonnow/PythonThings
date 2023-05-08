import speech_recognition as sr

# initialize recognizer
r = sr.Recognizer()

# define function to recognize chess moves
def recognize_chess_move():
    with sr.Microphone() as source:
        print("Say your move:")
        audio = r.listen(source)

    # use Google Speech Recognition to convert audio to text
    try:
        move = r.recognize_google(audio)
        print("You said: " + move)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return None



recognize_chess_move()

