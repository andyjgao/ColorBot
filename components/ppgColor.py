# -*- coding: utf-8 -*-
import requests
from meya import Component
from components.utilities import host, more_info
from meya.cards import Card, Button


class ColorRecommend(Component):

    def start(self):
        # importing from utilities
        api_host = host()

        # getting user color
        color = self.properties['colorName'].capitalize()
        url = '/colors?name='+color
        response = requests.get(api_host+url)
        response = response.json()['result']
        
        # getting color name and image
        if response['Color Name']:
            text = response['Color Name']
            self.db.user.set('color', text)
            
            # Color Details
            name =  str(self.db.user.get('color'))
            number = response['Color Number']
            r,g,b = str(response['R']),str(response['G']),str(response['B'])
            desc = response['Color Description']
            colName = response['Collection Name']
            imgURL = response['imgURL']
            ppg_url = more_info(name,number,colName)
            buttons = [Button(text="Go to PPG", url=ppg_url)]
            
            # Creating reply msg
            card = Card(
                     image_url=imgURL,
                     title=name,
                     buttons = buttons
            )
            text = 'The following is what I found in regards to ' + name +':'
            msg1 = self.create_message(text=text)
            msg2 = self.create_message(card=card)
            text = 'Description: ' + desc + '\n' + 'RGB: ( ' +r+', '+g+', '+b+ ' )' +'\n' + 'Color Number: ' + number
            msg3 = self.create_message(text=text)

            
            
            return self.respond(messages=[msg1,msg2,msg3], action="next")

        # color not found
        else:
            text = 'Unfortunately, I cannot find the color you are looking for.'
            message = self.create_message(text=text)
            return self.respond(message=message, action="next")
        return self.respond(message="error occured", action="next")
