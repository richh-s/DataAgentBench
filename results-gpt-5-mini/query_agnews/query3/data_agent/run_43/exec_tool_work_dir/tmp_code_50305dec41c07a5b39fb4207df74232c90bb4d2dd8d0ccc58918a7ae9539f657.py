code = """import json
import pandas as pd

# Load the large metadata result from the provided file path
metadata_path = var_call_wBMdICZcDqPVWUIjHShSXBKZ
with open(metadata_path, 'r') as f:
    metadata = json.load(f)

articles = var_call_muokBhUf3oqv7iEIPIQ4akSi

# Create DataFrames
df_meta = pd.DataFrame(metadata)
df_articles = pd.DataFrame(articles)

# Ensure article_id types are comparable (strings)
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Extract year
df_meta['year'] = pd.to_datetime(df_meta['publication_date']).dt.year

# Filter years 2010-2020 inclusive
df_meta = df_meta[(df_meta['year'] >= 2010) & (df_meta['year'] <= 2020)]

# Merge metadata with articles
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Define classification keywords
business_kw = [
    'market','markets','stock','stocks','wall st','wall street','economy','economic','business',
    'investment','investor','earnings','revenue','profit','bank','financial','finance','merger',
    'acquisition','oil prices','oil','crude','bond','bonds','share','shares','commercial aerospace',
    'private investment','deal'
]
sports_kw = ['score','match','season','football','soccer','nba','mlb','nfl','olympic','goal','tournament','coach','player','league']
tech_kw = ['technology','tech','software','computer','ai','robot','nasa','scientist','research','scientific','space','engineering','innovation']

# Function to classify
import re

def classify(row):
    text = ' '.join([str(row.get('title','') or ''), str(row.get('description','') or '')]).lower()
    # check sports
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    # check tech
    for kw in tech_kw:
        if kw in text:
            return 'Science/Technology'
    # check business
    for kw in business_kw:
        if kw in text:
            return 'Business'
    return 'World'

# Apply classification
df['category'] = df.apply(classify, axis=1)

# Count Business articles per year
business_counts = df[df['category']=='Business'].groupby('year').size().to_dict()

# Ensure all years 2010-2020 present
years = list(range(2010,2021))
counts_by_year = {str(y): int(business_counts.get(y, 0)) for y in years}

total_business = sum(counts_by_year.values())
num_years = len(years)
average_per_year = total_business / num_years if num_years>0 else None

result = {
    'counts_by_year': counts_by_year,
    'total_business_articles_2010_2020': int(total_business),
    'num_years': num_years,
    'average_business_articles_per_year': average_per_year
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lktjq80hW5RXIUMVW6pGcwQX': ['articles'], 'var_call_9NlDVun6rUGL37uHuDYYFL6b': ['authors', 'article_metadata'], 'var_call_wBMdICZcDqPVWUIjHShSXBKZ': 'file_storage/call_wBMdICZcDqPVWUIjHShSXBKZ.json', 'var_call_muokBhUf3oqv7iEIPIQ4akSi': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
