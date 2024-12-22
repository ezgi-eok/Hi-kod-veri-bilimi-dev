#!/usr/bin/env python
# coding: utf-8

# ## 1. Dairenin Alanını Hesaplayan Fonksiyon

# In[1]:


# Dairenin alanını hesaplayan fonksiyon
def daire_alani(pi, yaricap):
    alan = pi * (yaricap ** 2)
    return alan

# Kullanıcıdan pi ve yarıçap bilgisi al
pi_degeri = float(input("Pi değerini giriniz: "))
yaricap = float(input("Yarıçapı giriniz: "))

# Alanı hesapla ve yazdır
alan = daire_alani(pi_degeri, yaricap)
print(f"Dairenin alanı: {alan:.2f}")


# ## 2. Faktöriyel Hesaplayan Fonksiyon

# In[2]:


# Faktöriyel hesaplayan fonksiyon
def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc

# Kullanıcıdan sayı al ve faktöriyeli hesapla
sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz: "))
fakt = faktoriyel(sayi)
print(f"{sayi}! = {fakt}")


# ## 3. Yas Hesaplayan Fonksiyon

# In[3]:


# Yaşı hesaplayan fonksiyon
def yas_hesapla(dogum_yili):
    mevcut_yil = 2024
    yas = mevcut_yil - dogum_yili
    return yas

# Kullanıcıdan doğum yılı al ve yaşı hesapla
dogum_yili = int(input("Doğum yılınızı giriniz: "))
yas = yas_hesapla(dogum_yili)
print(f"Yaşınız: {yas}")


# ## 4. Emeklilik Belirleyen Fonksiyon

# In[4]:


# Yaşı hesaplayan fonksiyon
def yas_hesapla(dogum_yili):
    mevcut_yil = 2024
    yas = mevcut_yil - dogum_yili
    return yas

# Emeklilik durumunu belirleyen fonksiyon
def emeklilik_durumu(isim, dogum_yili):
    yas = yas_hesapla(dogum_yili)
    if yas >= 65:
        print(f"{isim}, emekli oldunuz.")
    else:
        kalan_yil = 65 - yas
        print(f"{isim}, emekliliğinize {kalan_yil} yıl kaldı.")

# Kullanıcıdan isim ve doğum yılı al
isim = input("İsminizi giriniz: ")
dogum_yili = int(input("Doğum yılınızı giriniz: "))

# Emeklilik durumunu hesapla ve yazdır
emeklilik_durumu(isim, dogum_yili)


# In[ ]:




