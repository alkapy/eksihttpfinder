# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup
import requests
import re

linkveisim = sys.argv

if len(linkveisim) > 2:
    linkial = linkveisim[1]
    dosyaismi = linkveisim[2]
else:
    linkial = linkveisim[1]
    urlbol = linkveisim[1].split("/")
    dosyaismi = urlbol[3]

 

def httpgetir(baslik_url, sayfa=1):
	baslik_url = linkial
	sayfaLinki = baslik_url
	if sayfa != 1:
		sayfaLinki += "?p=%s" % sayfa
	sayfayiAl = requests.get(sayfaLinki)
	icerik = BeautifulSoup(sayfayiAl.content, "html.parser") #BeautifulSoup ile linkin kaynağını alıyoruz
	sayfalama = icerik.select(".pager") #sayfalama bölümünden maksimum sayfa sayısını alıyoruz (başlığı baştan sona taraması için)
	sonSayfa = sayfalama[0]["data-pagecount"] #en son sayfa sayısı
	sonSayfa = int(sonSayfa)
	
	icerik = BeautifulSoup(sayfayiAl.content, "html.parser") #BeautifulSoup ile linkin kaynağını alıyoruz

	sayfaici = icerik.find_all("a", href=True) #sayfa kaynağının içerisinde ki "a" taglarını alıyoruz
	
	"""
	rr = re.compile('(?<=href=").*?(?=")')
	links = rr.findall(sayfayiAl.content)

	for link in links:
		if "http" in link and not "google" in link:
			print link

	"""
	for link in sayfaici:
		linkListesi = link.get('href')
		if "http" in linkListesi and not "eksisozluk" in linkListesi and not "twitter.com/sozluk" in linkListesi:
			dosya = open(dosyaismi+".txt", "a")
			dosya.write(linkListesi)
			dosya.write("\n")
			#else:
			#	print(link.get('href'))

	
	sayfa += 1
	if sayfa <= sonSayfa:
		httpgetir(baslik_url, sayfa=sayfa)
	
	
	

httpgetir(linkial)
