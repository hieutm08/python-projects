import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os

friday = pyttsx3.init()

voice = friday.getProperty('voices')

# voice[0].id: giọng nam 
# voice[1].id: giọng nữ 
friday.setProperty('voice', voice[1].id)

def speek(audio):
    print('R.O.B.E.R.T say :'+ audio)
    friday.say(audio)
    friday.runAndWait()
 
# %I: số giờ, %M: số phút %p: AM hoặc PM
def time():
    Time = datetime.datetime.now().strftime('%I:%M:%p')
    speek(Time)
    
def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speek('Good Morning sir')
    elif hour >= 12 and hour <= 18:     
        speek('Good Afternoon sir')
    elif hour >= 18 and hour <= 24:
        speek('Good Evening sir')
    speek('How can i help you?')

def command():
    c = sr.Recognizer()  # nhận diện và xử lý âm thanh thành văn bản
    with sr.Microphone() as source: # truy cập microphone mặc định
        c.pause_threshold = 2 # sau 2 giây không có âm thanh, chương trình sẽ dừng ghi âm.
        audio = c.listen(source) # bắt đầu ghi âm từ microphone (source)
    try:
        query = c.recognize_google(audio, language='en')
        print("Guest: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        query = str(input('Your order is: '))
    return query 

if __name__ == '__main__':
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speek("What should I search boss")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speek(f"Here is your {search} on google.")
        if "youtube" in query:
            speek("What should I search boss")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speek(f"Here is your {search} on youtube.")
        elif "open video" in query:
            meme = r""
            os.startfile(f"https://www.youtube.com/watch")
        elif "time" in query:
            time()
        elif "exit" in query:
            speek("Friday is qutting sir. Goodbye boss")
            quit()