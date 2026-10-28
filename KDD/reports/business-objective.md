# KDD Business Objective

## Business Problem

The company wants to better understand its customers based on their demographics, purchasing behavior, spending patterns, and campaign interactions.

Treating all customers the same may lead to inefficient marketing. Customer segmentation can help the company design more relevant marketing strategies for different groups.

## Project Objective

The objective of this project is to identify meaningful customer segments using unsupervised data-mining techniques.

Customers will be grouped according to characteristics such as:

- Income
- Age
- Household composition
- Product spending
- Purchase channels
- Website visits
- Discount purchases
- Campaign responses

## Business Value

The customer segments can help the company:

- Create targeted marketing campaigns.
- Identify high-value customers.
- Understand customer spending behavior.
- Improve product recommendations.
- Allocate marketing resources more efficiently.
- Develop personalized promotions.

## Data Mining Task

The primary data-mining task is customer segmentation using clustering.

The project will apply the K-Means clustering algorithm to group customers with similar characteristics.

The number of clusters will be evaluated using:

- The elbow method.
- Silhouette score.
- Cluster size.
- Business interpretability.

## Target Variable

This is an unsupervised learning project. Therefore, there is no target variable used to train the clustering model.

The `Response` column will not be used as a prediction target. It may be used later to help interpret and profile the resulting customer segments.

## Dataset

The project uses the Customer Personality Analysis dataset from Kaggle.

The dataset contains customer information related to:

- Demographics
- Household characteristics
- Product spending
- Purchase behavior
- Marketing campaign responses

## KDD Process

The project will follow these KDD phases:

1. Selection
2. Preprocessing
3. Transformation
4. Data Mining
5. Interpretation and Evaluatio
