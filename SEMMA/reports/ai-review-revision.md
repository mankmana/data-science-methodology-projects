# AI Review and Revision Record

AI assistance was used to review the SEMMA project during the Sample, Explore, Modify, Model, and Assess phases. The code was executed in Colab, and the outputs were reviewed before finalizing the analysis.

## Revisions Completed

- Corrected the dataset loading process after identifying that the CSV file was initially read as one column.
- Verified that `deposit` was the correct target variable.
- Reviewed the target distribution and categorical feature exploration.
- Checked missing values, duplicate records, numerical features, and categorical features.
- Converted the target variable into binary values.
- Applied one-hot encoding to categorical features and scaling to numerical features.
- Verified that the prepared data contained 51 features.
- Compared Logistic Regression, Decision Tree, and Random Forest models.
- Reviewed classification reports and confusion matrices.
- Selected Random Forest because it produced the strongest overall results.
- Corrected the deployment script so the saved model, preprocessor, and feature definitions were loaded correctly.
- Tested the deployment script with a sample customer.

The results were manually verified using the Colab outputs and the local deployment prediction.

