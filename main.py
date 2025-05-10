import yt_dlp

link = input("Video linkini gir: ")

print("\nİndirme Kalitesi Seç:")
print("1 - En iyi kalite")
print("2 - 720p")
print("3 - 480p")
print("4 - Sadece ses (MP3)")

secim = input("Seçimin (1-4): ")

ydl_opts = {}

if secim == "1":
    ydl_opts['format'] = 'best'
elif secim == "2":
    ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best'
elif secim == "3":
    ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best'
elif secim == "4":
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
else:
    print("Geçersiz seçim, en iyi kalite indiriliyor.")
    ydl_opts['format'] = 'best'

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("İşlem tamamlandı!")