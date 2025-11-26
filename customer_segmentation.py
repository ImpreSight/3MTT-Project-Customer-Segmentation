# Import essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Machine learning and preprocessing
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# Load dataset
df = pd.read_csv("Users\Erakab Edimulo\Desktop\3MTT_PROJECT\customer_segmentation_data.csv")  # Replace with your file path or Kaggle link if using API
df.head()

# View basic info
df.info()

# Check for missing values
print(df.isnull().sum())

# Check duplicates
print(f"Duplicate rows: {df.duplicated().sum()}")

# Handle missing values or duplicates if found
df.drop_duplicates(inplace=True)
# 
df['income'].fillna(df['income'].median(), inplace=True)