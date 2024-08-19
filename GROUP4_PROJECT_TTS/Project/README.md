# Computational Linguistics for Indian Languages (CS689A)
GROUP4- PROJECT: TEXT TO SPEECH FOR HINDI LANGUAGES
NEELU LALCHANDANI 231110031
PRIYANSHU JHA 231110039
TANMAY DUBEY 231110052

APPROACH- SYLLABLE-BASED CONCATENATION OF PHONEMES

Dependencies:
python
wave
pydub
os

*Change path of audio files according to your system in phonemeToSound.py.
*Write python index.py in your terminal to run the code.
*Enter Message in devanagri script.
*Go to output_audio.wav to hear the corresponding sound.

Flow:-
1. Message goes to tokenizer which creates word sequence
2. It is converted to syllable list
3. These syllables are mapped with their corresponding ids.
4. The ids are mapped with sounds, crossfading is applied to get final audio.

