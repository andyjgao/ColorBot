# -*- coding: utf-8 -*-

import requests
from meya import Component
from components.utilities import host, more_info
from meya.cards import Cards, Card, Button

class Shades(Component):

    def start(self):
        
        # getting selected color details
        color = str(self.db.user.get('color'))
        api_host = host()
        URL = '/colors?name='+color
        response = requests.get(api_host+URL)
        response = response.json()['result']
        
        # initializing urls of the shade colors of selected color
        elements = []
        
        num_url = api_host + '/colors?color-number=' 
        
        # accent1_URL =  requests.get(num_url + response['Accent 1'])
        # accent2_URL =  requests.get(num_url + response['Accent 2'])
        # trim1_URL =  requests.get(num_url + response['Trim 1'])
        # trim2_URL =  requests.get(num_url + response['Trim 2'])
        shade1_URL =  requests.get(num_url + response['Shade 1'])
        shade2_URL =  requests.get(num_url + response['Shade 2'])
        shade3_URL =  requests.get(num_url + response['Shade 3'])
        shade4_URL =  requests.get(num_url + response['Shade 4'])
        shade5_URL =  requests.get(num_url + response['Shade 5'])
        shade6_URL =  requests.get(num_url + response['Shade 6'])

        # SHADE 1
        response = shade1_URL.json()['result']
        buttons = [
            Button(text="Get Details",flow="color_details",data={'colorName': response['Color Name']}),
            Button(text="Go to PPG", url=more_info(response['Color Name'],response['Color Number'],response['Collection Name']))
            
        ]
     
        element = Card(title=response['Color Name'],
                          text='Shade 1',
                          image_url=response['imgURL'],
                          buttons=buttons)
        
        elements.append(element)
        
        # SHADE 2
        response = shade2_URL.json()['result']

        buttons = [
            Button(text="Get Details",flow="color_details",data={'colorName': response['Color Name']}),
            Button(text="Go to PPG", url=more_info(response['Color Name'],response['Color Number'],response['Collection Name']))
            
        ]
     
        element = Card(title=response['Color Name'],
                          text='Shade 2',
                          image_url=response['imgURL'],
                          buttons=buttons)
        
        elements.append(element)
            
        # SHADE 3
        response = shade3_URL.json()['result']

        buttons = [
            Button(text="Get Details",flow="color_details",data={'colorName': response['Color Name']}),
            Button(text="Go to PPG", url=more_info(response['Color Name'],response['Color Number'],response['Collection Name']))
            
        ]
     
        element = Card(title=response['Color Name'],
                          text='Shade 3',
                          image_url=response['imgURL'],
                          buttons=buttons)
        
        
        elements.append(element)

        # SHADE 4
        response = shade4_URL.json()['result']

        buttons = [
            Button(text="Get Details",flow="color_details",data={'colorName': response['Color Name']}),
            Button(text="Go to PPG", url=more_info(response['Color Name'],response['Color Number'],response['Collection Name']))
            
        ]
     
        element = Card(title=response['Color Name'],
                          text='Shade 4',
                          image_url=response['imgURL'],
                          buttons=buttons)
        
        elements.append(element)
    
        # SHADE 5
        response = shade5_URL.json()['result']
        buttons = [
            Button(text="Get Details",flow="color_details",data={'colorName': response['Color Name']}),
            Button(text="Go to PPG", url=more_info(response['Color Name'],response['Color Number'],response['Collection Name']))
            
        ]
     
        element = Card(title=response['Color Name'],
                          text='Shade 5',
                          image_url=response['imgURL'],
                          buttons=buttons)
        elements.append(element)
        
        # SHADE 6
        response = shade6_URL.json()['result']
       
        buttons = [
            Button(text="Get Details",flow="color_details",data={'colorName': response['Color Name']}),
            Button(text="Go to PPG", url=more_info(response['Color Name'],response['Color Number'],response['Collection Name']))
            
        ]
     
        # creating reply msg 
        element = Card(title=response['Color Name'],
                          text='Shade 6',
                          image_url=response['imgURL'],
                          buttons=buttons)
        
        elements.append(element)
    

        card = Cards(elements=elements)
        message= self.create_message(card=card)
        
        return self.respond(message=message)
