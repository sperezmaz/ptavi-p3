#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import json
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from urllib.request import urlretrieve


class KaraokeLocal():
    def __init__(self, file_smil):
        """
        Constructor. Parsea el fichero SMIL y obtiene las etiquetas
        """
        self.localiz_local = False
        parser = make_parser()
        self.cHandler = SmallSMILHandler()
        parser.setContentHandler(self.cHandler)
        parser.parse(open(file_smil))
        self.mytags = self.cHandler.get_tags()

    def __str__(self):
        """
        Método que devuelve un string listo para ser imprimido
        """
        self.atribut_org = ""
        self.total = ""
        for linedicc in self.mytags:
            for tag, atributo in linedicc.items():
                for at, valor in atributo.items():
                    if self.localiz_local and valor[0:7] == "http://":
                        valor = valor.split('/')[-1]
                    if valor != "":
                        self.atribut_org += "\t" + at + "=" + '"' + valor + '"'
                self.total += (tag + self.atribut_org + "\n")
                self.atribut_org = ""
        return self.total

    def do_json(self, file_smil, file_json):
        """
        Método que guarda dos ficheros diferentes segun lo llamemos
        """
        if file_json != "local":
            file_json = file_smil[:-4] + 'json'
        else:
            file_json = file_json + '.json'
        file_json = open(file_json, 'w')
        json.dump(self.total, file_json)
        self

    def do_local(self):
        """
        Método para descargar los recursos remotos
        """
        for linedicc in self.mytags:
            for tag, atributo in linedicc.items():
                for at, valor in atributo.items():
                    if at == "src" and valor[0:7] == "http://":
                        urlretrieve(valor, valor.split('/')[-1])
                        self.localiz_local = True

if __name__ == "__main__":
    """
    Programa principal(Comprueba que no hay errores en la invocación)
    """
    try:
        file_smil = sys.argv[1]
        karaoke = KaraokeLocal(file_smil)
        karaoke.__str__()
        print(karaoke)
        karaoke.do_json(file_smil, "nada")
        karaoke.do_local()
        karaoke.__str__()
        karaoke.do_json(file_smil, "local")
        print(karaoke)
    except IndexError:
        sys.exit('Usage: python3 karaoke.py file.smil')
    except FileNotFoundError:
        sys.exit('Usage: python3 karaoke.py file.smil')
