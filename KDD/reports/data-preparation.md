# KDD Data Preparation

## Data Loading

The `marketing_campaign.csv` file is tab-separated even though its filename uses the `.csv` extension. It will be loaded using:

```python
df = pd.read_csv("marketing_campaign.csv", sep="\t")```
