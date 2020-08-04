import ytdVM as VM
import tkinter

root = tkinter.Tk()
root.title('Youtube Video Downloader')

# TODO: Select Path
tkinter.Button(root, text="Select Directory",command=lambda: VM.open_directory()).pack()

# TODO: Enter Video URL
tkinter.Label(root, text="Enter Video Url").pack()
entry1 = tkinter.Entry(root, width=50)
entry1.pack()

# TODO: Button Download Video
tkinter.Button(root, text="Highest Quality Video",command=lambda: VM.vid_download("video",entry1)).pack()

# TODO: Button Download Audio
tkinter.Button(root, text="Highest Quality Audio",command=lambda: VM.vid_download("audio",entry1)).pack()

# TODO: Button Open Download Folder


root.mainloop()