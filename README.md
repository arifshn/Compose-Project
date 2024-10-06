# Docker Compose Project

Bu projede, Docker Compose kullanarak birden fazla container içeren bir sistemi ayağa kaldırdım. Aşağıda adım adım ilerlemeler yer almakta.

## Adımlar:

1. **Dizin ve Klasör Yapısını Ayarlama:**
   - İlk olarak gerekli dosya dizinini ve klasörleri oluşturdum.

2. **Kodların ve Dockerfile'ın Oluşturulması:**
   - Projede gerekli olan dosyalara kodlar yazıldı ve ardından `Dockerfile` oluşturuldu.

3. **Docker Compose Kullanımı:**
   - Birbirine bağlı birden fazla container olduğu için hepsini aynı anda ayağa kaldırmak amacıyla `docker-compose.yml` dosyasını oluşturdum.
   - Bu dosyada gerekli ayarlamaları yaparak container'ların doğru bir şekilde çalışmasını sağladım.

4. **Image Oluşturma ve Projenin Çalıştırılması:**
   - `docker-compose` ile projenin imajını oluşturdum:
     ```bash
     docker-compose up --build
     ```

5. **Docker Hub'a Push Atma:**
   - Oluşturduğum imajı Docker Hub'a yüklemek için önce Docker Hub repository bağlantısını yaptım.
   - Image dosyasını etiketledim:
     ```bash
     docker tag compose_prj arifshn/compose_project:latest
     ```
   - Son olarak, imajı Docker Hub'a push ettim:
     ```bash
     docker push arifshn/compose_project:latest
     ```

---

Projenin bütün aşamaları tamamlandı ve başarılı bir şekilde Docker Hub'a push edildi. Artık projen diğer geliştiriciler veya kullanıcılar tarafından kullanılabilir.

