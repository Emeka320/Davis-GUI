from datetime import datetime
import pyttsx3

engine = pyttsx3.init()
constant = ["Brush teeth", "Take a shower", "Eat breakfast"]
lectures_mon = ["GS", "CSC", "GSS", "Mat 1o1"]
lectures_tue = ["Sci", "SSt", "IT"]
lectures_wed = input('What are your lectures \n')
lectures_thu = ["CSC 1o1"]
lectures_fri = ["Sci", "SSt", "IT"]
lectures_sat = ["catch cruise"]
sun = [constant, "Go to church"]


def wochentage(t):
    wochentage = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return wochentage[t.weekday()]


if __name__ == "__main__":
    while True:
        t = datetime.today()
        wochentage(t)
        hour = datetime.now().hour
        if wochentage(t) == 'Monday':
            if 6 <= hour < 24:
                engine.say(str(constant))
                engine.say("Today is a Monday so you have only" + str(len(lectures_mon)) + "lectures")
                engine.say("They are as follows" + str(lectures_mon))
                engine.runAndWait()

        if wochentage(t) == 'Tuesday':
            if 6 <= hour < 24:
                engine.say(str(constant))
                engine.say("Today is a Tuesday so you have only" + str(len(lectures_tue)) + "lectures")
                engine.say("They are as follows" + str(lectures_tue))
                engine.runAndWait()

        if wochentage(t) == 'Wednesday':
            if 6 <= hour < 24:
                engine.say(str(constant))
                engine.say("Today is a Wednesday so you have only" + str(len(lectures_wed)) + "lectures")
                engine.say("They are as follows" + str(lectures_wed))
                engine.runAndWait()

        if wochentage(t) == 'Thursday':
            if 6 <= hour < 24:
                engine.say(str(constant))
                engine.say("Today is a Thursday so you have only" + str(len(lectures_thu)) + "lectures")
                engine.say("They are as follows" + str(lectures_thu))
                engine.runAndWait()

        if wochentage(t) == 'Friday':
            if 6 <= hour < 24:
                engine.say(str(constant))
                engine.say("Today is a Friday so you have only" + str(len(lectures_fri)) + "lectures")
                engine.say("They are as follows" + str(lectures_fri))
                engine.runAndWait()

        if wochentage(t) == 'Saturday':
            if 6 <= hour < 24:
                engine.say(str(constant))
                engine.say("Today is a Saturday so you have no lectures")
                engine.runAndWait()

        if wochentage(t) == 'Sunday':
            if 6 <= hour < 24:
                engine.say(str(sun))
                engine.runAndWait()
        break

