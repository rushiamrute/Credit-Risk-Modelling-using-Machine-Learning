# Import neccessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy.stats import chi2_contingency
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, precision_recall_fscore_support
import warnings
import os

# load the dataset

d1= pd.read_excel(r"C:\Users\rushi\OneDrive\Desktop\Credit Risk Project\Data\case_study1.xlsx")

d2 = pd.read_excel(r"C:\Users\rushi\OneDrive\Desktop\Credit Risk Project\Data\case_study2.xlsx")

df1 = d1.copy()
df2 = d2.copy()


# Remove Nulls 
df1 = df1.loc[df1['Age_Oldest_TL']!= -99999]