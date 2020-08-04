from tkinter import filedialog
import youtube_dl

download_location = ""
videoUrl = ""


def best_audio():
    return {
        'format': 'bestaudio/best',
        'ignoreerrors': True,
        'outtmpl': download_location + '/%(title)s.%(mp3)s',
        'ffmpeglocation': './',
        'addmetadata': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        },
            {
            'key': 'FFmpegMetadata',
        }],
    }


def best_video():
    return {
        'format': 'bestvideo+bestaudio/best',
        'ignoreerrors': True,
        'outtmpl': download_location + '/%(title)s',
        'ffmpeglocation': './',
    }    
    
def open_directory():
    global download_location
    download_location = filedialog.askdirectory()
    print(download_location)


def vid_download(format,userInput):
    videoUrl = userInput.get()
    if videoUrl != "":
        if (format == "video"):
            with youtube_dl.YoutubeDL(best_video()) as ydl:
                ydl.download([videoUrl])
        elif (format == "audio"):
            with youtube_dl.YoutubeDL(best_audio()) as ydl:
                ydl.download([videoUrl])
        else:
            raise LookupError
    else:
        raise IOError