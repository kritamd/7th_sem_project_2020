#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# In[2]:


dataset=pd.read_csv('heart1.csv')
dataset.head()


# In[3]:


X=dataset.drop(['target'],axis=1).values
y=dataset.target.values


# In[4]:


#splitting dataset into training set and test set

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.25,random_state=42)


# In[5]:


#feature scaling

from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)


# In[6]:


from sklearn.linear_model import LogisticRegression


# In[7]:



classifier =LogisticRegression()
classifier.fit(X_train,Y_train)
predictions=classifier.predict(X_test)


# In[9]:


#Saving the model to disk
import joblib

filename = 'Logistic_regression_model.pkl'
joblib.dump(classifier,filename)


# In[13]:


filename='standard_scalar.pkl'
joblib.dump(sc_X,filename)


# In[10]:


from sklearn.metrics import accuracy_score
score = accuracy_score(Y_test,predictions)
print(score)


# In[11]:


# Making the Confusion Matrix

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, predictions)
print(cm)


# In[12]:



from sklearn.metrics import classification_report
print(classification_report(Y_test,predictions))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




