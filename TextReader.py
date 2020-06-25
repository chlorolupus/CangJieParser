#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import base64
import json
import codecs
import io



testText = "幻燈\n片\n"
dict_cangjie = {
    "a": u"日",
    "b": u"月",
    "c": u"金",
    "d": u"木",
    "e": u"水",
    "f": u"火",
    "g": u"土",
    "h": u"竹",
    "i": u"戈",
    "j": u"十",
    "k": u"大",
    "l": u"中",
    "m": u"一",
    "n": u"弓",
    "o": u"人",
    "p": u"心",
    "q": u"手",
    "r": u"口",
    "s": u"尸",
    "t": u"廿",
    "u": u"山",
    "v": u"女",
    "w": u"田",
    "x": u"難",
    "y": u"卜",
    "z": u"Z",
}

def giveWord(dictPath="dictionary.json", fileToRead="script.txt", fileOutput="script.json"):
    with codecs.open(dictPath,mode='r',encoding="utf-8") as f:
        asciiString=""
        CangJieOutput="" 
        ChineseString=""
        finalScriptObject=[]
        d = json.load(f)
        with codecs.open(fileToRead,mode='r',encoding="utf-8") as file:
            lines = file.readlines()
            for num, line in enumerate(lines, 0):
                jsonFormat = "{stage}_{lineNo}"
                jsonID = jsonFormat.format(stage=fileToRead,lineNo=num)
                for char in line:
                    for entry in d:
                        if(char==entry['Words']):
                            ChineseString += char
                            for char in entry['Inputs_ASCII']:
                                CangJieOutput += dict_cangjie[char]
                            CangJieOutput += ' '
                            asciiString += entry['Inputs_ASCII'] + ' '
                print(finalScriptObject)
                finalScriptObject.append(
                {"Name": jsonID, 'Words':ChineseString,"Inputs_ASCII": asciiString, "Inputs_Separated": CangJieOutput}
                )
                tempString=""
                CangJieOutput="" 
                ChineseString=""
                asciiString=""
            with codecs.open(fileOutput, mode="w", encoding="utf-8") as finalJSON:
                json.dump(finalScriptObject, finalJSON, ensure_ascii=False,sort_keys=False,indent=4, separators=(',', ': '))
    
giveWord("dictionary.json",fileToRead="script.txt", fileOutput="script.json") 