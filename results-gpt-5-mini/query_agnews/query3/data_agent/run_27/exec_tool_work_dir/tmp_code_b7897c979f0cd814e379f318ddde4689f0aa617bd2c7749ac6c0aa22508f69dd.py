code = """import json
import pandas as pd
import re

# Helper to load storage entries which may be either lists or file paths
def load_storage(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

meta_records = load_storage(var_call_8FxzZo84pzLRYHC44my2FfbI)
article_records = load_storage(var_call_exodGndxEv2MMel3ypjx7mWp)

# Create DataFrames
df_meta = pd.DataFrame(meta_records)
# Ensure correct types
if 'article_id' in df_meta.columns:
    df_meta['article_id'] = df_meta['article_id'].astype(int)
    df_meta['publication_date'] = pd.to_datetime(df_meta['publication_date'])
    df_meta['year'] = df_meta['publication_date'].dt.year

df_articles = pd.DataFrame(article_records)
if 'article_id' in df_articles.columns:
    df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge metadata for Europe (already filtered) with article text
df = pd.merge(df_meta, df_articles[['article_id','title','description']], on='article_id', how='left')

# Define business-related keywords
business_keywords = [
    'company','companies','shares','stock','stocks','market','markets','economy','economic','trade','bank','finance',
    'financial','business','firm','investment','investor','ipo','earnings','profit','profits','revenue','merger','acquisition',
    'debt','dollar','euro','ftse','nasdaq','nyse','index','consumer','retail','sales','unemployment','jobs','revenue','oil prices',
    'oil prices','oil','gas prices','billion','million'
]
# Lowercase keywords
business_keywords = [kw.lower() for kw in business_keywords]

# Function to classify
def is_business(row):
    text = ''
    for col in ['title','description']:
        val = row.get(col)
        if isinstance(val, str):
            text += ' ' + val.lower()
    # simple keyword presence
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Apply classification
df['is_business'] = df.apply(is_business, axis=1)

# Filter years 2010-2020 inclusive
df = df[(df['year'] >= 2010) & (df['year'] <= 2020)]

# Count business articles per year
year_range = list(range(2010, 2021))
counts_by_year = {str(year): int(df[df['year']==year]['is_business'].sum()) for year in year_range}

total_business = sum(counts_by_year.values())
num_years = len(year_range)
average_per_year = total_business / num_years if num_years>0 else 0.0

result = {
    'average_business_articles_per_year': round(average_per_year, 2),
    'total_business_articles': int(total_business),
    'years_considered': num_years,
    'counts_by_year': counts_by_year
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8FxzZo84pzLRYHC44my2FfbI': 'file_storage/call_8FxzZo84pzLRYHC44my2FfbI.json', 'var_call_7jpGjpr3tRKiBBbMSvnPVUkd': 'file_storage/call_7jpGjpr3tRKiBBbMSvnPVUkd.json', 'var_call_exodGndxEv2MMel3ypjx7mWp': 'file_storage/call_exodGndxEv2MMel3ypjx7mWp.json'}

exec(code, env_args)
