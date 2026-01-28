code = """import json
import pandas as pd

# Load metadata results
metadata_result_file = locals()['var_functions.query_db:5']
with open(metadata_result_file, 'r') as f:
    metadata_records = json.load(f)

print("Total European articles 2010-2020:", len(metadata_records))

# Load article data
articles_result_file = locals()['var_functions.query_db:11']
with open(articles_result_file, 'r') as f:
    article_records = json.load(f)

print("Total articles retrieved:", len(article_records))

# Process data
metadata_df = pd.DataFrame(metadata_records)
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_df['year'] = metadata_df['publication_date'].dt.year

articles_df = pd.DataFrame(article_records)

# Ensure article_id is string in both dataframes for merging
metadata_df['article_id'] = metadata_df['article_id'].astype(str)
articles_df['article_id'] = articles_df['article_id'].astype(str)

# Merge on article_id
merged_df = pd.merge(metadata_df, articles_df, on='article_id', how='inner')
print("Successfully merged:", len(merged_df), "articles")

# Business keywords pattern
business_keywords = [
    'business', 'economy', 'economic', 'finance', 'financial', 'market', 'markets',
    'stock', 'stocks', 'trade', 'trading', 'investment', 'investments', 'investing',
    'investor', 'investors', 'company', 'companies', 'corporate', 'corporation',
    'bank', 'banks', 'banking', 'dollar', 'euro', 'currency', 'oil', 'energy',
    'profit', 'profits', 'revenue', 'sales', 'IPO', 'Wall St', 'Wall Street',
    'share', 'shares', 'quarter', 'earnings', 'fund', 'funds', 'capital',
    'CEO', 'executive', 'executives', 'industry', 'industries', 'export', 'exports'
]

# Classify articles as business
def check_business(title, desc):
    if pd.isna(title):
        title = ''
    if pd.isna(desc):
        desc = ''
    text = (str(title) + ' ' + str(desc)).lower()
    for word in business_keywords:
        if word.lower() in text:
            return True
    return False

merged_df['is_business'] = merged_df.apply(
    lambda x: check_business(x.get('title'), x.get('description')), axis=1
)

business_df = merged_df[merged_df['is_business']]
print("Business articles identified:", len(business_df))

# Calculate yearly counts for 2010-2020
business_counts = business_df['year'].value_counts().sort_index()
years_2010_2020 = list(range(2010, 2021))
year_counts = {}

for year in years_2010_2020:
    year_counts[year] = int(business_counts.get(year, 0))

# Calculate average
average_per_year = sum(year_counts.values()) / len(years_2010_2020)

print("Average business articles per year:", round(average_per_year, 2))
print("Total business articles:", sum(year_counts.values()))

result = {
    "total_business_articles": sum(year_counts.values()),
    "yearly_counts": year_counts,
    "average_per_year": round(average_per_year, 2),
    "years_analyzed": len(years_2010_2020)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
