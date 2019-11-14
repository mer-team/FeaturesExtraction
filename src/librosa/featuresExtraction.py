#install requirements -> pip install --user -r requirements.txt

#Help ->https://librosa.github.io/librosa/tutorial.html#quickstart; Exemplo extração de batimentos
import numpy as np
import librosa

filename = '../../audios/DYW-kEiCnJI.mp3'

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

print('Saving output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)