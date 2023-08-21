import mysql.connector as msql
from mysql.connector import Error
import pandas as pd

try:
    con = msql.connect(host='127.0.0.1',
                       user='root',
                       password='peiman2012',
                       database='PriceCarBuyFromDatabase'
                       )
    if con.is_connected():
        cursor=con.cursor()
        sql = "SELECT * FROM buycarprice "
        cursor.execute(sql)
        # Fetch all the records
        result = cursor.fetchall()
        a = 0

        Miles_Car = []
        Name_Car = []
        Color_Exterior = []
        Color_Interior = []
        Year_Car = []
        Model_Car = []
        Price_Car = []
        Accident_Car = []
        Owner_Car = []
        Person_Car = []

        for car in result:
            a += 1
            Name_Car.append(car[0])
            Model_Car.append(car[1])
            Color_Exterior.append(car[2])
            Color_Interior.append(car[3])
            Person_Car.append(car[4])
            Miles_Car.append(car[5])
            Year_Car.append(car[6])
            Accident_Car.append(car[7])
            Owner_Car.append(car[8])
            Price_Car.append(car[9])
            # print(car)
        # print(a)
        dict_car = {'Name Car': Name_Car, 'Model Car': Model_Car, 'Color Exterior': Color_Exterior
            , 'Color Interior': Color_Interior, 'Person Car': Person_Car, 'Miles Car': Miles_Car
            , 'Year Car': Year_Car, 'Accident Car': Accident_Car, 'Owner Car': Owner_Car
            , 'Price Car': Price_Car}
        df = pd.DataFrame(dict_car)
        # print(df)
        df.to_csv('Write_price_car_from_database_for.csv', index=False)
except Error as e :
    print("Error while connecting to MYSQL",e)


con.close()