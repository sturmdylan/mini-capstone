from pytube import YouTube 


yt = YouTube("https://www.youtube.com/watch?v=DC_grFx4AsA")

#stream = yt.streams.get_highest_resolution().download()

my_stream = yt.streams

'''for each_stream in my_stream
    print(each_stream)
'''

yt.streams.get_by_itag(18).download(filename="jake.mp4")

print(yt.title)
print(yt.thumbnail_url)
print(yt.author)
