import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Get all files/folders in current directory
highlightFiles = os.listdir('.')

# Sort files from oldest to newest
highlightFiles.sort(key=os.path.getmtime)

# Filtering for .mp4 files
# 5-17.182 seconds are frames with video of acutal play
subclips = [VideoFileClip(clip).subclip(5, 17.182) for clip in highlightFiles if clip.endswith(".mp4")]
final_clip = concatenate_videoclips(subclips)

final_clip.write_videofile("output.mp4")
