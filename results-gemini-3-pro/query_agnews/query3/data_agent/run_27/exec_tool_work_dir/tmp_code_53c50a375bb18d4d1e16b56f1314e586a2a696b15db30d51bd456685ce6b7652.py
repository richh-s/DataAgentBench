code = """import json
import pandas as pd
import re

# Load metadata
meta_path = locals()['var_function-call-1304167582762502927']
with open(meta_path, 'r') as f:
    meta_data = json.load(f)

# Load articles
articles_path = locals()['var_function-call-4198962169091228890']
with open(articles_path, 'r') as f:
    articles_data = json.load(f)

# Convert to DataFrames
df_meta = pd.DataFrame(meta_data)
df_articles = pd.DataFrame(articles_data)

# Ensure article_id is int for join
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Extract year
df['year'] = pd.to_datetime(df['publication_date']).dt.year

# Define keywords
business_keywords = [
    "business", "economy", "economic", "market", "stock", "trade", "finance", "financial", 
    "bank", "investment", "investor", "money", "currency", "dollar", "euro", "profit", 
    "revenue", "sales", "tax", "debt", "inflation", "rates", "interest rate", "fed", 
    "central bank", "wall street", "nasdaq", "dow jones", "company", "corporation", 
    "firm", "industry", "sector", "ceo", "cfo", "manager", "share", "asset", "fund", 
    "capital", "deal", "merger", "acquisition", "buyout", "ipo", "bid", "growth", 
    "recession", "spending", "jobs", "unemployment", "oil", "price", "cost", "consumer",
    "retail", "commercial", "short-seller", "dividend"
]

# Function to check category
def is_business(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    for kw in business_keywords:
        # distinct word match to avoid substrings like 'fed' in 'federal' (okay for fed but careful)
        # Simple check first
        if kw in text:
            return True
    return False

# Apply filter
df['is_business'] = df.apply(is_business, axis=1)
business_df = df[df['is_business']]

# Count per year
counts = business_df.groupby('year').size()

# Ensure all years 2010-2020 are covered
all_years = list(range(2010, 2021))
counts = counts.reindex(all_years, fill_value=0)

# Calculate average
average = counts.mean()

print(f"Counts per year: {counts.to_dict()}")
print(f"Average: {average}")

print("__RESULT__:")
print(json.dumps(average))"""

env_args = {'var_function-call-1304167582762502927': 'file_storage/function-call-1304167582762502927.json', 'var_function-call-641571560304296616': 'file_storage/function-call-641571560304296616.json', 'var_function-call-5674583780523164016': [{'_id': '6944d845bdad7807dc849895', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d845bdad7807dc849896', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d845bdad7807dc849897', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d845bdad7807dc849898', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d845bdad7807dc849899', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4198962169091228890': 'file_storage/function-call-4198962169091228890.json'}

exec(code, env_args)
