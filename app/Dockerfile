# Python 3.9 slim imajını kullandım
FROM python:3.9-slim

# Çalışma dizinini ayarladım
WORKDIR /usr/src/app

# Gereksinimleri yüklemek için requirements.txt adında bir txt dosyası oluşurdum ve içine yüklenmesini sağladım 
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Uygulamayı kopyala kısmında kopyalamaya gerek yok 
COPY . .

# Flask uygulamasını başlattım 
CMD ["python", "app.py"]
