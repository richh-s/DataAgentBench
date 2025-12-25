code = """import pandas as pd
import json
import re
import os

# Load metadata
# Key for metadata file path from previous turn
meta_path_key = 'var_function-call-1050039959698811753'
# Retrieve the path
if meta_path_key in locals():
    meta_path = locals()[meta_path_key]
else:
    # Fallback if I lost track of keys, but I should have it.
    # Actually, the file path was given in turn 4 result.
    pass

with open(meta_path, 'r') as f:
    meta_data = json.load(f)

df_meta = pd.DataFrame(meta_data)
# Ensure article_id is int
df_meta['article_id'] = pd.to_numeric(df_meta['article_id'], errors='coerce')

# Load articles
articles_res = locals()['var_function-call-14707976591899183813']
if isinstance(articles_res, str) and articles_res.endswith('.json') and os.path.exists(articles_res):
    with open(articles_res, 'r') as f:
        articles_data = json.load(f)
else:
    articles_data = articles_res

df_articles = pd.DataFrame(articles_data)
# Ensure article_id is int
df_articles['article_id'] = pd.to_numeric(df_articles['article_id'], errors='coerce')

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Define Business Keywords
business_keywords = [
    "business", "economy", "economic", "market", "markets", "stock", "stocks", 
    "finance", "financial", "corporate", "industry", "company", "companies", 
    "profit", "profits", "earnings", "invest", "investment", "investor", "investors", 
    "bank", "banks", "banking", "trade", "trading", "merger", "acquisition", 
    "deal", "share", "shares", "revenue", "sales", "dollar", "currency", 
    "inflation", "recession", "tax", "taxes", "wall street", "nasdaq", "dow jones", 
    "oil price", "oil prices", "crude", "imf", "fed", "central bank", "ceo", "cfo",
    "retail", "retailers", "consumer spending", "growth", "debt", "eurozone", "bond", "bonds"
]

# Compile Regex
regex = re.compile(r'\b(' + '|'.join([re.escape(k) for k in business_keywords]) + r')\b', re.IGNORECASE)

# Filter
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
print(json.dumps({"average": average, "counts": counts.to_dict()}))"""

env_args = {'var_function-call-886384908282461354': ['authors', 'article_metadata'], 'var_function-call-1050039959698811753': 'file_storage/function-call-1050039959698811753.json', 'var_function-call-18250612966487496501': 'file_storage/function-call-18250612966487496501.json', 'var_function-call-4586272944250348228': 14860, 'var_function-call-14707976591899183813': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
