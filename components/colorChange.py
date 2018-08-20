# -*- coding: utf-8 -*-
import requests
from meya import Component
from components.utilities import host, colors
from meya.cards import Image, Button, ImageWithButtons, Card

class ColorChange(Component):

    def start(self):
        
        # From user color, change to color(s) based on selected harmony
        api_host = host()
        harmony = self.properties['harmony']
        color = str(self.db.user.get('color'))       
        URL = '/' + harmony + '?name=' + color
        response = requests.get(api_host + URL)
        response = response.json()['result'][0]['color1']
        
        # From new color, get details on the color(s)
        new_color = response['Name']  
        self.db.user.set('color', new_color)
        buttons = [Button(text='Get Details',flow="color_details",data={'colorName': self.db.user.get('color')})]
        image = Card(title = response['Name'], image_url=response['imgURL'], buttons=buttons, mode="buttons", passthru='true')
        
        #creating reply msg
        image_card =  self.create_message(card=image)
        text = 'The best PPG paint that matches with your new ' + harmony \
        + ' color is ' + new_color + '. Here is what the color looks like:'
        reply_text = self.create_message(text=text)
        message = [reply_text,image_card]
        return self.respond(messages=message, action="check")
