#Import models from scikit learn module:
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression ## Importing the logistic regression model from the scikit -learn

df = pd.read_csv("sachine_score_in_last_20_matches.csv") ## Reading the csv file having Odi, and Score as header
scores = df.Score # taking the Scores into a list
scores_arr = np.array(scores) ## taking the scores into an numpy array

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from sklearn import metrics

def classification_model(model, data, predictors, outcome):
  model.fit(data[predictors],data[outcome]) #Fit the model
  
  predictions = model.predict(data[predictors])#Make predictions on training set
  
  accuracy = metrics.accuracy_score(predictions,data[outcome]) #Print accuracy
  print "Accuracy : %s" % "{0:.3%}".format(accuracy)

  kf = KFold(data.shape[0], n_folds=5) #Perform k-fold cross-validation with 5 folds
  error = []
  for train, test in kf:
    
    train_predictors = (data[predictors].iloc[train,:]) # Filter training data
    
    train_target = data[outcome].iloc[train] # The target we're using to train the algorithm.
    
    model.fit(train_predictors, train_target) # Training the algorithm using the predictors and target.
    
    error.append(model.score(data[predictors].iloc[test,:], data[outcome].iloc[test])) #Record error from each cross-validation run
 
  print "Cross-Validation Score : %s" % "{0:.3%}".format(np.mean(error))

  model.fit(data[predictors],data[outcome]) #Fit the model again so that it can be refered outside the function:

outcome_var = 'Score'
model = LogisticRegression()
predictor_var = ['Score','ODI']
classification_model(model, df,predictor_var,outcome_var)

