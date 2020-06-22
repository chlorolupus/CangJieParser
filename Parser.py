#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import json
import codecs

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
final_db_list = []
stageid = "Null"


def populateLibrary(originalDictName="cj5-tc.txt", finalDictName="dictionary.json"):
    with open(file=originalDictName, mode="r", encoding="utf-8") as txt:
        new_Data = {}
        data = txt.readlines()
        for num, line in enumerate(data, 0):
            step_0 = line.split("\t")
            step_1 = step_0[0]
            step_2 = step_0[1]
            step_3 = ""
            step_4 = " "

            # This is an ascii -> cangjie converter
            for char in step_1:
                newchar = dict_cangjie.get(char)
                step_3 += newchar

            # This is to remake utf char with non ASCII
            for char in step_2:
                char = char.replace("\n", "")
                print(char)
                step_4 += char

            final_db_key_temp = "Demo_{lineNo}"
            final_db_key = final_db_key_temp.format(lineNo=num)
            final_db_list.append(
                {"Name": final_db_key, "Inputs_ASCII": step_1, "Words": step_4}
            )

    with codecs.open(finalDictName, "w", "utf-8") as dictionary:
        json.dump(final_db_list, dictionary, ensure_ascii=False)


populateLibrary(originalDictName="cj5-tc.txt", finalDictName="dictionary.json")

