# -*- coding: utf-8 -*-

import requests
from meya import Component
from components.utilities import host, more_info
from meya.cards import List, Element, Button

class Shades(Component):

    def start(self):
        color = str(self.db.user.get('color'))
        api_host = host()
        URL = '/colors?name='+color
        response = requests.get(api_host+URL)
        response = response.json()['result']
        
        
        
        elements = []
        
        num_url = api_host + '/colors?color-number=' 
     
        shade5_URL =  requests.get(num_url + response['Shade 5'])
        shade6_URL =  requests.get(num_url + response['Shade 6'])

   
        # SHADE 5
        response = shade5_URL.json()['result']
        button = Button(text="Get Details",
                        flow="color_details",data={'colorName': response['Color Name']})
        default_action = Button(
            url=more_info(response['Color Name'],response['Color Number'],response['Collection Name']),
            webview_height_ratio="tall")
        element = Element(title=response['Color Name'],
                          subtitle='Shade 5',
                          image_url=response['imgURL'],
                          buttons=[button],
                          default_action=default_action)
        
        elements.append(element)
        
        # SHADE 6
        response = shade6_URL.json()['result']

        button = Button(text="Get Details",
                        flow="color_details",data={'colorName': response['Color Name']})
        default_action = Button(
            url=more_info(response['Color Name'],response['Color Number'],response['Collection Name']),
            webview_height_ratio="tall")
        element = Element(title=response['Color Name'],
                          subtitle='Shade 6',
                          image_url=response['imgURL'],
                          buttons=[button],
                          default_action=default_action)
        
        elements.append(element)
    
        card = List(elements=elements,
                    top_element_style="compact")
        message= self.create_message(card=card)
        
        return self.respond(message=message)
