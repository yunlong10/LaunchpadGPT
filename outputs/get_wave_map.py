import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load ground truth video
cap = cv2.VideoCapture('ground_truth.mp4')

# Get audio information
sample_rate = int(cap.get(cv2.CAP_PROP_FPS))
num_channels = 2
sample_width = 2

# Create an array to store audio data
audio_data = np.empty((0, num_channels), dtype=np.int16)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Extract audio data from the frame
    audio_frame = np.frombuffer(frame.tobytes(), dtype=np.int16).reshape(-1, num_channels)
    audio_data = np.vstack((audio_data, audio_frame))

cap.release()

# Save the audio data as a WAV file
import soundfile as sf

sf.write('ground_truth_audio.wav', audio_data, sample_rate)

# Plot the waveform and save the figure
plt.plot(audio_data[:, 0])
plt.xlabel('Time (samples)')
plt.ylabel('Amplitude')
plt.savefig('ground_truth_audio_waveform.png')
