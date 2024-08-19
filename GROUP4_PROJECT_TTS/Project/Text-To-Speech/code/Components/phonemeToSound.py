# # Matches each phoneme from list with appropriate wav file

# from Components import phonemes
# import wave, os

# AUDIOFILESPATH = "C:\\Users\\Priyanshu\\Desktop\\IIT Kanpur Courses\\NLP Linguistics-Arnab Bhattacharya Sir\\Project-draft2\\Project\\Aduio_files\\Aduio_files\\"

# def phonemes_to_sounds(phoneme_list, outfile):
#     audioFilePathNames = [get_sound_file(phoneme) for phoneme in phoneme_list]  # List comprehension for getting sound files
#     audios = [read_sound_file(infile) for infile in audioFilePathNames]  # List comprehension for reading sound files

#     output_params = audios[0][0]  # Use parameters from the first sound file
#     with wave.open(outfile, 'wb') as output:
#         output.setparams(output_params)
#         for frames in [item[1] for item in audios]:  # Iterate over frames in the data list
#             output.writeframes(frames)


# def get_sound_file(phoneme):
#     fname = "%03d" % phoneme
#     return AUDIOFILESPATH + fname + ".wav"

# def read_sound_file(audioFilePathNames):
#     with wave.open(audioFilePathNames, 'rb') as w:
#         return [w.getparams(), w.readframes(w.getnframes())]


# Tanmay's Update
# Matches each phoneme from list with appropriate wav file

from Components import phonemes
import wave, os
from pydub import AudioSegment

AUDIOFILESPATH = "C:\\Users\\Priyanshu\\Desktop\\IIT Kanpur Courses\\NLP Linguistics-Arnab Bhattacharya Sir\\Project-draft3\\Project\\Audio_files\\Audio_files\\"
        
def phonemes_to_sounds(phoneme_list, output_file, crossfade_duration=20):
    
    audio_files = [get_sound_file(phoneme) for phoneme in phoneme_list]
    crossfaded_audio = AudioSegment.from_file(audio_files[0])
    
    for audio_file in audio_files[1:]:
        
        audio = AudioSegment.from_file(audio_file)
        audio = audio.set_frame_rate(crossfaded_audio.frame_rate)
        crossfaded_audio = crossfaded_audio.fade_out(crossfade_duration)
        audio = audio.fade_in(crossfade_duration)
        crossfaded_audio = crossfaded_audio.append(audio, crossfade=crossfade_duration)
        
    crossfaded_audio.export(output_file, format="wav")


def get_sound_file(phoneme):
    fname = "%03d" % phoneme
    return AUDIOFILESPATH + fname + ".wav"

def read_sound_file(audioFilePathNames):
    with wave.open(audioFilePathNames, 'rb') as w:
        return [w.getparams(), w.readframes(w.getnframes())]