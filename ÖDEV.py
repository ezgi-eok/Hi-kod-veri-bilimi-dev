#!/usr/bin/env python
# coding: utf-8

# In[1]:


# İsimlere yaş değerleri atanır
ahmet_yas = 25
mehmet_yas = 30
ayse_yas = 20

# Karşılaştırma ve mantıksal operatörlerle değerlendirme
print(ahmet_yas > ayse_yas and mehmet_yas > ayse_yas)  # Ahmet ve Mehmet, Ayşe'den büyük mü?
print(ahmet_yas < mehmet_yas or ayse_yas < ahmet_yas)  # Ahmet, Mehmet'ten veya Ayşe, Ahmet'ten küçük mü?
print(not (ahmet_yas == mehmet_yas))  # Ahmet ve Mehmet aynı yaşta değil mi?


# In[2]:


# Kullanıcıdan iki değer alınır
deger1 = int(input("Birinci sayıyı giriniz: "))
deger2 = int(input("İkinci sayıyı giriniz: "))

# Toplama, çıkarma, çarpma ve bölme işlemleri
print(f"Toplama: {deger1 + deger2}")
print(f"Çıkarma: {deger1 - deger2}")
print(f"Çarpma: {deger1 * deger2}")
print(f"Bölme: {deger1 / deger2}")


# In[3]:


# Kullanıcıdan bilgiler alınır
isim = input("Adınızı giriniz: ")
yas = input("Yaşınızı giriniz: ")
sehir = input("Şehir adını giriniz: ")
meslek = input("Mesleğinizi giriniz: ")

# Bilgiler yazdırılır
print(f"Adınız: {isim}, Yaşınız: {yas}, Şehir: {sehir}, Meslek: {meslek}")


# In[4]:


# Değişken tanımlanır
ifade = "Hi-Kod Veri Bilimi Atölyesi"

# Kelimeler seçilir
kelime1 = ifade.split()[0]  # "Hi-Kod"
kelime2 = ifade.split()[1]  # "Veri"
kelime3 = ifade.split()[2]  # "Bilimi"
kelime4 = ifade.split()[3]  # "Atölyesi"

print(kelime1, kelime2, kelime3, kelime4)

# İfade büyük harfe dönüştürülür
print(ifade.upper())

# İfade küçük harfe dönüştürülür
print(ifade.lower())

# Çift ve tek sayılar seçilir
sayilar = "0123456789"
cift_sayilar = sayilar[0::2]  # "02468"
tek_sayilar = sayilar[1::2]  # "13579"

print(f"Çift sayılar: {cift_sayilar}")
print(f"Tek sayılar: {tek_sayilar}")


# In[ ]:




