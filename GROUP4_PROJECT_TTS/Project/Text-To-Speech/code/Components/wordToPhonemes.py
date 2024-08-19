from Components import phonemes, char_to_ph_id
import ast, re
import wave, os
from Components import tokenizer

def tuple_to_int(tup):
    if isinstance(tup, tuple):
        return tup[0]
    return tup[1]

def words_to_phonemes(word, use_pronunciation_dict=True):
    # Takes list which contains all syllables of one word
    result = []
    phonemeList = char_to_ph_id.phoneme_scan(word)
    # print(str(type(phonemeList[1])))
    new_phoneme_list = []
    for item in phonemeList:
        new_item = char_to_ph_id.exception_handler(item)
        if(str(type(new_item))==str(type(phonemeList))):
             for i in new_item:
                  new_phoneme_list.append(i)
        else:
             new_phoneme_list.append(new_item)
    phonemeList = char_to_ph_id.phoneme_scan(new_phoneme_list)
    for i in phonemeList:
            # print("I is: "+str(i))
            result.append(tuple_to_int(i))
    # print(result)
    # result.extend(phonemeList)
    result.append(phonemes.PAUSE_WORD)
   # print(type(result[2]))
    return result
