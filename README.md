#Compose Project
-ilk olarak dosya dizinini ve klasörleri ayarladım 

-Dosyalara gerekli kodları yazdım ve Dockerfile ı oluşturdum 

-Birbirine bağlı birden fazla container olduğu için hepsini birden ayağa kaldırmak için docker compose kullandım 

-Docker compose dosyasını oluşturdum ve projenin ayağa kalkması için gerekli ayarlamaları yaptım 

-Sonrasında docker compose ile oluşturduğum projemin image ini oluşturdum 

 -docker-compose up --build

-Oluşturduğum image dosyasını dockerhub da repository e push atmak kaldı 

-Öncesinde dockerhub repository i bağladım

  -docker tag compose_prj arifshn/compose_project:latest

-Şimdi push atabilirim

-docker push arifshn/compose_project:latest
