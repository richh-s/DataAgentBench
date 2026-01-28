code = """import json
import pandas as pd
from datetime import datetime
import re

# Load metadata results
metadata_file = var_functions.query_db:5
with open(metadata_file, 'r') as f:
    metadata_records = json.load(f)

print(f"Total European articles 2010-2020: {len(metadata_records)}")

# Load article data
articles_file = var_functions.query_db:11
with open(articles_file, 'r') as f:
    article_records = json.load(f)

print(f"Total articles retrieved: {len(article_records)}")

# Create DataFrames
metadata_df = pd.DataFrame(metadata_records)
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_df['year'] = metadata_df['publication_date'].dt.year

articles_df = pd.DataFrame(article_records)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Check if all article IDs from metadata are in articles
metadata_ids = set(metadata_df['article_id'].astype(int).tolist())
articles_ids = set(articles_df['article_id'].tolist())

missing_ids = metadata_ids - articles_ids
print(f"Articles in metadata but not in articles collection: {len(missing_ids)}")

# Merge the datasets
merged_df = pd.merge(metadata_df, articles_df, on='article_id', how='inner')
print(f"Merged dataset size: {len(merged_df)}")

# Classify business articles based on title and description
business_keywords = [
    'business', 'economy', 'economic', 'economics', 'finance', 'financial', 'market', 'markets', 'stock', 'stocks',
    'trade', 'trading', 'investment', 'investments', 'investing', 'investor', 'investors', 'company', 'companies',
    'corporate', 'corporation', 'corporations', 'bank', 'banks', 'banking', 'dollar', 'euro', 'currency', 'currencies',
    'oil', 'energy', 'profit', 'profits', 'revenue', 'sales', 'IPO', 'Wall St', 'Wall Street', 'share', 'shares',
    'quarter', 'earnings', 'fund', 'funds', 'capital', 'CEO', 'executive', 'executives'
]

def is_business_article(title, description):
    if pd.isna(title) and pd.isna(description):
        return False
    
    text = ' '.join([str(title), str(description)]).lower()
    
    # Check for business keywords
    for keyword in business_keywords:
        if keyword.lower() in text:
            return True
    
    return False

# Apply classification
merged_df['is_business'] = merged_df.apply(
    lambda row: is_business_article(row['title'], row['description']), axis=1
)

business_df = merged_df[merged_df['is_business'] == True]
print(f"Business articles found: {len(business_df)}")

# Count business articles per year
business_per_year = business_df['year'].value_counts().sort_index()
print(f"\nBusiness articles by year:")
print(business_per_year)

# Calculate average
average_business_per_year = business_df['year'].value_counts().mean()
print(f"\nAverage business articles per year: {average_business_per_year:.2f}")

# Prepare result
result = {
    "total_business_articles": len(business_df),
    "business_per_year": business_per_year.to_dict(),
    "average_per_year": round(average_business_per_year, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
