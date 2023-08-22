import pandas as pd
from sklearn import tree
from sklearn import preprocessing
df=pd.read_csv('C:\\Users\\peyman\\pythonProject16\\Write_price_car_from_database_for.csv')
# print(df.head())

Miles_Car=df['Miles Car']
Year_Car=df['Year Car']
Accident_Car=df['Accident Car']
Owner_Car=df['Owner Car']
Price_Car=df['Price Car']
Name_car=df['Name Car']
Color_Exterior=df['Color Exterior']
Color_Interior=df['Color Interior']
Person_Car=df['Person Car']

le = preprocessing.LabelEncoder()
le.fit(Name_car)
df['NameCar_label'] = le.transform(Name_car)
Name_label=df['NameCar_label']

le.fit(Color_Exterior)
df['ColorCarEx_label'] = le.transform(Color_Exterior)
ColorEX_label=df['ColorCarEx_label']

le.fit(Color_Interior)
df['ColorCarEx_label'] = le.transform(Color_Interior)
ColorIN_label=df['ColorCarEx_label']

le.fit(Person_Car)
df['Person_label'] = le.transform(Person_Car)
Person_label=df['Person_label']

x=[]
y=[]
# print(ColorIN_label)
for i in range(len(df)):
    x.append([Name_label[i],ColorEX_label[i],ColorIN_label[i],Person_label[i],Miles_Car[i],Year_Car[i],Accident_Car[i],Owner_Car[i]])
    y.append([Price_Car[i]])


ans=[]
name=[]
n=int(input("Enter a number: "))
new_data_1=[]
for i in range(n):
    n_input = input("Enter a car: ")
    c_ex_input = input("Enter a color ex car : ")
    c_in_input = input("Enter a color in car : ")
    p_input = input("Enter a personal car : ")
    y_input = int(input("Enter a year car : "))
    m_input = float(input("Enter a miles car: "))
    a_input = int(input("Enter a accident car: "))
    o_input = int(input("Enter a owner car: "))
    search_name = df.loc[df['Name Car'] == n_input, 'NameCar_label'][0]
    search_color_ex = df.loc[df['Color Exterior'] == c_ex_input, 'ColorCarEx_label'][0]
    search_color_in = df.loc[df['Color Interior'] == c_in_input, 'ColorCarEx_label'][0]
    search_person = df.loc[df['Person Car'] == p_input, 'Person_label'][0]
    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(x, y)
    new_data = [[search_name, search_color_ex, search_color_in, search_person, m_input, y_input, a_input, o_input]]
    new_data_1.append(new_data)
    answer = clf.predict(new_data)
    ans.append(answer)
    name.append(n_input)

for i in range(len(new_data_1)):
    print(f'Car: {name[i]} ==> Price : {ans[i][0]}')
