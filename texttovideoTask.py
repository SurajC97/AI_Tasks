import time
import math
import keras_cv
import tensorflow as tf
import matplotlib.pyplot as plt

from PIL import Image
from tensorflow import keras
from IPython.display import Image as IImage

import re
from moviepy.editor import *
import os

model = keras_cv.models.StableDiffusion(
    img_width=512,
    img_height=512
)

text= 'A fish was swimming in a pond, then a fisherman caught the fish.'
paragraphs = re.split(r"[,.]", text)

i=1
for para in paragraphs[:-1]:
  image = model.text_to_image(para, batch_size=1)
  im = Image.fromarray(image)
  im.save(f"image{i}.jpg")
  i+=1

i=1
for para in paragraphs[:-1]:

    # Load the image file using moviepy
    image_clip = ImageClip(f"image{i}.jpg").set_duration(3)

    # create a text clip from the text
    text_clip = TextClip(para, fontsize=50, color="white")
    text_clip = text_clip.set_pos('center').set_duration(3)

    # create a final video by concatenating
    print("Concatenate Audio, Image, Text to Create Final Clip...")
    video = CompositeVideoClip([image_clip, text_clip])

    # Save the final video to a file
    video = video.write_videofile(f"videos/video{i}.mp4", fps=24)
    i+=1

clips = []
l_files = os.listdir("videos")
for file in l_files:
    clip = VideoFileClip(f"videos/{file}")
    clips.append(clip)

final_video = concatenate_videoclips(clips, method="compose")
final_video = final_video.write_videofile("final_video.mp4")
print("The Final Video Has Been Created Successfully.")
