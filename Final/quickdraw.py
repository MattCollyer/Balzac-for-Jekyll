#!/usr/bin/env python3
"""

    Author: Matthew Collyer (matthewcollyer@bennington.edu)
    Date:
"""
import web
import random
from pymongo import MongoClient

render = web.template.render('templates/')

urls = (
    '/doodle/(.*)', 'answer',
    '/doodle', 'doodle'

)

app = web.application(urls, globals())
class doodle:
    def POST(self):
        return render.doodle(get_doodle())
class answer:
    def POST(self, url):
        my_input=web.input()
        guess=my_input.guess
        correct=True
        dood=get_doodle(int(url))
        if(guess.lower()!=dood['word'].lower()):
            correct=False
        update_table(int(url), guess,correct)
        return render.answer(dood,correct)


def get_doodle(key_id=None):
    """

    """
    try:
        client = MongoClient('localhost') # get our client
        db = client.quickdraw # get our database
        if(key_id==None): #if random
            total=db.qd.count()
            rando=random.randint(1,total)
            doodle=db.qd.find_one({'key_id':rando})
        else:
            doodle=db.qd.find_one({'key_id':key_id})

        return doodle
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))

def update_table(key_id,guess,correct):
    """
    Updates the d-
    if wrong: adds guess
    if right: adds +1 for right guesses

    """
    try:
        client = MongoClient('localhost') # get our client
        db = client.quickdraw # get our database
        if(correct==False):
            db.qd.update_one({'key_id':key_id},{'$push': {'human_guesses': guess}})
        else:
            db.qd.update_one({'key_id':key_id},{'$inc':{'recognized_by_human': 1}})
    except Exception as e:
        print("Unable to connect to database: {0}".format(e))



if __name__ == "__main__":
    app.run()
