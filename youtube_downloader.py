from pytube import YouTube

link = input("Link: ")
yt = YouTube(link)

ys = yt.streams.get_audio_only()

print("İndiriliyor")
ys.download()
print("İndirildi")
