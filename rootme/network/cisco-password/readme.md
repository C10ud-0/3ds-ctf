Burda cisco 7 ve cisco 5 ile şifrelenmiş verileri görüyoruz direk.Yine soruda verilmiş olan kaynaklara baktığımızda temel olarak şifreleme algoritması ortaya çıkıyor.Burda bize lazım olan değer salt değeri.Bunun için önce cisco 7 şifrelerinde bulunan verileri decrypt ediyoruz ve bize aşağıdaki değerleri veriyor.
![rm](https://raw.githubusercontent.com/C10ud-0/ctf/master/rootme/network/cisco-password/hub.png)
![rm](https://raw.githubusercontent.com/C10ud-0/ctf/master/rootme/network/cisco-password/guest.png)
![rm](https://raw.githubusercontent.com/C10ud-0/ctf/master/rootme/network/cisco-password/admin.png)


````
6sK0_hub 
6sK0_admin 
6sK0_guest
```
Burdan anlaşılacağı üzere salt değerimiz "6sK0" bizden enable'ın passwordunu istiyor.Direk tahmin edilebilir şekilde "6sKO_enable" olucak fakat yine test etmek adına aşağıdaki komutu terminalde girdiğimizde bize "6sK0_enable" değerinin encrypt edilmiş halini vericek.

![rm](https://raw.githubusercontent.com/C10ud-0/ctf/master/rootme/network/cisco-password/test.png)

Görüldüğü gibi bize verilmiş olan encrypted şifre çıktı direk.Doğruladığımıza göre artık cevabı "6sK0_enable" olarak girebiliriz.
