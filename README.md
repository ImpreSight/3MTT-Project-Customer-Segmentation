# 3MTT-Project-Customer-Segmentation
 This project builds an end to end customer segmentation using categorical encoders, standard scalers, PCA  and KMeans clustering. The final solution supports both training and testing on new dataset
Customer Segmentation with PCA and KMeans 

This project builds an end-to-end customer model using:
- Categorical encoders (OneHotEncoder, LabelEncoder and OrdinalEncoder)
- Standard scalers for numeric fields
- Principal Component Analysis (PCA) for dimentionality reduction
- KMeans for clustering
- Pickle for saving and loading dependencies

Project Structure
-- Importing Required Libraries and Packages
-- Loading Dataset File
-- Data Cleaning
-- Exploratory Data Analysis
-- KMeans Model Building with PCA
-- Communicating Results
-- Saving PCA trained KMeans Model

-- KMeans Model Building with feature with the Highest Variance 
-- Communicating Results

-- Testing PCA trained KMeans Model

Project Goals
-- Build a robust clustering pipeline for customer segmentation
-- Handle multiple categorical variables with appropriate encoders
-- Scale numeric data using standardscaler
-- Reduce dimensionalty with PCA - 1D component
-- Train a KMeans model on the 1-dimensional PCA feature
-- Save and load all artifacts and dependencies using pickle
-- visualize cluster distribution for both training and test data

key Concepts Used
- Categorical Encoding
-- OneHotEncoder for nominal categories
-- OrdinalEncoder for ordered categories
- Numeric Scaling
-- StandardScaler is applied only to numeric fields to normalize variance.
- Dimensionality Reduction
-- PCA converts all processed fields into a single dimension (n_components = 1), ensuring:
1. consistent representation
2. Reduce noise
3. compatibility with 1D clustering and vidualisation

- Clustering
-- KMeans groups customers based on the 1D PCA latent feature.

Visualisation
The model produces:
1. PCA 1D distribution
-- Shows how all customers lie along the 1 - component axis
2. Cluster stripplot
-- Visualizes the KMeans assignments on the reduced dimension
-- These help determine cluster separation and usefulness.


