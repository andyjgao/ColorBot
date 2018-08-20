# -*- coding: utf-8 -*-
import requests
from meya import Component
import random



class ChuckNorrisJoke(Component):

    def start(self
        
        # Getting list of colors available in dataset
        response = requests.post('https://get-colors-service-dot-color-monarch-flex.appspot.com', json = {'allColors':'yes'})
        response = response.json()
        response = response['colors']
        
        # Finding a random index and getting the corresponding color
        randIdx =  random.randint(0,len(response))
        keys = [k for (k, v) in response.iteritems() ]
        color = response[keys[randIdx]][0]
        self.db.user.set('color', color)
        
        # Creating reply msg
        text = "Your color is " + color
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")