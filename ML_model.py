## machine learning libraries and functions
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# pandas
import pandas as pd

#saving model
import pickle 


#load the dataset
iris_bunch=load_iris() ## it is bunch object works like dictionary
#print(iris_bunch)

iris_df=pd.DataFrame(iris_bunch['data'], columns=iris_bunch['feature_names'])
#print(iris_df.head(3))

target=iris_bunch['target']

## split the train and the test
X_train, X_test, y_train , y_test=train_test_split(iris_df, target, random_state=1, test_size=0.2)

## create the model
logistic=LogisticRegression(max_iter=1000)

## train it
logistic.fit(X_train, y_train)

## prediction
print(logistic.predict(X_test))

## evaluate
#print(logistic.score(X_test, y_test))

## save the model
pkl_file="logistic_model.p"

with open(pkl_file, 'wb') as file:
    pickle.dump(logistic, file)


