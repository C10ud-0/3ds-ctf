metin = "Flies were floating, recieving acknowledge, stealing feds' letters. Ooh this message. Back: ooh drawings! Will solutions keeps hanging bags there?"
cikti = ""
sayac=0
while(sayac<3):
	for i in metin.lower().split():
		cikti += i[sayac]
	print(cikti,"\n")
	cikti=""
	sayac=sayac+1

