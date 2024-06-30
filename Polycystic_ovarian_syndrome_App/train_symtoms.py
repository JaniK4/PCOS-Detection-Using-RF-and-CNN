import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import svm

def process(X_test):
    print(X_test)
    dataset=pd.read_csv('media/features.csv')
    dataset.shape
    X=np.array(dataset.iloc[:,:-1])
    X=X.astype(dtype='int')
    Y=np.array(dataset.iloc[:,-1])
    Y=Y.reshape(-1,)

    X_train, X_test, y_train, y_test =train_test_split(X,Y,test_size=0.25,
                                                    random_state=42)
    # import seaborn as sb
    # import joblib
    print(X_train.shape)

    model_RR=RandomForestClassifier(n_estimators=100,random_state=42)
    model_RR.fit(X_train,y_train)
    # joblib.dump(model_RR, "RF_model.joblib")
    # X_test=[0,0,0,0,1,1,0,1,1]

    y_predicted_RR=model_RR.predict(np.asarray(X_test).reshape(1,-1))
    print(y_predicted_RR)
    confusion=confusion_matrix(y_test,y_predicted_RR)
    print(accuracy_score(y_test,y_predicted_RR))





