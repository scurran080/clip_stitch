from moviepy.editor import *


def stitch(clips):
    output_clips: list[VideoFileClip] = []
    for clip in clips:
        subclip = VideoFileClip(clip)
        output_clips.append(subclip)

    final_output = concatenate_videoclips(output_clips, method="compose")
    final_output.write_videofile(filename="output.mp4")
