Yazıyı tekrar tekrar okuyarak bi hint aradım fakat "stealing feds' letters. Ooh this message." i görmem zor oldu daha sonra abest olan bu metnin harflerine bakmaya başladım,hızlı olması için sadece ilk 4 kelimeyi inceleyerek 3.harflerinde "i" "r" "o" "c" kısmına baktıktan sonra emin oldum ve kısa bi kod yazdım sonuç resimdeki gibi çıktı.Tek yapmam gereken kelime aralarına boşluk koymak oldu.

```
metin = "Flies were floating, recieving acknowledge, stealing feds' letters. Ooh this message. Back: ooh drawings! Will solutions keeps hanging bags there?"
cikti = ""
sayac=0
while(sayac<3):
	for i in metin.lower().split():
		cikti += i[sayac]
	print(cikti,"\n")
	cikti=""
	sayac=sayac+1
  ```


![hbh](https://raw.githubusercontent.com/C10ud-0/ctf/master/hellboundhackers/stega/4/4.png)
