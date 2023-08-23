# Find-the-desired-car-using-scikit-learn


![scikit-learn-using-python](https://github.com/Peyman2012/Find-the-desired-car-using-scikit-learn/assets/88220773/f089130c-382c-4ccb-852d-3cd06da56bf1)


**Find the desired car using scikit-learn**

We cannot use classification in this project because the classifier generally separates distinct classes, and so this classifier expects a string or an integer type to distinguish different classes from each other (this is called the "target " Is known). You can read more about this in Introduction to Classifiers.

The problem we are trying to solve is to determine a continuous numerical output, Result. This is known as a regression problem, so we need to use a regression algorithm (such as DecisionTreeRegressor).

      clf = tree.DecisionTreeRegressor()
      clf = clf.fit(x, y)
      new_data = [[search_name, search_color_ex, search_color_in, search_person, m_input, y_input, a_input, o_input]]
      new_data_1.append(new_data)
      answer = clf.predict(new_data)


Encoding the code means that it works with numbers in scikit-learn, and the strings must be converted into code, which will be done using the following library:

      from sklearn import preprocessing
      le = preprocessing.LabelEncoder()
      le.fit(Name_car)
      df['NameCar_label'] = le.transform(Name_car)
      Name_label=df['NameCar_label']

To search for a value in the columns of the data set, we use the following code:

      df_price = df[df['Price Car'] ==answer[i]]
        search_price=df_price['Name Car'].tolist()
        search_color_ex=df_price['Color Exterior'].tolist()
        search_color_in = df_price['Color Interior'].tolist()
        search_model=df_price['Model Car'].tolist()
        search_person=df_price['Person Car'].tolist()
      
This code gives the number of answers requested:

      for i in range(len(new_data_1)):
          print(f'Car: {name[i]} ==> Price : {ans[i][0]}')

Link to the dataset I collected in Keggle:

https://www.kaggle.com/datasets/peimandaii/buy-car
