# -*- coding: utf-8 -*-
import requests
from meya import Component
from components.utilities import host, more_info
from meya.cards import Card, Button


class ColorDetails(Component):

    def start(self):
        
        # From a selected color, get details in json
        color = str(self.db.flow.get('colorName'))
        self.db.user.set('color', color)
        URL = '/colors?name=' + color
        api_host = host()
        response = requests.get(api_host+URL)
        response = response.json()['result']
        
        
        # Organizing detail info to display Color Number, RGB, Desc, Image
        name = color
        number = response['Color Number']
        r,g,b = str(response['R']),str(response['G']),str(response['B'])
        desc = response['Color Description']
        colName = response['Collection Name']
        imgURL = response['imgURL']
        ppg_url = more_info(name,number,colName)
        buttons = [Button(text="Go to PPG", url=ppg_url)]
        card = Card(
                 image_url=imgURL,
                 title=name,
                 buttons = buttons
        )
        
        # creating reply msg
        the_card = self.create_message(card=card)
        text = 'Description: ' + desc + '\n' + 'RGB: ( ' +r+', '+g+', '+b+ ' )' +'\n' + 'Color Number: ' + number
        reply_text = self.create_message(text=text)


        message = [the_card,reply_text]
        return self.respond(messages=message, action="next")
