# -*- coding: utf-8 -*-
import requests
from meya import Component
from components.utilities import host, colors
from meya.cards import Image, ImageWithButtons, Button, Card


class ColorRecommend(Component):

    def start(self):
        # importing from utilities
        api_host = host()
        colorDict = colors()
        
        #getting user color
        color = self.properties['colorName']
        
        #finding color from DB
        if color in colorDict:
            rgb = colorDict[color]
            r= str(rgb[0])
            g = str(rgb[1])
            b = str(rgb[2])
            url = '/colors?R='+r+'&G='+g+'&B='+b
            response = requests.get(api_host+url)
            response = response.json()['result']
            
            #Getting color name and image
            text = response['Color Name']
            self.db.user.set('color', text)
            buttons = [Button(text='Get Details',flow="color_details",data={'colorName': self.db.user.get('color')})]
            image = Card(title=text, image_url=response['imgURL'], buttons=buttons,   mode="buttons", passthru='false')
            
            #creating reply msg
            image_card =  self.create_message(card=image)
            text = 'The best PPG paint that matches with your color is ' + \
            text + '. Here is what the color looks like:'
            reply_text = self.create_message(text=text)
            message = [reply_text,image_card]
            return self.respond(messages=message, action="next")
        
        #color not found
        else:
            text = 'Unfortunately, I cannot find the color you are looking for.'
            message = self.create_message(text=text)
            return self.respond(message=message, action="next")
        return self.respond(message="error occured", action="next")
