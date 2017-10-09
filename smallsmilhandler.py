#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):
            """
            Constructor. Inicializamos las variables
            """
            self.width = ""
            self.height = ""
            self.background-color = ""
            self.id = ""
            self.top = ""
            self.bottom = ""
            self.left = ""
            self.right = ""
            self.src = ""
            self.region = ""
            self.begin = ""
            self.dur = ""
            self.end = ""
            self.variable = []
            
    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root_layout':
            # De esta manera tomamos los valores de los atributos
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.background_color = attrs.get('background_color', "")
            self.variable.append(self.width)
            self.variable.append(self.height)
            self.variable.append(self.background_color)
            
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            self.variable.append(self.id)
            self.variable.append(self.top)
            self.variable.append(self.bottom)
            self.variable.append(self.left)
            self.variable.append(self.right)
            
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.variable.append(self.src)
            self.variable.append(self.region)
            self.variable.append(self.begin)
            self.variable.append(self.dur)
           
        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.variable.append(self.src)
            self.variable.append(self.begin)
            self.variable.append(self.dur)       
            
        elif name == 'textstream':    
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.variable.append(self.src)
            self.variable.append(self.region)
