code = """import json
import pandas as pd

# Access the stored results
articles_result = var_functions.query_db:0
metadata_result = var_functions.query_db:2

# Load articles data
if isinstance(articles_result, str) and articles_result.endswith('.json'):
    with open(articles_result, 'r') as f:
        articles_data = json.load(f)
else:
    articles_data = var_functions.query_db:0

# Load metadata data
if isinstance(metadata_result, str) and metadata_result.endswith('.json'):
    with open(metadata_result, 'r') as f:
        metadata_data = json.load(f)
else:
    metadata_data = var_functions.query_db:2

# Create DataFrames
df_articles = pd.DataFrame(articles_data)
df_metadata = pd.DataFrame(metadata_data)

# Convert article_id to string for matching
df_articles['article_id'] = df_articles['article_id'].astype(str)
df_metadata['article_id'] = df_metadata['article_id'].astype(str)

# Merge dataframes
df_merged = pd.merge(df_articles, df_metadata, on='article_id', how='inner')

# Define business keywords
business_keywords = [
    'business', 'economy', 'stock', 'stocks', 'wall st', 'wall street', 
    'company', 'companies', 'corporate', 'investment', 'investing',
    'market', 'markets', 'trade', 'trading', 'finance', 'financial',
    'profit', 'profits', 'loss', 'revenue', 'sales', 'quarter',
    'oil', 'energy', 'bank', 'banks', 'banking', 'retail',
    'job', 'jobs', 'employment', 'unemployment', 'dollar', 'euro'
]

# Function to classify as business article
def is_business_article(title, description):
    text = f"{title} {description}".lower()
    return any(keyword in text for keyword in business_keywords)

# Apply classification
df_merged['is_business'] = df_merged.apply(
    lambda row: is_business_article(row['title'], row['description']), 
    axis=1
)

# Filter business articles in Europe (2010-2020)
df_business = df_merged[df_merged['is_business'] == True].copy()

# Extract year from publication date
df_business['year'] = pd.to_datetime(df_business['publication_date']).dt.year

# Filter years 2010-2020
df_business = df_business[
    (df_business['year'] >= 2010) & (df_business['year'] <= 2020)
]

# Group by year and count articles
yearly_counts = df_business.groupby('year').size().reset_index(name='count')

# Calculate average
average_per_year = yearly_counts['count'].mean() if not yearly_counts.empty else 0

# Prepare result
result = {
    'average_business_articles_per_year': round(average_per_year, 2),
    'yearly_breakdown': yearly_counts.to_dict('records'),
    'total_years': len(yearly_counts),
    'total_business_articles': yearly_counts['count'].sum() if not yearly_counts.empty else 0
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
