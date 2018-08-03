# -*- coding: utf-8 -*-
import requests
import urllib, cStringIO,urllib2, base64
from io import BytesIO
from PIL import Image
from utilities import host
from utilities import get_as_base64
from meya import Component
from meya.cards import Image, ImageWithButtons, Button, Card
class ChuckNorrisJoke(Component):
    

    def start(self):
        URL = str(self.db.flow.get('color_url'))
        data = {"url": URL}
        response = requests.post(url = "https://ppgpaint-api.herokuapp.com", json = data)
        response = response.json()
        closestColor = response['result']['colors'][0]['closestColor'][0]
        URL = '/colors?name=' + closestColor
        api_host = host()
        response = requests.get(api_host+URL)
        response = response.json()['result']
         #Getting color name and image
        text = response['Color Name']
        self.db.user.set('color', text)
        buttons = [Button(text='Get Details',flow="color_details",data={'colorName': self.db.user.get('color')})]
        image = Card(title = text, image_url=response['imgURL'], buttons=buttons,   mode="buttons", passthru='true')
        #creating reply msg
        image_card =  self.create_message(card=image)
        text = 'The best PPG paint that matches with your color is ' + \
        text + '. Here is what the color looks like:'
        reply_text = self.create_message(text=text)
        message = [reply_text,image_card]
        return self.respond(messages=message, action="next")
        
        
        

        
    