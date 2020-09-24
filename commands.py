import urllib.request
import json
from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice
import requests
from lxml import html


class Command():
    def __init__(self,comingVoice):
        self.voice = comingVoice.upper()
        self.voiceBlocks = self.voice.split()
        print(self.voiceBlocks)
        self.commands = ["ABONE", "ÇEVİR", "NABER", "NASILSIN", "KAPAT", "HAVA"]


    def dubbing(self, textOfVoice):
        tts = gTTS(text=textOfVoice, lang = 'tr' )
        tts.save("audio.mp3")
        playsound("audio.mp3")
        os.remove("audio.mp3")
        print(textOfVoice)


    def close(self):
        self.dubbing("Kapatıyorum, görüşmek üzere")
        sys.exit()


    def weather(self):
        r = requests.get("https://www.ntvhava.com/konum/elazig/15-gunluk-hava-tahmini")
        tree = html.fromstring(r.content)

        degree = tree.xpath('//*[@id="main"]/section[3]/div/ul[3]/li[1]/div[2]/div[1]/p[1]/span')
        statu = tree.xpath('//*[@id="main"]/section[3]/div/ul[3]/li[1]/div[2]/div[1]/p[2]')
        warning = ""

        if statu[0].text == "Yağmurlu":
            warning = "Dont forget umbrella!"


        text = "Mücahit, bugün hava {} derece ve {} gözüküyor.".format(degree[0].text, statu[0])
        self.dubbing(text)


    def chat(self):
        texts = ["İyiyim ama bundan sanane",
                 "Beni boşver sen kendinden bahset",
                 "Düşünmem lazım",
                ]

        choice_text = choice(texts)
        self.dubbing(texts)


    def youtube(self):
        url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&fields=items/statistics/subscriberCount&key=AIzaSyDjhNNVNMfw3rT3eB2u5JJyCxDA-CeVpIQ"
        data = urllib.request.urlopen(url).read()

        self.SubscriberCount = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        text = "Şu an pewdiepie kanalının {} abonesi var".format(self.SubscriberCount)
        self.dubbing(text)


    def findCommand(self):
        for command in self.commands:
            if command in self.voiceBlocks:
                self.commandExecute(command)


    def commandExecute(self, command):
        if command == "Abone":
            self.youtube()
        if command == "Kapat":
            self.close()
        if command == "Naber" or command == "nasılsın":
            self.chat()
        if command == "Hava durumu":
            self.weather()

