from pytube import YouTube

link = input('Type link:')

yt = YouTube(link)

ys = yt.streams.get_highest_resolution()

ys.download('./videos')


print('download success')