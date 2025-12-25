code = """import json, pandas as pd
from pathlib import Path

# Load full Europe metadata from file
path = Path(var_call_fLYT2U2c9rcfmcZfieiXnmIl)
with open(path, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_HRXa5UBh9aV00EaGDnI9ulav

# Build DataFrames
meta_df = pd.DataFrame(europe_meta)
articles_df = pd.DataFrame(articles)

# Ensure types
meta_df['article_id'] = meta_df['article_id'].astype(int)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge to keep only Europe 2010-2020 articles with text
merged = meta_df.merge(articles_df, on='article_id', how='left')

# Business classification
def is_business(title, description):
    text = f"{title} {description}".lower()
    keywords = [
        'market', 'markets', 'stock', 'stocks', 'share', 'shares', 'bond', 'bonds',
        'investment', 'investor', 'investors', 'economy', 'economic', 'gdp',
        'unemployment', 'inflation', 'revenue', 'profit', 'losses', 'earnings',
        'merger', 'acquisition', 'ipo', 'bank', 'banks', 'interest rate',
        'currency', 'currencies', 'trade', 'trading', 'business', 'company',
        'companies', 'corporate', 'finance', 'financial', 'budget', 'tariff',
        'tariffs', 'export', 'exports', 'import', 'imports', 'deficit', 'surplus'
    ]
    return any(k in text for k in keywords)

merged['is_business'] = merged.apply(lambda r: is_business(r.get('title', ''), r.get('description', '')), axis=1)

# Extract year and compute counts per year
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

business_counts = merged[merged['is_business']].groupby('year').size()

# Reindex to ensure all years 2010-2020 present with 0s
years = list(range(2010, 2021))
business_counts = business_counts.reindex(years, fill_value=0)

avg_business_per_year = business_counts.mean()

result = json.dumps({"average_business_articles_per_year_europe_2010_2020": avg_business_per_year})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_fLYT2U2c9rcfmcZfieiXnmIl': 'file_storage/call_fLYT2U2c9rcfmcZfieiXnmIl.json', 'var_call_HRXa5UBh9aV00EaGDnI9ulav': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_f316Pl1mwMDMQsVIpER1QKdh': {'info': 'classification function ready'}}

exec(code, env_args)
