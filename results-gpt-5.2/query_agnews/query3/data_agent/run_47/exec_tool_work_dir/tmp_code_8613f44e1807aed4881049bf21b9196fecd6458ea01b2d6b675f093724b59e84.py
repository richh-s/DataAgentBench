code = """import json, pandas as pd

# Load Europe metadata (may be in file)
meta_src = var_call_ByeUMZISiGZhqaTfXtkgYIyO
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_UFvsg83tbF2yNh00uDSAws0v

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# Normalize types
for c in ['article_id']:
    df_meta[c] = df_meta[c].astype(str)
    df_arts[c] = df_arts[c].astype(str)

# Join to get title/description for Europe 2010-2020
df = df_meta.merge(df_arts, on='article_id', how='left')

# Simple keyword-based business classifier
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_kw = [
    'stock', 'stocks', 'wall st', 'wall street', 'nasdaq', 'dow', 's&p', 'sp500', 's&p 500',
    'shares', 'equity', 'equities', 'bond', 'bonds', 'treasury', 'yield',
    'profit', 'profits', 'earnings', 'revenue', 'sales', 'forecast',
    'economy', 'economic', 'gdp', 'inflation', 'recession', 'unemployment',
    'bank', 'banks', 'banking', 'central bank', 'ecb', 'boe', 'fed',
    'interest rate', 'rates', 'loan', 'loans', 'credit', 'debt',
    'company', 'companies', 'corporate', 'ceo', 'merger', 'acquisition', 'ipo',
    'market', 'markets', 'invest', 'investment', 'investor', 'fund', 'hedge',
    'oil', 'crude', 'gas', 'energy prices', 'commodity', 'commodities',
    'currency', 'euro', 'dollar', 'forex', 'exchange rate',
    'trade', 'tariff'
]

pattern = r'(' + '|'.join([pd.regex.escape(k) for k in business_kw]) + r')'
# pandas doesn't have regex.escape; use re
import re
pattern = r'(' + '|'.join([re.escape(k) for k in business_kw]) + r')'

is_business = text.str.contains(pattern, regex=True, na=False)

df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

# Count business articles per year for years 2010-2020 inclusive
years = list(range(2010, 2021))
counts = df[is_business].groupby('year').size().reindex(years, fill_value=0)
avg = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg),
    'total_business_articles_2010_2020': int(counts.sum()),
    'yearly_counts': {str(int(k)): int(v) for k, v in counts.items()}
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ByeUMZISiGZhqaTfXtkgYIyO': 'file_storage/call_ByeUMZISiGZhqaTfXtkgYIyO.json', 'var_call_UFvsg83tbF2yNh00uDSAws0v': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
