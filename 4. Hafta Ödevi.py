#!/usr/bin/env python
# coding: utf-8

# ## 1.Ödev - Maaş Bilgisi ve Veri Hesaplama
# 

# In[ ]:


# Kullanıcıdan maaş bilgisi al
maas = float(input("Maaşınızı giriniz: "))

# Vergi oranını belirle ve yeni maaşı hesapla
if maas <= 10000:
    vergi_orani = 0.05
elif maas <= 25000:
    vergi_orani = 0.10
elif maas <= 45000:
    vergi_orani = 0.25
else:
    vergi_orani = 0.30

vergi = maas * vergi_orani
yeni_maas = maas - vergi

# Sonuçları yazdır
print(f"Vergi oranı: %{vergi_orani * 100}")
print(f"Kesilen vergi miktarı: {vergi:.2f} TL")
print(f"Yeni maaşınız: {yeni_maas:.2f} TL")


# ## 2. Ödev - Kullanıcı Adı ve Şifre Oluşturma 

# In[ ]:


# Kullanıcıdan giriş bilgilerini al
kullanici_adi = input("Kullanıcı adınızı oluşturun: ")
sifre = input("Şifre oluşturun: ")

# Şifre uzunluğunu kontrol et
if len(sifre) >= 6:
    print("Hesabınız oluşturuldu.")
else:
    print("Altı haneli şifre oluşturmanız gerekmektedir!")


# ## 3. Ödev - Geliştirilmiş Şifre Kontrolü

# In[ ]:


# Kullanıcıdan doğru şifre oluşturana kadar şifre al
while True:
    sifre = input("Şifre oluşturun (5 ile 10 hane arasında olmalı): ")

    if 5 <= len(sifre) <= 10:
        print("Hesabınız oluşturuldu.")
        break
    else:
        print("Lütfen şifrenizi 5 haneden az ve 10 haneden fazla olmayacak şekilde oluşturun!")


# ## 4. Ödev - İsim ve Şifre Girişi ile Deneme Hakkı

# In[ ]:


# Önceden tanımlı şifre
dogru_sifre = "123456"

# Kullanıcıya üç giriş hakkı tanımla
hak = 3

while hak > 0:
    # Kullanıcıdan bilgiler al
    isim = input("İsminizi giriniz: ")
    sifre = input("Şifrenizi giriniz: ")

    if sifre == dogru_sifre:
        print("Giriş yapıldı.")
        break
    else:
        hak -= 1
        print("Yanlış şifre girildi!")
        if hak > 0:
            print(f"Kalan hakkınız: {hak}")
        else:
            print("Üç kez yanlış şifre girdiniz. Program sonlanıyor.")


# In[ ]:




