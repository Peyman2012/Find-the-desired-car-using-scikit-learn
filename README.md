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

This code is encoded to search the input and find the value from the column:

     search_name = df.loc[df['Name Car'] == n_input, 'NameCar_label'][0]
     search_color_ex = df.loc[df['Color Exterior'] == c_ex_input, 'ColorCarEx_label'][0]
     search_color_in = df.loc[df['Color Interior'] == c_in_input, 'ColorCarEx_label'][0]
     search_person = df.loc[df['Person Car'] == p_input, 'Person_label'][0]

Encoding the code means that it works with numbers in scikit-learn, and the strings must be converted into code, which will be done using the following library:

      from sklearn import preprocessing
      le = preprocessing.LabelEncoder()
      le.fit(Name_car)
      df['NameCar_label'] = le.transform(Name_car)
      Name_label=df['NameCar_label']
