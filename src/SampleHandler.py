import pyaudio
import wave

CHUNK = 1024
playingStreams = {}

def getPlayingSamples():
    playingSamples = playingStreams.keys()
    return playingSamples

def play(button_configs):
    if (not button_configs) and (len(button_configs) == 3) and (playingStreams.keys().__contains__(button_configs[0])):
        audioPlayer = pyaudio.PyAudio()
        try:
            filepath = button_configs[1]
            sample = wave.open(filepath)
            stream = audioPlayer.open( format = audioPlayer.get_format_from_width(sample.getsampwidth()),
                                       channels = sample.getnchannels(),
                                       rate = sample.getframerate(),
                                       output = True)
            data = sample.readframes(CHUNK)
            while len(data) > 0:
                stream.write(data)
                data = sample.readframes(CHUNK)
        except Exception as e:
            print('An error occurred while trying to play sample: ' + str(e))
    else:
        print('Parameters are not usable.')

def stop(button_configs):
    stoppedStream = playingStreams.get(button_configs[0])
    stoppedStream.stop_stream()
    stoppedStream.close()
    playingStreams.pop(stoppedStream)

# wf = wave.open('../resources/test.wav', 'rb')
#
# # instantiate PyAudio
# p = pyaudio.PyAudio()
#
# # open stream
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True)
#
# # read data
# data = wf.readframes(CHUNK)
#
# # play stream
# while len(data) > 0:
#     stream.write(data)
#     data = wf.readframes(CHUNK)
#
# # stop stream
# stream.stop_stream()
# stream.close()
#
# # close PyAudio
# p.terminate()
