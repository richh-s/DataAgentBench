code = """import json
import pandas as pd

# Load the large results from the provided storage file paths
with open(var_call_os2kGeQzsrjOcYqgAzMxw5u5, 'r') as f:
    articles = json.load(f)
with open(var_call_vyipnDhE8iXJHti8RaLNLSbC, 'r') as f:
    metadata = json.load(f)

# Create DataFrames
articles_df = pd.DataFrame(articles)
metadata_df = pd.DataFrame(metadata)

# Normalize article_id types to integers where possible
articles_df['article_id'] = articles_df['article_id'].astype(str).str.extract(r"(\d+)")[0].astype(int)
metadata_df['article_id'] = metadata_df['article_id'].astype(str).str.extract(r"(\d+)")[0].astype(int)

# Ensure publication_date is datetime and extract year
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'], errors='coerce')
metadata_df['year'] = metadata_df['publication_date'].dt.year

# Filter to years 2010-2020 inclusive
metadata_df = metadata_df[metadata_df['year'].between(2010, 2020)]

# Join metadata (Europe articles) with article texts
merged = metadata_df.merge(articles_df, on='article_id', how='left')

# Fill missing title/description with empty strings
merged['title'] = merged['title'].fillna('')
merged['description'] = merged['description'].fillna('')

# Simple keyword-based classifier for Business category
business_keywords = [
    'business','market','markets','stock','stocks','wall st','wall street','economy','economic',
    'finance','financial','bank','banks','investment','investor','investors','ipo','earnings','profit','profits',
    'shares','merger','acquisition','interest rate','rates','mortgage','capital','company','companies','corporate',
    'revenue','lost','losses','billion','million','ftse','dow','nasdaq','s&p','spx'
]

def is_business(row):
    text = (row.get('title','') + ' ' + row.get('description','')).lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

merged['is_business'] = merged.apply(is_business, axis=1)

# Count business articles per year
year_counts = merged[merged['is_business']].groupby('year').size().to_dict()

# Ensure all years 2010-2020 present
counts_complete = {str(y): int(year_counts.get(y, 0)) for y in range(2010, 2021)}

total_business = sum(counts_complete.values())
num_years = 2020 - 2010 + 1
average_per_year = total_business / num_years if num_years > 0 else 0.0

result = {
    'year_counts': counts_complete,
    'total_business_articles_2010_2020': int(total_business),
    'num_years': num_years,
    'average_per_year': round(float(average_per_year), 2)
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_os2kGeQzsrjOcYqgAzMxw5u5': 'file_storage/call_os2kGeQzsrjOcYqgAzMxw5u5.json', 'var_call_vyipnDhE8iXJHti8RaLNLSbC': 'file_storage/call_vyipnDhE8iXJHti8RaLNLSbC.json'}

exec(code, env_args)
