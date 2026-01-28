code = """import json
import pandas as pd

# Load metadata results
metadata_file = locals()['var_functions.query_db:5']
with open(metadata_file, 'r') as f:
    metadata_records = json.load(f)

print("Total European articles 2010-2020:", len(metadata_records))

# Load article data
articles_file = locals()['var_functions.query_db:11']
with open(articles_file, 'r') as f:
    article_records = json.load(f)

print("Total articles retrieved:", len(article_records))

# Process metadata
metadata_df = pd.DataFrame(metadata_records)
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_df['year'] = metadata_df['publication_date'].dt.year

# Process articles
articles_df = pd.DataFrame(article_records)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge datasets
merged_df = pd.merge(metadata_df, articles_df, on='article_id', how='inner')
print("Successfully merged:", len(merged_df), "articles")

# Classify business articles
business_keywords = [
    'business', 'economy', 'economic', 'finance', 'financial', 'market', 'markets',
    'stock', 'stocks', 'trade', 'trading', 'investment', 'investments', 'investing', 'investor',
    'investors', 'company', 'companies', 'corporate', 'corporation', 'bank', 'banks', 'banking',
    'dollar', 'euro', 'currency', 'oil', 'energy', 'profit', 'profits', 'revenue', 'sales', 'IPO',
    'Wall St', 'Wall Street', 'share', 'shares', 'quarter', 'earnings', 'fund', 'funds', 'capital',
    'CEO', 'executive', 'executives'
]

def is_business(title, desc):
    if pd.isna(title) and pd.isna(desc):
        return False
    text = str(title) + " " + str(desc)
    text = text.lower()
    for keyword in business_keywords:
        if keyword.lower() in text:
            return True
    return False

# Apply classification
merged_df['is_business'] = merged_df.apply(
    lambda row: is_business(row.get('title'), row.get('description')), axis=1
)

business_df = merged_df[merged_df['is_business']]
print("Business articles identified:", len(business_df))

# Count by year
business_by_year = business_df['year'].value_counts().sort_index()
print("Business articles by year:")
print(business_by_year.to_string())

# Calculate average for 2010-2020 inclusive
years_range = list(range(2010, 2021))
total_years = len(years_range)

# Create complete year count dictionary
year_counts = {}
for year in years_range:
    year_counts[year] = 0

# Update with actual counts
for year, count in business_by_year.items():
    if year in year_counts:
        year_counts[year] = int(count)

# Calculate average
total_business = sum(year_counts.values())
average_per_year = total_business / total_years

print("Average business articles per year (2010-2020):", round(average_per_year, 2))

result = {
    "total_business_articles": len(business_df),
    "yearly_counts": year_counts,
    "average_per_year": round(average_per_year, 2),
    "total_years": total_years
}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
