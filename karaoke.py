#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import json
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from urllib.request import urlretrieve


if __name__ == "__main__":
    file_json = sys.argv[1][:-4] + 'json'
    file_json = open(file_json, 'w')
    atribut_org = ""
    total = ""
    try:
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(sys.argv[1]))
        mytags = cHandler.get_tags()

        for linedicc in mytags:
            for tag, atributo in linedicc.items():
                for at, valor in atributo.items():
                    if at == "src" and valor[0:7] == "http://":
                        urlretrieve(valor, valor.split('/')[-1])
                        valor = valor.split('/')[-1]
                    if valor != "":
                        atribut_org += "\t" + at + "=" + '"' + valor + '"'

                print(tag + atribut_org)
                total += (tag + atribut_org + "\n")
                atribut_org = ""
        json.dump(total, file_json)

    except IndexError:
        sys.exit('Usage: python3 karaoke.py file.smil')
    except FileNotFoundError:
        sys.exit('Usage: python3 karaoke.py file.smil')
