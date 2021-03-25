#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.öğrenci
vize1 = int(input("Vize Notunuzu giriniz:"))
proje1 = int(input("Proje Notunuzu giriniz:"))
final1 = int(input("Final Notunuzu giriniz:"))
gecme_notu1 = (vize1*30/100)+(proje1*30/100)+(final1*40/100)
print("gecme_notu1:", gecme_notu1)

#2.öğrenci
vize2 = int(input("Vize Notunuzu giriniz:"))
proje2 = int(input("Proje Notunuzu giriniz:"))
final2 = int(input("Final Notunuzu giriniz:"))
gecme_notu2 = (vize2*30/100)+(proje2*30/100)+(final2*40/100)
print("gecme_notu2:", gecme_notu2)

#3.öğrenci
vize3 = int(input("Vize Notunuzu giriniz:"))
proje3 = int(input("Proje Notunuzu giriniz:"))
final3 = int(input("Final Notunuzu giriniz:"))
gecme_notu3 = (vize3*30/100)+(proje3*30/100)+(final3*40/100)
print("gecme_notu3:", gecme_notu3)

#4.öğrenci
vize4 = int(input("Vize Notunuzu giriniz:"))
proje4 = int(input("Proje Notunuzu giriniz:"))
final4 = int(input("Final Notunuzu giriniz:"))
gecme_notu4 = (vize4*30/100)+(proje4*30/100)+(final4*40/100)
print("gecme_notu4:", gecme_notu4)

#5.öğrenci
vize5 = int(input("Vize Notunuzu giriniz:"))
proje5 = int(input("Proje Notunuzu giriniz:"))
final5 = int(input("Final Notunuzu giriniz:"))
gecme_notu5 = (vize5*30/100)+(proje5*30/100)+(final5*40/100)
print("gecme_notu5:", gecme_notu5)

not_listesi = [gecme_notu1, gecme_notu2, gecme_notu3, gecme_notu4, gecme_notu5]

not_listesi.sort(reverse=True)
print('Sorted list:', not_listesi)


# In[ ]:




