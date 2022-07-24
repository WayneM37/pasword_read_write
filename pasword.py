"""You can read-Write-store 8 digit paswords, with alpha-numeric and special chars."""

import json
import random

dict_1 = {"şifre_1": "dlfei*-er", "şifre_2": "jdfkladf-o"}

with open("pasword.json", "r+", encoding="utf-8") as origin:
    temp_1 = json.loads(origin.read())
    origin.close()

ans=""
entry = input("Please enter the name for pasword you are looking for: ").title()


if entry in temp_1:
    ans= temp_1[entry]
    print(entry, ":", ans)
else:
    print(f"Pasword {entry} is not in our data.")

    while True:
        ask= input(f"Would you like to create a 8 digit pasword for {entry}, Please write 'Yes or No': ").title()
        if ask == "Yes" :
            uppers = [chr(random.randint(65,90)) for i in range(2)]  # code u 3 defa çalıştırsın diye range 3 yaptık.
            low = [chr(random.randint(97,122)) for i in range(2)]
            num = [chr(random.randint(48,57)) for i in range(2)]
            schar = [chr(random.randint(33,47)) + chr(random.randint(58,64))] #buradan farklı aralıklarda 1 er tane özel karakter
            pasword_1 = "".join(uppers) + "".join(low) + "".join(num) + "".join(schar) # boş stringe üretilenleri atadık.
            temlist = list(pasword_1)
            ab = random.shuffle(temlist)
            a ="".join(temlist)
            dict_1.update({entry:a})

            with open("pasword.json", "w", encoding="utf-8") as origin: #python klasoru üçerisinde pasword.json dosyası açıyoruz.
                origin.write(json.dumps(dict_1))
                origin.close()
                print(f"You have created the pasword; {entry} : {a}")
                break
        elif ask == "No":
            print("Have Goodday!!!")
            break
        else:
            print("You made an incorrect entry, please try again!")
