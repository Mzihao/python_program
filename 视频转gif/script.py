from moviepy.editor import VideoFileClip

clip = (VideoFileClip("2.mp4")
        .subclip(0, 4)
        .resize(0.17))
clip.write_gif("2.gif")
