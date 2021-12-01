from datetime import datetime

from playsound import playsound
from translate import Translator
import pytz
from gtts import gTTS

tzDhaka = pytz.timezone('Asia/Dhaka')
datetimeBD = datetime.now(tzDhaka)
EngText = "Bangladesh time is : "
EngTime = datetimeBD.strftime("%I:%M:%S %p")
BText = Translator(from_lang='English', to_lang='Bengali')
BTranslation_text = BText.translate(EngText)
print(BTranslation_text + EngTime)

CBHour = EngTime[0:2]
CBMinute = EngTime[3:5]
CBSecond = EngTime[6:8]



"""
#This part hasn't been working for me, the audio is stored but isn't played T^T

BHour = Translator(from_lang='English', to_lang='Bengali')
BTranslation_Hour = BHour.translate(CBHour)
BMinute = Translator(from_lang='English', to_lang='Bengali')
BTranslation_Minute= BMinute.translate(CBMinute)

BTimeLoud = gTTS(text="এখন সময়" + BTranslation_Hour + "টা বেজে" + BTranslation_Minute + "মিনিট", lang='bn')
BTimeLoud.save("TimeInBangla.wav")
playsound('C:/Users/Nadia/Desktop/bleh/TimeInBangla.mp3', False)
"""



def validateTime(alarmTime):
    if len(alarmTime) != 11:
        return "ভুল ইনপুট ফরম্যাট! অনুগ্রহপূর্বক আবার চেষ্টা করুন"
    elif int(alarmTime[0:2]) > 12:
        return "ঘন্টার ফরম্যাট ভুল ! অনুগ্রহপূর্বক আবার চেষ্টা করুন"
    elif int(alarmTime[3:5]) > 59:
        return "মিনিটের ফরম্যাট ভুল ! অনুগ্রহপূর্বক আবার চেষ্টা করুন"
    elif int(alarmTime[6:8]) > 59:
        return "সেকেণডের ফরম্যাট ভুল ! অনুগ্রহপূর্বক আবার চেষ্টা করুন"
    else:
        return "আগুসার হচ্ছে"


while True:
    print("নিচে এই ফরম্যাটে অ্যালার্ম সেট করার সময় লিখুন: HH:MM:SS AM/PM : \n")

    BStartLoud = gTTS(text="নিচে এই ফরম্যাটে অ্যালার্ম সেট করার সময় লিখুন", lang='bn')
    BStartLoud.save("good.mp3")
    playsound('C:/Users/Nadia/Desktop/bleh/good.mp3')

    alarmTime = input()

    validate = validateTime(alarmTime.lower())
    if validate != "আগুসার হচ্ছে":
        print(validate)
    else:
        print(f"{alarmTime} টার জন্য অ্যালার্ম দেয়া হলো...")
        break

alarmHour = alarmTime[0:2]
alarmMinute = alarmTime[3:5]
alarmSecond = alarmTime[6:8]
alarmPeriod = alarmTime[9:11].upper()

# print("Setting up alarm...")

while True:
    now = datetime.now(tzDhaka)
    currentHour = now.strftime("%I")
    currentMinute = now.strftime("%M")
    currentSeconds = now.strftime("%S")
    currentPeriod = now.strftime("%p")

    if alarmPeriod == currentPeriod:
        if alarmHour == currentHour:
            if alarmMinute == currentMinute:
                if alarmSecond == currentSeconds:
                    print("ওঠে পরুন!")

                    BLoud = gTTS(text="সময় শেষ। এখন ওঠে পরুন!", lang='bn')
                    BLoud.save("good3.mp3")
                    playsound('C:/Users/Nadia/Desktop/bleh/good3.mp3')
                    #line below is to add any additional sound you want...
                    #playsound('C:/Users/Nadia/Desktop/bleh/Instrumental-techno.mp3')
                    break
