Hikayeyi okuduğumuzda bize Brett Thwaits adlı bi suçlunun füze kodlarını çaldığını ve çalıntı kodların bulunmus oldugu daha sonradan formatladığını söylüyor.Bizden istediği ise bu diskin backup dosyasını kullanarak bu kodlarıdan 4. olanı bulmamız.Çözümün tüm adımları aşağıdaki videoda göstermeye çalıştım.



[![Forensic1](https://img.youtube.com/vi/aJghHf8giKc/0.jpg)](https://youtu.be/aJghHf8giKc)




Videoda goruldugu sekilde gayet basit aslında,biraz dikkat etmek gerekiyor.Rar şifresini brute force yaparken "100" ile başlatmamın nedeni aşağıdaki resimde görüldüğü üzere kullanıcının daha önce şifre denemesi yaparken "123" ve "12345" kullanmıs olması.

![ht](https://raw.githubusercontent.com/C10ud-0/ctf/master/ht.co.uk/forensic/output/jpg/00032123.jpg)

Diğer bi noktada en sonda cevabı girerken direk kod olarak kabul etmemiş olması,daha sonra txt dosyalarından birinin içerisinde AAAA-AAAA-AAAA-AAAA
şeklinde girilmiş olduğuydu kodu bu şekilde denediğimizde cevap olarak kabul etti.
```
4C63-02F0-2715-5B46
2D98-036A-CB59-23F3
E035-E034-ACC8-D09A
AA6B-A4A8-3F67-FFF7
CA50-44C7-0BCD-17BF
```


(Çözümü girdikte sonra merak ettiğim için denedim,text dosyasındaki 4. kodu cevap olarak girmemiz bize doğru cevabı vermiyor hikayenin aksine.)

