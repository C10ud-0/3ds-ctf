![hbh](https://raw.githubusercontent.com/C10ud-0/ctf/master/hellboundhackers/stega/5/stegano5.png)

Ilk olarak klasik resme file,exiftool,stegsolve ile baktım herhangi bi değer çıkmadı daha sonra resmi gimp ile açtım ve resimdeki değerleri teker teker beyazlar "0" ve siyahlar "1" olacak şekilde manuel sekilde decode ettim.
(Bu arada resimdeki siyahların ve beyazların birer pixel yer tuttuğunu görmüş olduk burası ilerde lazım olucak bi kenarda dursun.)


```
01000011011011110110111001100111011100100110000101110100011101010110
11000110000101110100011010010110111101101110011100110010110000100000
```

![hbh](https://raw.githubusercontent.com/C10ud-0/ctf/master/hellboundhackers/stega/5/51.png)





Ilk iki sıra bu şekilde çıktı ve "Congratu'" yazıyordu.Burda artık bi mesaj barındırdığından emin olduktan sonra manuel olarak yazmak hem zor hemde hata riski olduğundan bi python scripti oluşturdum:
```
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
      
 ```




Çıktısı aşağıdaki gibi oldu:

![hbh](https://raw.githubusercontent.com/C10ud-0/ctf/master/hellboundhackers/stega/5/52.png)

```
01000011011011110110111001100111011100100110000101110100011101010110
11000110000101110100011010010110111101101110011100110010110000100000
01011001011011110111010100100000011010000110000101110110011001010010
00000110010001101001011100110110001101101111011101100110010101110010
01100101011001000010000001110100011010000110100101110011001000000110
11010110010101110011011100110110000101100111011001010010110000100000
00100000011100000110000101110011011101000110010100100000011101000110
10000110100101110011001000000110010101101110011101000110100101110010
01100101001000000111010001101000011010010110111001100111001000000110
10010110111000100000011101000110100001100101001000000110000101101110
01110011011101110110010101110010001000000110001001101111011110000010
11000010000001100110011011110111001000100000011110010110111101110101
01110010001000000111000001101111011010010110111001110100011100110000

```
![hbh](https://raw.githubusercontent.com/C10ud-0/ctf/master/hellboundhackers/stega/5/53.png)

Bu mesajıda decode ettiğimizde bize:

"Congratulations, You have discovered this message,  paste this entire thing in the answer box, for your points�"

Cevabı geldi,yalnız bu şekilde cevabı kabul etmedi bir tane fazla boşluk var,boşluğu ve son kısmı silip "Congratulations, You have discovered this message, paste this entire thing in the answer box, for your points" şeklinde yolladığımızda puan geldi.
