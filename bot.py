import datetime, time
import random

def get_ans(req):
    req = req.lower()

    if 'hello' in req or 'hi' in req:
        return "Hello! Have a good day!"
    elif 'time' in req:
        now = datetime.datetime.now()
        return "It's %s:%s" % (now.hour, now.minute)
    elif 'day' in req:
        return time.ctime()
    elif 'how' in req and 'you' in req:
        return "I can'r be better now!"
    elif 'weather' in req:
        return "It's sunny and cloudy!"
    elif 'temperature' in req:
        return "It's about 20 degrees"
    elif 'where' in req and 'you' in req:
        return "I'm from ITMO!"
    else:
        return "I'm so pleasure to talk with you!"

list_random = ["How are you?",
                "What's your name?",
                "Where are you?",
                "Hello, what can i help you?"]

def chatting():
    return random.choice(list_random)


