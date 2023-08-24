import pandas as pd
from sklearn import tree
import time
df=pd.read_csv('C:\\Users\\peyman\\pythonProject16\\Write_price_car_from_database_for.csv')
# print(df.head())


n_input=''
y_input=0
m_input=0.0
a_input=0
o_input=0
max_price=0.0
min_price=0.0

n=int(input('Enter a number: '))

Miles_Car=df['Miles Car']
Year_Car=df['Year Car']
Accident_Car=df['Accident Car']
Owner_Car=df['Owner Car']
Price_Car=df['Price Car']
Name_car=df['Name Car']
Color_Exterior=df['Color Exterior']
Color_Interior=df['Color Interior']
Person_Car=df['Person Car']
Model_Car = ['Model Car']

x=[]
y=[]


for i in range(len(df)):
    x.append([Miles_Car[i],Year_Car[i],Accident_Car[i],Owner_Car[i]])
    y.append([Price_Car[i]])



print("Please waite....")
time.sleep(2)
print()



print('''Hello .....
The specifications of the car :''')
time.sleep(2)


for i in range(n):
    y_input = int(input("Enter a Year:"))
    m_input = float(input("Enter a Miles:"))
    a_input = int(input("Enter a Accident:"))
    o_input = int(input("Enter a Owners:"))
    max_price = float(input("Your maximum payment: "))
    min_price = float(input("Your minimum payment: "))
    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(x, y)
    new_data = [[m_input, y_input, a_input, o_input]]
    answer = clf.predict(new_data)
    list_answer = []
    for item in answer:
        list_answer.append(item)
    print(f'''So....
    The specifications of the car you want are:
    Car year: {y_input}
    Car operation: {m_input} Miles
    Number of accidents: {a_input}
    Number of owners: {o_input} person
    Min Price {min_price} and Max Price: {max_price}''')
    print("Please waite....")
    time.sleep(10)
    print()
    print("Result : ")
    if list_answer[0] >= min_price and list_answer[0] <= max_price:
        df_price = df[df['Price Car'] == list_answer[0]]
        search_price = df_price['Name Car'].tolist()
        search_color_ex = df_price['Color Exterior'].tolist()
        search_color_in = df_price['Color Interior'].tolist()
        search_model = df_price['Model Car'].tolist()
        search_person = df_price['Person Car'].tolist()
        print(f'''Name Car: {search_price[0]}   and     
    Model Car : {search_model[0]}   and              
    Color Exterior : {search_color_ex[0]}   and        ==> Price Car : {list_answer[0]}$
    Color Interior :{search_color_in[0]} and      
    Person Car : {search_person[0]}
     ''')
    else:
        print(f'''We are sorry!!!!
    The car is not available at the price you want
    The car with the specifications you asked for is available at the price: {list_answer[0]}$''')

