code = """import pandas as pd
import json
import re
import os

# Load metadata
meta_path = locals()['var_function-call-1050039959698811753']
with open(meta_path, 'r') as f:
    meta_data = json.load(f)

df_meta = pd.DataFrame(meta_data)
df_meta['article_id'] = pd.to_numeric(df_meta['article_id'], errors='coerce')

# Load articles
articles_path = locals()['var_function-call-13889016544522667956']
with open(articles_path, 'r') as f:
    articles_data = json.load(f)

df_articles = pd.DataFrame(articles_data)
df_articles['article_id'] = pd.to_numeric(df_articles['article_id'], errors='coerce')

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Business Keywords
business_keywords = [
    "business", "economy", "economic", "market", "markets", "stock", "stocks", 
    "finance", "financial", "corporate", "industry", "company", "companies", 
    "profit", "profits", "earnings", "invest", "investment", "investor", "investors", 
    "bank", "banks", "banking", "trade", "trading", "merger", "acquisition", 
    "deal", "share", "shares", "revenue", "sales", "dollar", "currency", 
    "inflation", "recession", "tax", "taxes", "wall street", "nasdaq", "dow jones", 
    "oil price", "oil prices", "crude", "imf", "fed", "central bank", "ceo", "cfo",
    "retail", "retailers", "consumer spending", "growth", "debt", "eurozone", 
    "bond", "bonds", "ipo", "initial public offering", "deficit", "surplus", 
    "gdp", "interest rate", "interest rates", "yield", "treasury", "loan", "loans"
]

regex = re.compile(r'\b(' + '|'.join([re.escape(k) for k in business_keywords]) + r')\b', re.IGNORECASE)

def classify(text):
    if regex.search(text):
        return True
    return False

df['text'] = df['title'].fillna('') + " " + df['description'].fillna('')
df['is_business'] = df['text'].apply(classify)

df_business = df[df['is_business']]

# Group by Year
df_business['year'] = pd.to_datetime(df_business['publication_date']).dt.year
counts = df_business.groupby('year').size()

# Reindex 2010-2020
all_years = range(2010, 2021)
counts = counts.reindex(all_years, fill_value=0)

average = counts.mean()

print("__RESULT__:")
print(json.dumps({"average": average, "counts": counts.to_dict(), "merged_count": len(df), "business_count": len(df_business)}))"""

env_args = {'var_function-call-886384908282461354': ['authors', 'article_metadata'], 'var_function-call-1050039959698811753': 'file_storage/function-call-1050039959698811753.json', 'var_function-call-18250612966487496501': 'file_storage/function-call-18250612966487496501.json', 'var_function-call-4586272944250348228': 14860, 'var_function-call-14707976591899183813': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9804075469372697773': {'average': 0.0, 'counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}}, 'var_function-call-8122181870560022517': {'meta_size': 14860, 'articles_size': 5, 'merged_size': 1, 'sample': [{'article_id': 3, 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}]}, 'var_function-call-13889016544522667956': 'file_storage/function-call-13889016544522667956.json'}

exec(code, env_args)
