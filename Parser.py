#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import json

dict_cangjie = {"a": '日',
              "b": '月',
              "c": '金',
              "d": '木',
              "e": '水',
              "f": '火',
              "g": '土',
              "h": '竹',
              "i": '戈',
              "j": '十',
              "k": '大',
              "l": '中',
              "m": '一',
              "n": '弓',
              "o": '人',
              "p": '心',
              "q": '手',
              "r": '口',
              "s": '尸',
              "t": '廿',
              "u": '山',
              "v": '女',
              "w": '田',
              "x": '難',
              "y": '卜',
              "z": 'Z',
}
final_db_list = []
stageid = "Null"

def populateLibrary(originalDictName = 'cj5-tc.txt', finalDictName='dictionary.json'):
    with open(file=originalDictName,mode='r',encoding='utf-8') as txt:
        new_Data ={}
        data = txt.readlines()
        for num,line in enumerate(data,0):
            step_0 = line.split('\t')
            step_1 = step_0[0]
            step_2 = step_0[1]
            step_3 = ""
            step_4 = ' '
            
            # This is an ascii -> cangjie converter 
            for char in step_1:
                newchar = dict_cangjie.get(char)
                step_3 += newchar
            
            # This is to remake utf char with non ASCII
            for char in step_2:
                char = char.replace("\n","")
                print(char)
                step_4 += char.decode()
                           
            final_db_key_temp = "Demo_{lineNo}"
            final_db_key = final_db_key_temp.format(lineNo=num)
            final_db_list.append({
                'Name':final_db_key,
                'Inputs_ASCII':step_1,
                'Words': step_4
                })
            
    with open(file=finalDictName,mode='w') as dictionary:
        json.dump(final_db_list, dictionary)
    
populateLibrary(originalDictName = 'cj5-tc.txt', finalDictName='dictionary.json')