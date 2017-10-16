#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.variable = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        tags = {'root-layout': {'width', 'height', 'background-color'},
                'region': {'id', 'top', 'bottom', 'left', 'right'},
                'img': {'src', 'region', 'begin', 'dur'},
                'audio': {'src', 'begin', 'dur'},
                'textstream': {'src', 'region'}}
        atribcont = {}

        if name in tags:

            for atribute in tags[name]:
                atribcont[atribute] = attrs.get(atribute, "")
                tagsentero = {name: atribcont}

            self.variable.append(tagsentero)

    def get_tags(self):
        return self.variable

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
