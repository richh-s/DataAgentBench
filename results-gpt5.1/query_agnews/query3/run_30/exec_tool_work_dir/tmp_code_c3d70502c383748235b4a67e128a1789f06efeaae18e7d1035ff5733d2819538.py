code = """import json, pandas as pd

# Load Europe metadata from file
import pathlib
path = pathlib.Path(var_call_KpqorlJrMAFaoMnZ5CNO67kU)
with open(path, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_Elebom1ydfhUKwwXj4yt5tuU

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

merged = meta_df.merge(articles_df, on='article_id', how='inner')

business_keywords = ['market', 'markets', 'stock', 'stocks', 'shares', 'trade', 'trading', 'economy', 'economic', 'business', 'company', 'companies', 'corporate', 'finance', 'financial', 'bank', 'banks', 'banking', 'invest', 'investment', 'investor', 'investors', 'merger', 'acquisition', 'deal', 'deals', 'profit', 'profits', 'earnings', 'revenue', 'sales', 'ipo', 'bond', 'bonds', 'currency', 'currencies', 'dollar', 'dollars', 'euro', 'yen', 'pound', 'tariff', 'tariffs', 'trade war', 'unemployment', 'inflation', 'gdp']

import re

def is_business(row):
    text = f"{row['title']} {row['description']}".lower()
    for kw in business_keywords:
        if re.search(r'\\b' + re.escape(kw) + r'\\b', text):
            return True
    return False

merged['is_business'] = merged.apply(is_business, axis=1)

merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

business_counts = merged[merged['is_business']].groupby('year').size().reindex(range(2010, 2021), fill_value=0)

avg_per_year = business_counts.mean()

result = json.dumps({"average_business_articles_per_year_europe_2010_2020": avg_per_year})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_KpqorlJrMAFaoMnZ5CNO67kU': 'file_storage/call_KpqorlJrMAFaoMnZ5CNO67kU.json', 'var_call_Elebom1ydfhUKwwXj4yt5tuU': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
