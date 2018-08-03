# -*- coding: utf-8 -*-
import requests
from meya import Component
from components.utilities import host, more_info
from meya.cards import List, Element, Button, Card, Cards

class ColorChange(Component):

    def start(self):
        
        api_host = host()
        harmony = self.properties['harmony']
        color = str(self.db.user.get('color'))       
        URL = '/' + harmony + '?name=' + color
        response = requests.get(api_host + URL)
        response = response.json()['result'][0]
        color_names = []
        color_img = []
        
        for color in response:
            color_names.append(response[color]['Name'])
            color_img.append(response[color]['imgURL'])
    
        ppg_url = api_host + '/colors?name='
        url_response = []
        for name in color_names:
            response =  requests.get(ppg_url + name)
            response = response.json()['result']
            url_response.append(response)
        
   
        elements = []
        print url_response
        for i in range(0, len(color_names)):
            buttons = [
                Button(text="Get Details",flow="color_details",data={'colorName': color_names[i]}),
                Button(text="Go to PPG", url=more_info(url_response[i]['Color Name'],url_response[i]['Color Number'],url_response[i]['Collection Name']))
            ]
     
            element = Card(title=color_names[i],
                          image_url=url_response[i]['imgURL'],
                          buttons=buttons)
        
            
            elements.append(element)
           
        
        
        card = Cards(elements=elements)
        message= self.create_message(card=card)
        
        text = 'We found that these colors best match with {}: '.format(str(self.db.user.get('color'))       )
        reply_text = self.create_message(text=text)
        message = [reply_text,message]
        
        
        return self.respond(messages=message)