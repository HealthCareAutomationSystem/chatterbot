from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
bot = ChatBot("My Bot")

convo = [
   'hello',
    'hi there !',
    'what is your name ?',
    
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    
    'In which language you talk?',
    ' I mostly talk in english',
    'What is covid-19?',
    'COVID-19 is the disease caused by a new coronavirus called SARS-CoV-2.  WHO first learned of this new virus on 31 December 2019, following a report of a cluster of cases of ‘viral pneumonia’ in Wuhan, People’s Republic of China.',
    'what are the symptoms of covid-19?',
    '''The most common symptoms of COVID-19 are

Fever
Dry cough
Fatigue
Other symptoms that are less common and may affect some patients include:

Loss of taste or smell,
Nasal congestion,
Conjunctivitis (also known as red eyes)
Sore throat,
Headache,
Muscle or joint pain,
Different types of skin rash,
Nausea or vomiting,
Diarrhea,
Chills or dizziness.
 

Symptoms of severe COVID‐19 disease include:

Shortness of breath,
Loss of appetite,
Confusion,
Persistent pain or pressure in the chest,
High temperature (above 38 °C).
Other less common symptoms are:

Irritability,
Confusion,
Reduced consciousness (sometimes associated with seizures),
Anxiety,
Depression,
Sleep disorders,
More severe and rare neurological complications such as strokes, brain inflammation, delirium and nerve damage.
People of all ages who experience fever and/or cough associated with difficulty breathing or shortness of breath, chest pain or pressure, or loss of speech or movement should seek medical care immediately. If possible, call your health care provider, hotline or health facility first, so you can be directed to the right clinic.''',
   
    'who are most at risk of severe illness from covid-19?',
    '''Some people who have had COVID-19, whether they have needed hospitalization or not, continue to experience symptoms, including fatigue, respiratory and neurological symptoms.
 ''',
    'how we can protect others and ourselves if we do not know who is infected?',
    'Stay safe by taking some simple precautions, such as physical distancing, wearing a mask, especially when distancing cannot be maintained, keeping rooms well ventilated, avoiding crowds and close contact, regularly cleaning your hands, and coughing into a bent elbow or tissue. Check local advice where you live and work. Do it all!',
    'When should i get a test for covid-19?',
    '''Anyone with symptoms should be tested, wherever possible. People who do not have symptoms but have had close contact with someone who is, or may be, infected may also consider testing – contact your local health guidelines and follow their guidance.  

While a person is waiting for test results, they should remain isolated from others. Where testing capacity is limited, tests should first be done for those at higher risk of infection, such as health workers, and those at higher risk of severe illness such as older people, especially those living in seniors’ residences or long-term care facilities.''',
    'what test should i get to see if i have covid-19?',
    '''In most situations, a molecular test is used to detect SARS-CoV-2 and confirm infection. Polymerase chain reaction (PCR) is the most commonly used molecular test. Samples are collected from the nose and/or throat with a swab. Molecular tests detect virus in the sample by amplifying viral genetic material to detectable levels. For this reason, a molecular test is used to confirm an active infection, usually within a few days of exposure and around the time that symptoms may begin. ''',
    '''what about rapid test?''',
    '''Rapid antigen tests (sometimes known as a rapid diagnostic test – RDT) detect viral proteins (known as antigens). Samples are collected from the nose and/or throat with a swab. These tests are cheaper than PCR and will offer results more quickly, although they are generally less accurate. These tests perform best when there is more virus circulating in the community and when sampled from an individual during the time they are most infectious. ''',
    'what should i do if i have covid-19 symptoms?',
    '''If you have any symptoms suggestive of COVID-19, call your health care provider or COVID-19 hotline for instructions and find out when and where to get a test, stay at home for 14 days away from others and monitor your health.

If you have shortness of breath or pain or pressure in the chest, seek medical attention at a health facility immediately. Call your health care provider or hotline in advance for direction to the right health facility.

If you live in an area with malaria or dengue fever, seek medical care if you have a fever.

If local guidance recommends visiting a medical centre for testing, assessment or isolation, wear a medical mask while travelling to and from the facility and during medical care. Also keep at least a 1-metre distance from other people and avoid touching surfaces with your hands.  This applies to adults and children.''',

]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = Tk()

main.geometry("500x650")

main.title("My Chat bot")
img = PhotoImage(file="bot1.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()
