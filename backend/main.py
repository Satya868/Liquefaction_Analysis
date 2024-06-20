# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:10:34 2024

@author: satya
"""

import os
os.chdir("C:/Program Files/Spyder")
os.chdir("D:/Summ Pro/Soll")

# D:\Summ Pro\Soll
import pandas as pd

def satya(input_from_user):
    df = pd.read_csv("data.csv")

    # print(df)

    df.drop('S. No.', inplace=True, axis=1) 

    # print(df)
    df.isnull().sum()

    df.info()
    df.tail()

    x = df.drop('Liquefied?', axis = 1)

    # print(x)

    y = df['Liquefied?']

    # print(y)


    from sklearn.model_selection import train_test_split

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1, test_size = 0.2)

    # x_train.info()
    # y_train.info()




    # Model 1 ----- 11111111-------(Logistic Regression)

    from sklearn.linear_model import LogisticRegression

    #model = LogisticRegression()
    model = LogisticRegression(max_iter=1000)

    model.fit(x_train, y_train)
    y_pred1 = model.predict(x_test)

    from sklearn.metrics import accuracy_score

    logis_reg = accuracy_score(y_test, y_pred1)

    print("Logistic Accuracy is " + str(logis_reg))

    # Logistic Accuracy score is 0.8723404255319149


    # Model 2 ---------- 22222 ----------

    from sklearn.tree import DecisionTreeClassifier
    model_2 = DecisionTreeClassifier()

    model_2.fit(x_train, y_train)

    y_pred_2 = model_2.predict(x_test)

    dec_acc = accuracy_score(y_test, y_pred_2)
    print("Decision Tree Accuracy is " + str(dec_acc))

    # decision tree accuracy score is -- .8936170212765957

    # Model 3 -- -------

    from sklearn.ensemble import RandomForestClassifier
    model_3 = RandomForestClassifier()

    model_3.fit(x_train, y_train)

    y_pred_3 = model_2.predict(x_test)

    random_fo_acc = accuracy_score(y_test, y_pred_3)

    print("Random Forest Accuracy is " + str(random_fo_acc))

    # Accuracy score is --- .8936170212765957


    import joblib

    filename = "data"

    # i have used the best models (3rd one) based on their accuracy score
    joblib.dump(model_3, 'data')

    app = joblib.load('data')


    # test sample

    item = [[7.9,	96.3,	40,	0.21,	9,	9,	0.5,	16.01,	32,	1.5,	1.5,	0]]

    # print("Here goes our predicted crop")

    ans = (app.predict(input_from_user))
    return ans

# satya()