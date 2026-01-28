code = """import json
import pandas as pd
from datetime import datetime

# Load metadata results from file path
metadata_path = locals()['var_functions.query_db:5']
print(f"Loading metadata from: {metadata_path}")

with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

print(f"Total European articles 2010-2020: {len(metadata_records)}")

# Load article data from file path
articles_path = locals()['var_functions.query_db:11']
print(f"Loading articles from: {articles_path}")

with open(articles_path, 'r') as f:
    article_records = json.load(f)

print(f"Total articles retrieved: {len(article_records)}")

# Process metadata - convert publication_date to datetime and extract year
metadata_df = pd.DataFrame(metadata_records)
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_df['year'] = metadata_df['publication_date'].dt.year

# Process articles - convert article_id to int for matching
articles_df = pd.DataFrame(article_records)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Check coverage
metadata_ids = set(metadata_df['article_id'].astype(int).tolist())
articles_ids = set(articles_df['article_id'].tolist())
missing_count = len(metadata_ids - articles_ids)
print(f"Articles in metadata but not retrieved: {missing_count}")

# Merge datasets on article_id
merged_df = pd.merge(metadata_df, articles_df, on='article_id', how='inner')
print(f"Successfully merged: {len(merged_df)} articles")

# Define function to classify business articles
business_keywords = [
    'business', 'economy', 'economic', 'economics', 'finance', 'financial', 'market', 'markets',
    'stock', 'stocks', 'trade', 'trading', 'investment', 'investments', 'investing', 'investor',
    'investors', 'company', 'companies', 'corporate', 'corporation', 'corporations', 'bank',
    'banks', 'banking', 'dollar', 'euro', 'currency', 'currencies', 'oil', 'energy', 'profit',
    'profits', 'revenue', 'sales', 'IPO', 'Wall St', 'Wall Street', 'share', 'shares',
    'quarter', 'earnings', 'fund', 'funds', 'capital', 'CEO', 'executive', 'executives'
]

def is_business(title, desc):
    if pd.isna(title) and pd.isna(desc):
        return False
    text = f"{title} {desc}".lower()
    return any(keyword.lower() in text for keyword in business_keywords)

# Classify articles
merged_df['is_business'] = merged_df.apply(
    lambda row: is_business(row.get('title'), row.get('description')), axis=1
)

business_df = merged_df[merged_df['is_business']]
print(f"Business articles identified: {len(business_df)}")

# Count by year
business_by_year = business_df['year'].value_counts().sort_index()
print(f"Business articles by year:\n{business_by_year}")

# Calculate average for 2010-2020 inclusive
years_2010_2020 = list(range(2010, 2021))
total_years = len(years_2010_2020)

# Ensure we count all years (even those with 0 articles)
year_counts = {year: 0 for year in years_2010_2020}
year_counts.update(business_by_year.to_dict())

# Calculate average
business_count_values = [year_counts[year] for year in years_2010_2020]
average_per_year = sum(business_count_values) / total_years

print(f"Average business articles per year (2010-2020): {average_per_year:.2f}")

result = {
    "total_business_articles": len(business_df),
    "yearly_counts": year_counts,
    "average_per_year": round(average_per_year, 2),
    "total_years": total_years
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
