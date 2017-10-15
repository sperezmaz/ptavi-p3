#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import json
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(sys.argv[1]))
    mytags = cHandler.get_tags()
    
    for linedicc in mytags:
        for tag, atributo in linedicc.items(): 
            print('\n' + tag, end='') 
            
            for at, valor in atributo.items():
                print('/t' + at + "=" + '"' + valor + '"', end='')
