from pytube import YouTube

link =input("Link:  ")

yt=YouTube(link)
ys=yt.streams.get_highest_resolution()

print("İndiriliyor..")

ys.download()

print("İndirildi..")