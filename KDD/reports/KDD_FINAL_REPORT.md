# KDD Customer Segmentation Final Report

## 1. Selection

The Customer Personality Analysis dataset was selected from Kaggle:

[Customer Personality Analysis Dataset](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

The dataset contains demographic, spending, purchasing, and marketing campaign information.

The original dataset contained 2,240 records and 29 columns. Since this is an unsupervised learning project, no prediction target was used for clustering.

## 2. Preprocessing

The dataset was loaded as a tab-separated file.

During data-quality inspection:

- No duplicate records were found.
- Twenty-four missing values were found in `Income`.
- Two unrealistic birth-year records were identified and removed.
- Missing income values were replaced with the median income.
- `ID`, `Z_CostContact`, and `Z_Revenue` were removed.

After cleaning, the dataset contained 2,238 records and 26 columns with no remaining missing values.

## 3. Transformation

The following features were created:

- `Age`
- `Children_Total`
- `Total_Spending`
- `Total_Purchases`
- `Total_Campaign_Accepted`

Nine features were selected for clustering:

- Age
- Income
- Children_Total
- Recency
- Total_Spending
- Total_Purchases
- NumDealsPurchases
- NumWebVisitsMonth
- Total_Campaign_Accepted

`Income`, `Total_Campaign_Accepted`, and `NumDealsPurchases` were right-skewed, so a `log1p` transformation was applied. All selected features were then standardized using `StandardScaler`.

## 4. Data Mining

K-Means clustering was evaluated using values of `k` from 2 through 10.

The silhouette score was highest for two clusters:

- `k = 2`: 0.2702
- `k = 5`: 0.1765

Although five clusters provided more detailed segments, the two-cluster solution produced better separation and was easier to interpret. Therefore, `k = 2` was selected.

## 5. Final Results

The final clusters contained:

- Cluster 0: 1,326 customers
- Cluster 1: 912 customers

### Cluster Interpretation

Cluster 0 represents lower-value customers:

- Average income: 38,307.35
- Average spending: 193.55
- Average purchases: 7.80
- Response rate: 10.18%

Cluster 1 represents higher-value customers:

- Average income: 72,449.07
- Average spending: 1,204.46
- Average purchases: 19.44
- Response rate: 21.82%

Cluster 1 customers have higher income, substantially higher spending, more purchases, and a higher marketing response rate.

The `Response` column was used only to interpret the clusters after clustering. It was not used to create the clusters.

## 6. Conclusion

The KDD process successfully identified two meaningful customer segments. The results suggest that the company can use different marketing strategies for lower-value and higher-value customers.

The trained K-Means model was also tested through `KDD/deployment/predict.py`. A sample customer was assigned to Cluster 1, the higher-value customer segment.

Saved project artifacts include:

- K-Means model
- Standardization scaler
- Customer cluster assignments
- Segment summary
- Deployment script
