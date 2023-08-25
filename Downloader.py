# importing packages
from pytube import YouTube
import os



def download(url):
# url input from user
    yt = YouTube(str(url))

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    
    destination = './'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success

    print("ok")
    
    return new_file

#download("https://www.youtube.com/watch?v=x7X9w_GIm1s")