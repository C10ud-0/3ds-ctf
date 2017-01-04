Ilk olarak direk username=' ve password=' girdiğimizde bize Syntax hatasını ve arkada dönen SQL kodunu döndürüyor.
![ht]()

Burda yapmamız gerek tek şey kodu aşağıdaki şekle getirmek:

```
SELECT * FROM users WHERE username='' or '1'='1' AND password='' or '1'='1' 

```
Ve sonuç:
![ht]()

Burda girdiğimiz ' or '1'='1 bize username ve passwordun TRUE olduğu ilk değeri kullanarak giriş yapmamızı sağlıyor.Zira "1" her zaman "1" eşit,burda 1 değilde başka herhangi bir değerde kullanabilirdik sonucu true yapacak şekilde 'a'='a gibi.
