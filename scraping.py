import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

Miles = []
color_exterior = []
color_interior = []
color_car = []
year_car = []
name_car = []
model_car = []
price_car=[]
accident_car=[]
owner_car=[]
person_car=[]
len_car=0
pages = 200

for i in range(1,pages+1):
    url='https://www.truecar.com/used-cars-for-sale/listings/?buyOnline=true&page='+str(i)
    print(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.text)

    car = soup.find_all('div',attrs={'class':'linkable card card-shadow vehicle-card'})
    # print(home[0].text)
    machin_name = soup.find_all('div', attrs={'class': 'vehicle-card-top'})
    machin_info = soup.find_all('div', attrs={'class': 'mt-2-5 w-full border-t pt-2-5'})
    machin_mile=soup.find_all('div', attrs={'data-test': 'vehicleMileage'})
    machin_price = soup.find_all('span', attrs={'data-test': 'vehicleListingPriceAmount'})
    machin_n = soup.find_all('span', attrs={'class': 'truncate'})
    machin_model = soup.find_all('div', attrs={'data-test': 'vehicleCardTrim'})
    machin_report=soup.find_all('div', attrs={'data-test': 'vehicleCardCondition'})
    for i in range(len(car)):
        Miles.append(re.findall('(\d.+|\d)\s[m]', machin_mile[i].text))
        year_car.append(re.findall('(20\d{2}|19\d{2})\s', machin_name[i].text))
        color_exterior.append(re.findall('[,]\s\w{2}(.+)[,]', machin_info[i].text))
        color_interior.append(re.findall('[i][o][r][,]\s(\w.+)', machin_info[i].text))
        name_car.append(re.findall('(\w.+)', machin_n[i].text))
        model_car.append(re.findall('(.+)', machin_model[i].text))
        price_car.append(re.findall('[$](\d.+)', machin_price[i].text))
        accident_car.append(re.findall('([N][o]|\d)\s[a]', machin_report[i].text))
        owner_car.append(re.findall('[,]\s(\d)\s[O]', machin_report[i].text))
        person_car.append(re.findall('\s([F].+|[P].+)', machin_report[i].text))
    # for i in range(len(car)):
    #     print(machin_report[i].text)
    len_car=len(car)+len_car
    # print(len(car))
    # print(len(machin_mile))
    # print(Miles)




miles_Car = []
price_Car=[]

Miles_Car = []
Name_Car=[]
Color_Exterior=[]
Color_Interior=[]
Year_Car=[]
Model_Car=[]
Price_Car=[]
Accident_Car=[]
Owner_Car=[]
Person_Car=[]
print(len(name_car))
print(len(model_car))
print(len(color_interior))
print(len(color_exterior))
print(len(Miles))
print(len(price_car))
print(len(accident_car))
print(len(owner_car))
print(len(person_car))

for i in range(len_car):
    Name_Car.append(name_car[i][0])
    Model_Car.append(model_car[i][0])
    Color_Exterior.append(color_exterior[i][0])
    Color_Interior.append(color_interior[i][0])
    price_Car.append(price_car[i][0])
    Year_Car.append(int(year_car[i][0]))
    miles_Car.append(Miles[i][0])
    Miles_Car.append(float(miles_Car[i].replace(",", ".")))
    Price_Car.append(float(price_Car[i].replace(",", ".")))
    Person_Car.append(person_car[i][0])
    Owner_Car.append(int(owner_car[i][0]))
    if accident_car[i][0]=='No':
        Accident_Car.append(0)
    else:
        Accident_Car.append(int(accident_car[i][0]))


# print(Name_Car)
# print(Miles_Car)
# print(Model_Car)
# print(Color_Exterior)
# print(Color_Interior)
# print(Price_Car)
# print(Year_Car)
# print(Accident_Car)
# print(Owner_Car)
# print(Person_Car)



dict_car={'Name Car':Name_Car,'Model Car':Model_Car,'Color Exterior':Color_Exterior
          ,'Color Interior':Color_Interior,'Person Car':Person_Car,'Miles Car':Miles_Car
          ,'Year Car':Year_Car,'Accident Car':Accident_Car,'Owner Car':Owner_Car
          ,'Price Car':Price_Car}

df=pd.DataFrame(dict_car)
print(df)
df.to_csv('Write_to_database_for_use_from_BuyCar.csv',index=False)






