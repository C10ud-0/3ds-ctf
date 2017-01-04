import os, sys
from PIL import Image

st5 = Image.open("stegano5.png")
#Pixel degerleri
width = st5.size[0] 
height = st5.size[1]

#Her pixel konumunu teker teker kontrol
for y in range(0, height): 
	row = ""
	for x in range(0, width):
		pix = st5.load()
		if pix[x,y] == 255:
			print("0",end="") #Beyaz olduğunda "0" yaz
		if pix[x,y] == 0 :
			print("1",end="") #Siyah olduğunda "1" yaz
