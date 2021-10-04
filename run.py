import requests
import yagmail
from settings import settings_dict

while True:
    response = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
    temp = response.json()
    price = temp['data']['amount']
    print("Aktualna cena: ", price)
    desired = (input("Podaj cene przy ktorej dostaniesz maila (w USD, 'exit' zeby wyjsc):  "))
    if desired == "exit":
        break

    while float(desired) > float(price):
        response = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
        temp = response.json()
        price = temp['data']['amount']
        print("Aktualna cena:  ", price)
    else:
        yag = yagmail.SMTP(settings_dict['login'], settings_dict['password'])
        contents = [f'Cena Bitcoina wynosi teraz ${price}',
                    f'Przekroczyla zadana cene ${desired}']
        yag.send(settings_dict['receiver'], f'Cena bitcoina wynosi ${price}', contents)
        print("----- Wyslano maila -----")