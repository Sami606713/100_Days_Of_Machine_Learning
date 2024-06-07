import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from mlxtend.plotting import plot_decision_regions
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
import streamlit as st

# This code snippet is loading the Iris dataset using the `load_iris()` function from scikit-learn's
data=load_iris()
feature=data.data
target=data.target

df1=pd.DataFrame(feature,columns=data.feature_names)
df2=pd.Series(target)

final=pd.concat([df1,df2],axis=1).rename(columns={0:"target"})
final=final[["sepal length (cm)",'petal width (cm)',"target"]]


# st.title("Logistic Regression Hyperparameter")
with st.sidebar:
    st.header("Hyperparameter")
    class_=st.sidebar.selectbox("class", ["Binary","Multiclass"])
    penalty = st.sidebar.selectbox("Penalty", ["l1", "l2", "elasticnet", "none"])
    dual = st.sidebar.selectbox("dual", [True,False])
    class_weight = st.sidebar.selectbox("dual", ['balanced',None])
    C=st.sidebar.number_input("Inverse of regularization strength (C)")
    solver = st.sidebar.selectbox("Solver", ["newton-cg", "lbfgs", "liblinear", "sag", "saga"])
    max_iter = st.sidebar.number_input("Maximum number of iterations", 100, 10000, step=100)
    tune_button = st.button("Tune")

if class_=="Binary":
    final=final[(final["target"]==0) | (final["target"]==1)]
if class_=="Multiclass":
    final=final

from sklearn.model_selection import train_test_split,cross_val_score
x_train,x_test,y_train,y_test=train_test_split(final.drop(columns=['target']),final['target'],test_size=0.2,random_state=35)

if tune_button:
    # Fit the logistic regression model using training data
    model = LogisticRegression(penalty=penalty,solver=solver,max_iter=max_iter,C=C,dual=dual,class_weight=class_weight)
    model.fit(x_train, y_train)  # Use y_train here instead of y_test

   # Create scatter plot with Plotly
    fig = plt.figure(figsize=(10, 6))
    plot_decision_regions(x_train.values, y_train.values, clf=model, legend=2)
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Width (cm)")
    plt.title("Decision Boundary")
    st.pyplot(fig)

else:
     # # Create scatter plot with Plotly
    fig = px.scatter(final, x="sepal length (cm)", y="petal width (cm)", color="target",
                    labels={"sepal length (cm)": "Sepal Length (cm)", "petal width (cm)": "Petal Width (cm)", "target": "Target"})

    st.plotly_chart(fig)
