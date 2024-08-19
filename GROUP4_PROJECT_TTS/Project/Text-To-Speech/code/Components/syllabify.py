def generate_syllable(word):
    counter=0
    # Array containing all the vowels in Devanagari script
    hindi_vowels = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ओ', 'औ']


    # Array containing all the matras in Devanagari script
    hindi_matras = ['ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'े', 'ै', 'ो', 'ौ', 'ॄ','़']

    # Array containing mapping of matras with vowels in Devanagari script
    hindi_vowel_matras = {"ा":"आ","ि":"इ","ी":"ई","ु":"उ","ू":"ऊ","े":"ए","ै":"ऐ","ो":"ओ","ौ":"औ", "ं":"अं","ृ":"ऋ",'ॉ':"ऑ", 'ॄ': "ॠ" }    
    res= []

    for i in word:
        n = len(word)
        counter+=1

        if(counter-2>=0 and word[counter-2]=='्'): continue

        # vowel
        elif(i in hindi_vowels):
            res.append(i)

        # matra or halanth
        elif(i=='्' or (i in hindi_vowel_matras) or i=='़'): continue

        #consonant followed by maatra
        elif(counter != n and((word[counter] in hindi_matras))):
            res.append(i+word[counter])

        #consonant followed by halanth
        elif(counter != n and ((word[counter]=='्'))):
            temp=""
            temp+=i+'्'
            if(counter+1!=n):
              temp+=word[counter+1]
            if(counter+2<len(word) and (word[counter+2] in hindi_matras)):
              temp+=word[counter+2]
            res.append(temp)

        #consonant followed by consonant or nothing
        else:
            res.append(i)
    return res
# word="शिव"
# print(generate_syllable(word))
# # for word in hindi_words_unicode:
  #  print(generate_syllable(word))