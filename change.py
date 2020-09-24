import soundfile

data, samplerate = soundfile.read('ground.wav')
soundfile.write('ground16.wav', data, samplerate, subtype='PCM_16')