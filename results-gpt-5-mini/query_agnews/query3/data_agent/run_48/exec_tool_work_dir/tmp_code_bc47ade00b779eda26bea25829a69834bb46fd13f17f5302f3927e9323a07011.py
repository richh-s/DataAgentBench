code = """import json
import pandas as pd
import re

# Load metadata records from file path variable
meta_path = var_call_jQ5dhQ0C3EMQSuPbocUQbQ1H
with open(meta_path, 'r') as f:
    meta_records = json.load(f)

# Load articles records from variable
articles_records = var_call_4AKv569EHdPW9DzPTN9M9LOu

# Build DataFrames
meta_df = pd.DataFrame(meta_records)
articles_df = pd.DataFrame(articles_records)

# Ensure correct types
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge on article_id
df = pd.merge(meta_df, articles_df[['article_id','title','description']], on='article_id', how='left')

# Define business keywords
business_keywords = [
    'business','economy','economic','market','markets','stock','stocks','wall st','wall street',
    'investment','investor','investors','company','companies','bank','banks','merger','acquisition',
    'earnings','profit','profits','revenue','ipo','currency','inflation','interest rate','interest-rate',
    'interest','bond','bonds','share','shares','capital','fund','funds','retail','corporate','merchants'
]

# Function to detect business
def is_business(row):
    txt = ''
    if pd.notna(row.get('title')):
        txt += str(row['title']) + ' '
    if pd.notna(row.get('description')):
        txt += str(row['description'])
    txt = txt.lower()
    for kw in business_keywords:
        if kw in txt:
            return 1
    return 0

# Apply detection
df['is_business'] = df.apply(is_business, axis=1)

# Extract year
df['year'] = pd.to_datetime(df['publication_date']).dt.year

# Filter years 2010-2020
df = df[(df['year'] >= 2010) & (df['year'] <= 2020)]

# Group counts by year
counts = df.groupby('year')['is_business'].sum().to_dict()

# Ensure all years present
result_counts = {str(y): int(counts.get(y, 0)) for y in range(2010, 2021)}

# Compute average over 11 years
total_business = sum(result_counts.values())
average = total_business / 11.0

result = {
    'average_per_year': average,
    'total_business_articles': int(total_business),
    'counts_by_year': result_counts
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jQ5dhQ0C3EMQSuPbocUQbQ1H': 'file_storage/call_jQ5dhQ0C3EMQSuPbocUQbQ1H.json', 'var_call_ihLCcHqBvYDfttpyZkZ7dQSm': 'file_storage/call_ihLCcHqBvYDfttpyZkZ7dQSm.json', 'var_call_4AKv569EHdPW9DzPTN9M9LOu': [{'_id': '6959a1be9f5795fb810a95ea', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a1be9f5795fb810a95eb', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a1be9f5795fb810a95ec', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a1be9f5795fb810a95ed', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a1be9f5795fb810a95ee', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
