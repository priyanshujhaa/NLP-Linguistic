OUTPUT_FILE = "output_audio.wav"

from Components import tokenizer
from Components import wordToPhonemes
from Components import phonemeToSound
from Components import syllabify

def text_to_speech(message, output_file=OUTPUT_FILE, debug=False, use_pronunciation_dict=True):
    print()
    if debug: 
        print("Starting TTS system...")
    print(message)
    words = tokenizer.tokenize(message)
    print(words)
    if debug: 
        print("Words list: " + str(words))
    # which takes list of words as input and iterates word by word and returns the syllables of that word
    syllable_list = [] # contains syllables of all the words
    for word in words:
        temp_list = syllabify.generate_syllable(word)
        syllable_list.append(temp_list)

    print("Syllable list: "+str(syllable_list))

    phonemes=[]

    for i in syllable_list: 
        temp=wordToPhonemes.words_to_phonemes(i,use_pronunciation_dict)
        phonemes.extend(temp)

    if debug: 
        print("Phonemes list: " + str(phonemes))
    phonemeToSound.phonemes_to_sounds(phonemes, output_file)
    if debug: 
        print("File created.")

if __name__ == "__main__":
    text = input("Please enter the text: ")
    text_to_speech(text, debug=True, use_pronunciation_dict=True)
