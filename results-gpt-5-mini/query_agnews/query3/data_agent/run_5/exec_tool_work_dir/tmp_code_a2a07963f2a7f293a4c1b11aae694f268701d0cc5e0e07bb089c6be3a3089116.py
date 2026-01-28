code = """import json
import pandas as pd

# Load articles result (small list) from storage variable
articles = var_call_brI66eyidGrATuvppnT8PvBx

# Load metadata result from JSON file path stored in var_call_5PY2CU3pNxtc83taniQVUlgL
metadata_path = var_call_5PY2CU3pNxtc83taniQVUlgL
with open(metadata_path, 'r', encoding='utf-8') as f:
    metadata = json.load(f)

# Create DataFrames
df_articles = pd.DataFrame(articles)
df_metadata = pd.DataFrame(metadata)

# Normalize article_id types
# Some article_id fields are strings; convert to int if possible
def to_int(x):
    try:
        return int(x)
    except:
        return None

if 'article_id' in df_articles.columns:
    df_articles['article_id'] = df_articles['article_id'].apply(to_int)
if 'article_id' in df_metadata.columns:
    df_metadata['article_id'] = df_metadata['article_id'].apply(to_int)

# Merge metadata (which is already filtered to Europe and date range) with articles on article_id
df_merged = pd.merge(df_metadata, df_articles, on='article_id', how='left')

# Define simple keyword-based classifier for Business category
business_keywords = [
    'market','markets','stock','stocks','economy','economic','oil','prices','price',
    'earnings','bank','financial','finance','investment','investor','investors','shares',
    'business','commercial','firm','private','company','companies','reuters','wall st','wall street',
    'carlyle','dow','nasdaq'
]

def is_business(row):
    text_parts = []
    if pd.notnull(row.get('title')):
        text_parts.append(str(row['title']))
    if pd.notnull(row.get('description')):
        text_parts.append(str(row['description']))
    if not text_parts:
        return False
    text = ' '.join(text_parts).lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Apply classifier
df_merged['is_business'] = df_merged.apply(is_business, axis=1)

# Extract year from publication_date and filter for 2010-2020 inclusive
def get_year(pubdate):
    try:
        return int(str(pubdate)[:4])
    except:
        return None

df_merged['year'] = df_merged['publication_date'].apply(get_year)

# Consider only years 2010-2020
df_period = df_merged[df_merged['year'].between(2010, 2020)]

# Count business articles per year. Use article_id unique count per year in case of duplicates
counts = df_period[df_period['is_business']].groupby('year')['article_id'].nunique().to_dict()

# Ensure all years 2010..2020 are present
counts_by_year = {year: int(counts.get(year, 0)) for year in range(2010, 2021)}

total_business = sum(counts_by_year.values())
num_years = 2020 - 2010 + 1
average_per_year = total_business / num_years if num_years>0 else 0

# Prepare result
result = {
    'average_business_articles_per_year': average_per_year,
    'total_business_articles_in_period': total_business,
    'counts_by_year': counts_by_year,
    'notes': 'Classification based on keyword matching of title and description; only articles with available title/description were classified.'
}

import json
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_brI66eyidGrATuvppnT8PvBx': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_5PY2CU3pNxtc83taniQVUlgL': 'file_storage/call_5PY2CU3pNxtc83taniQVUlgL.json'}

exec(code, env_args)
