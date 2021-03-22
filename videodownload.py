Download_Videos_From_Youtube = """from pytube import YouTube

link = input("Enter URL Please: ")
video = YouTube(link)

def completed():
    print("download completed")

video.streams.get_highest_resolution().download(output_path="C:/desktop", filename="الحمار زين")
video.register_on_complete_callback(completed())"""

Download_PlayLists_From_Youtube = """from pytube import Playlist


link = input("Enter Playlist Link: ")
playlist = Playlist(link)

def completed():
    print("download completed")

for video in playlist.videos:
    video.streams.get_highest_resolution().download(output_path="C:/desktop")
video.register_on_complete_callback(completed())
"""
