"""You can read-Write-store 8 digit paswords, with alpha-numeric and special chars.""" 
# Aşağıdaki yapı ile json dosyasındaki sözlüğün üzerine yazmak yerine yeni kullanıcı - password ikilileri ekleme yapılabiliyor.

import json
import random

with open("pasword.json", encoding="utf-8") as origin:
    # print(origin.read())
    # origin.seek(0)
    pwd_dict = json.loads(origin.read())
    """
    If you have a JSON string, you can parse it by using the json.loads() method.

    The result will be a Python dictionary.

    Syntax : json.loads(s)

    Argument: it takes a string, bytes, or byte array instance which contains the JSON document as a parameter (s).

    Return: It returns a Python dictionary.
    """

pwd=""
entry = input("Please enter the name for pasword you are looking for: ").title()


if entry in pwd_dict:
    pwd = pwd_dict[entry]
    print(entry, ":", pwd)
else:
    print(f"Pasword {entry} is not in our data.")
    
    while True:
        ask= input(f"Would you like to create a 8 digit pasword for {entry}, Please write 'Yes or No': ").title()
        if ask == "Yes" :
            uppers = [chr(random.randint(65,90)) for i in range(2)]  # code u 3 defa çalıştırsın diye range 3 yaptık. 
            low = [chr(random.randint(97,122)) for i in range(2)] 
            num = [chr(random.randint(48,57)) for i in range(2)]
            schar = [chr(random.randint(33,47)) , chr(random.randint(58,64))] #buradan farklı aralıklarda 1 er tane özel karakter
            pasword_1 = "".join(uppers) + "".join(low) + "".join(num) + "".join(schar) # boş stringe üretilenleri atadık. 
            templist = list(pasword_1)
            ab = random.shuffle(templist)
            a ="".join(templist)     
            
            pwd_dict[entry] = a
    
            with open("pasword.json", "w", encoding="utf-8") as origin: #python klasoru üçerisinde pasword.json dosyası açıyoruz. 
                """
                If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
                You can convert Python objects of the following types, into JSON strings:
                dict
                list
                tuple
                string
                int
                float
                True
                False
                None
                """
                origin.write(json.dumps(pwd_dict, 
                                        sort_keys=True, 
                                        indent=4, separators=(',', ': ')))
                print(f"You have created the pasword; {entry} : {a}")
                break
        elif ask == "No":
            print("Have a good day!")
            break
        else:
            print("You made an incorrect entry, please try again!")
