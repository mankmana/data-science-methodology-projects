## KDD Selection Phase: Dataset Loading

The Customer Personality Analysis dataset was selected from Kaggle:

[Customer Personality Analysis Dataset](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis)

The dataset file, `marketing_campaign.csv`, was loaded successfully into a pandas DataFrame.

Because the file is tab-separated, the tab delimiter was specified while loading the data.

The initial dataset contains:

- 2,240 customer records
- 29 columns

The first five records were displayed to verify that the data loaded correctly and that the columns were read properly.

The dataset includes customer demographics, household information, spending behavior, purchase activity, and marketing campaign information.

## Initial Data Quality Check

The dataset was inspected for missing values and duplicate records.

- Duplicate rows found: 0
- Missing values were found only in the `Income` column.
- Missing `Income` values: 24.
- All other columns contained no missing values.


## Numerical Summary Findings

The numerical summary revealed the following:

- `Income` contains 2,216 non-null values, confirming 24 missing values.
- `Year_Birth` ranges from 1893 to 1996. The earliest birth years will be reviewed for possible invalid or unrealistic records.
- `Income` has a maximum value of 666,666, which may represent an extreme outlier.
- Spending variables such as `MntWines` and `MntMeatProducts` have wide ranges and possible high-value outliers.
- The purchase-channel variables have different ranges and will require scaling before clustering.
- `Z_CostContact` and `Z_Revenue` have zero standard deviation, meaning they are constant columns and will not provide useful information for clustering.
- `ID` is an identifier and should not be used as a clustering feature.

## Data Quality Findings

The inspection identified two records with birth years before 1900:

- Customer ID `11004` with birth year `1893`
- Customer ID `1150` with birth year `1899`

These values are unrealistic for the dataset and will be removed before creating the age feature.

The following constant columns were identified:

- `Z_CostContact`
- `Z_Revenue`

Because constant columns do not provide variation between customers, they will be removed before clustering.

The `ID` column will also be removed because it is only an identifier.

## Completed Initial Cleaning

The initial cleaning process produced the following results:

- Removed 2 records with unrealistic birth years.
- Imputed 24 missing `Income` values using the median income.
- Removed the identifier column `ID`.
- Removed the constant columns `Z_CostContact` and `Z_Revenue`.
- Reduced the dataset from 29 to 26 columns.
- Remaining missing values: 0.

The cleaned dataset contains 2,238 customer records and 26 columns.

## Feature Engineering Results

Five customer-level features were created:

- `Age`
- `Children_Total`
- `Total_Spending`
- `Total_Purchases`
- `Total_Campaign_Accepted`

These features summarize customer age, household composition, spending behavior, purchase activity, and campaign engagement.

The cleaned dataset increased from 26 to 31 columns after feature engineering.

The resulting dataset contains:

- 2,238 customer records
- 31 columns
- No remaining missing values

## Skewness Findings

The skewness analysis showed that `Income`, `Total_Campaign_Accepted`, and `NumDealsPurchases` are strongly right-skewed.

These features contain many lower values and a smaller number of unusually high values. A logarithmic transformation will be applied to reduce the influence of extreme values before standardization.

The remaining features have moderate or low skewness and will not be log-transformed.

## Log Transformation Results

A `log1p` transformation was applied to the strongly right-skewed features:

- `Income`
- `Total_Campaign_Accepted`
- `NumDealsPurchases`

The transformation reduced the influence of unusually large values while preserving all customer records.

The transformed dataset still contains 2,238 records and 9 selected clustering features.

## Standardization Results

The nine selected clustering features were standardized using `StandardScaler`.

After standardization:

- Each feature has a comparable scale.
- The transformed features have a mean close to 0.
- Large-range variables such as income and spending no longer dominate distance calculations.
- The final scaled dataset contains 2,238 customers and 9 features.

The data is now ready for the KDD Data Mining phase.

## Elbow Method Findings

The within-cluster sum of squares decreases as the number of clusters increases.

The largest improvements occur between two and five clusters. After approximately five clusters, the reduction becomes more gradual.

Based on the elbow plot, five clusters appear to be a reasonable starting point. The silhouette score will also be calculated before making the final decision.

## Cluster Number Evaluation

The elbow method suggested that the improvement in within-cluster variation becomes smaller after approximately five clusters.

However, the silhouette analysis produced its highest score for two clusters:

- `k = 2`: silhouette score = 0.2702
- `k = 5`: silhouette score = 0.1765

This indicates that two clusters are more clearly separated, while five clusters may provide more detailed but less distinct customer segments.

Both `k = 2` and `k = 5` will be compared using cluster sizes and customer profiles before selecting the final solution.

## Cluster Size Findings

The candidate cluster solutions produced the following group sizes:

### Two-Cluster Solution

- Cluster 0: 1,326 customers
- Cluster 1: 912 customers

### Five-Cluster Solution

- Cluster 0: 455 customers
- Cluster 1: 444 customers
- Cluster 2: 570 customers
- Cluster 3: 500 customers
- Cluster 4: 269 customers

Both solutions produce usable cluster sizes. The five-cluster solution provides more detailed customer segmentation, while the two-cluster solution has the stronger silhouette score.

The customer profiles will be compared next before selecting the final number of clusters.

## Final Cluster Selection

The silhouette score was highest for `k = 2`, with a score of 0.2702.

The two clusters also showed clear differences in income, spending, purchases, and campaign activity.

Therefore, `k = 2` was selected as the final clustering solution.

- Cluster 0: 1,326 customers
- Cluster 1: 912 customers

Cluster 0 represents lower-spending customers with lower average income and fewer purchases.

Cluster 1 represents higher-value customers with higher average income, substantially higher spending, and more purchases.

## Cluster Response Analysis

Cluster 0 contains 1,326 customers and has a response rate of 10.18%.

Cluster 1 contains 912 customers and has a response rate of 21.82%.

Cluster 1 has a substantially higher response rate, suggesting that higher-income and higher-spending customers may be more responsive to marketing campaigns.

The `Response` variable was used only to interpret the clusters and was not used to create them.

## KDD Interpretation and Evaluation

The final clustering produced two meaningful customer segments.

Cluster 0 contains lower-income and lower-spending customers. It has an average spending value of approximately 193.55 and a marketing response rate of 10.18%.

Cluster 1 contains higher-income and higher-spending customers. It has an average spending value of approximately 1,204.46 and a marketing response rate of 21.82%.

Cluster 1 appears to be the higher-value and more responsive customer segment. The company may prioritize this group for premium offers and targeted campaigns, while using lower-cost or personalized strategies for Cluster 0.


## Final Segment Interpretation

Cluster 0 contains 1,326 customers with average income of 38,307.35, average spending of 193.55, and an average of 7.80 purchases. Its response rate is 10.18%.

Cluster 1 contains 912 customers with average income of 72,449.07, average spending of 1,204.46, and an average of 19.44 purchases. Its response rate is 21.82%.

Cluster 1 represents the higher-value and more responsive customer segment.

## KDD Deployment Demonstration

The trained K-Means model can assign a new customer to an existing customer segment.

The new customer must go through the same transformations used during training:

1. Apply the log transformation.
2. Apply the saved standardization scaler.
3. Use the trained K-Means model to predict the customer’s cluster.
