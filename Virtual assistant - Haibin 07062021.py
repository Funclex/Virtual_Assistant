"""
---NLP Virtual Assistant Sandwich Project---扶海滨 20210607---
功能： 智能语音助手，可回答基本问题
1. 建议使用python3.6版本环境。
2. 必装3个基础库 SpeechRecognition / pyttsx3 / pyAudio
3. 助手名称可更换，功能可自定义增加 (如实时语言翻译，朗读pdf等)
Haibin FU – Bournemouth University
hfu@bournemouth.ac.uk
"""

import speech_recognition as sr  #语音识别 （可离线）- pip install SpeechRecognition
import pyttsx3                   #文字语音转换库 （可离线） - pip install pyttsx3
import pywhatkit                 #基本问题反馈 - pip install pywhatkit
import datetime
import wikipedia                 #维基百科 - pip install wikipedia
import pyjokes                   #笑话 - pip install pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:#麦克风作为声音输入设备
            print('listening...please say command')      #提示可开始说话
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'sandwich' in command:     #可更换为任何名称
                command = command.replace('sandwich', '')
                print(command)
    except:
        pass
    return command

def run_sandwich():
    command = take_command()
    print(command)
    if 'play' in command:           #播放音乐功能
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:         #报时功能
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:       #搜人功能
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'creator' in command: #自定义功能
        talk('Haibin Fu is my creator')
    elif 'joke' in command:         #讲笑话功能
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

print("已为您开启语音助手 running sandwich...")
while True:
    run_sandwich()

