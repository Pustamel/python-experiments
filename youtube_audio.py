from pytube import YouTube

link = input('Type link:')

url_youtube = YouTube(link)

ys = url_youtube.streams.get_audio_only()

ys.download('./sounds')

print('download success')


