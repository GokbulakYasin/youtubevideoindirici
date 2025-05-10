# YouTube Video İndirici 🎥

Basit ve sade bir arayüzle YouTube videolarını bilgisayarına indirmeni sağlar. Video ya da MP3 formatında indirme yapabilirsin. Tkinter kullanılarak yapılmış bu masaüstü uygulaması, ekstra bir yazılım bilgisi gerektirmeden kolay kullanım sunar.

## 🚀 Özellikler

- ✅ En yüksek kalitede video indirme  
- ✅ 720p ve 480p video çözünürlük seçenekleri  
- ✅ MP3 formatında ses indirimi  
- ✅ Dinamik ilerleme çubuğu (progress bar)  
- ✅ Klasör seçme özelliği (varsayılan: proje içindeki `downloads` klasörü)  

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

Copyright (c) 2025 Yasin Gökbulak

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
