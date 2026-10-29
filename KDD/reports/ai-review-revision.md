# AI Review and Revision Record

AI assistance was used to review the KDD project through the Selection, Preprocessing, Transformation, Data Mining, and Interpretation phases. The notebook was executed step by step, and the results were checked before being added to the project reports.

## Revisions Completed

- Corrected the dataset loading process because the file was tab-separated.
- Reviewed missing values, duplicate records, unrealistic birth years, and constant columns.
- Removed two unrealistic birth-year records and imputed missing income values.
- Created summary features including age, total spending, total purchases, and campaign acceptance.
- Reviewed feature selection for customer clustering.
- Identified right-skewed features and applied a `log1p` transformation.
- Standardized the selected clustering features using `StandardScaler`.
- Compared K-Means solutions using the elbow method and silhouette scores.
- Compared two-cluster and five-cluster solutions.
- Selected two clusters because they had the highest silhouette score and clearer interpretation.
- Reviewed cluster sizes, customer profiles, spending behavior, and response rates.
- Confirmed that `Response` was used only for interpretation and not for creating the clusters.
- Corrected the deployment script by defining the log features and scaler.
- Tested the deployment script and assigned a sample customer to Cluster 1.

All findings were verified using the Colab outputs and the local deployment result.
