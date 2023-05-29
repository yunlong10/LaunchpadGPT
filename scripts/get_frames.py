import cv2
import os

# Define the input and output directories
input_dir = 'segments'
output_dir = 'frames'

# Create the output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop over all the video files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.mp4') and filename.startswith('seg'):
        # Open the video file
        filepath = os.path.join(input_dir, filename)
        cap = cv2.VideoCapture(filepath)

        # Get video properties
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Create the output directory for this video if it does not exist
        output_subdir = os.path.join(output_dir, os.path.splitext(filename)[0])
        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        # Read each frame and save as image file
        for i in range(frame_count):
            ret, frame = cap.read()
            if not ret:
                break
            frame_filename = f'seg{os.path.splitext(filename)[0][3:]}frame{i+1:04d}.png'
            output_filepath = os.path.join(output_subdir, frame_filename)
            cv2.imwrite(output_filepath, frame)

        # Release the video file
        cap.release()
