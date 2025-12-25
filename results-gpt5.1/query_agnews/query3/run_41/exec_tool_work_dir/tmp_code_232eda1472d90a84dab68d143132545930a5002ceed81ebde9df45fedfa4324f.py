code = """import json, pandas as pd
import os

# Load Europe metadata from file path
path = var_call_4G6vg1FA9zUlvrC4UfV7YNBi
with open(path, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_tvxi84y3kFd9T2b5u7cYuOVo

meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

merged = meta_df.merge(articles_df, on='article_id', how='inner')

text = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.lower()

business_keywords = ['business', 'market', 'markets', 'stock', 'stocks', 'company', 'companies', 'corporate', 'shares', 'investor', 'investors', 'investment', 'economy', 'economic', 'finance', 'financial', 'bank', 'banks', 'banking', 'trade', 'trading', 'merger', 'acquisition', 'earnings', 'profit', 'profits', 'revenue', 'sales', 'industry', 'industries']

pattern = '|'.join(business_keywords)

business_mask = text.str.contains(pattern, case=False, regex=True)

merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

business_by_year = merged[business_mask].groupby('year').size()

years = list(range(2010, 2021))
counts = [int(business_by_year.get(y, 0)) for y in years]

avg_business_per_year = sum(counts) / len(years) if years else 0

result = {
    'years': years,
    'business_counts_per_year': counts,
    'average_business_articles_per_year_europe_2010_2020': avg_business_per_year
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_4G6vg1FA9zUlvrC4UfV7YNBi': 'file_storage/call_4G6vg1FA9zUlvrC4UfV7YNBi.json', 'var_call_tvxi84y3kFd9T2b5u7cYuOVo': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
