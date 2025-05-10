# YouTube Video İndirici 🎥

Basit ve sade bir arayüzle YouTube videolarını bilgisayarına indirmeni sağlar. Video ya da MP3 formatında indirme yapabilirsin. Tkinter kullanılarak yapılmış bu masaüstü uygulaması, ekstra bir yazılım bilgisi gerektirmeden kolay kullanım sunar.

## 🚀 Özellikler

- ✅ En yüksek kalitede video indirme  
- ✅ 720p ve 480p video çözünürlük seçenekleri  
- ✅ MP3 formatında ses indirimi  
- ✅ Dinamik ilerleme çubuğu (progress bar)  
- ✅ Klasör seçme özelliği (varsayılan: proje içindeki `downloads` klasörü)  
- ✅ Karanlık, sade ve modern arayüz tasarımı  

## 🛠️ Gereksinimler

Aşağıdaki kütüphaneyi yüklemen gerekiyor:

pip install yt-dlp

> `tkinter` çoğu Python dağıtımında yüklü gelir. Eğer hata alırsan sistemine göre manuel kurman gerekebilir.

Ayrıca `ffmpeg` bilgisayarında kurulu olmalı ve ortam değişkenlerine (PATH) tanımlanmış olmalı.  
FFmpeg indirme sayfası: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

## ⚙️ Kullanım

1. `main.py` dosyasını çalıştır.  
2. Açılan arayüzde video linkini gir.  
3. İndirme kalitesini seç (`En iyi`, `720p`, `480p`, `MP3`).  
4. Dilersen indirme klasörünü değiştir.  
5. **"İndirmeyi Başlat"** butonuna tıkla.  
6. İndirme tamamlandığında bildirim gelir.  

## 📄 Lisans

Bu proje lisanssız olarak paylaşılmıştır. Dilediğiniz gibi kullanabilir, geliştirebilirsiniz.