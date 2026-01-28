code = """import json, pandas as pd, re

path_meta = var_call_hpBoCyEkmdQ8dpxE2BTDMZ5h
with open(path_meta, 'r', encoding='utf-8') as f:
    meta = json.load(f)
arts = var_call_CHTsAxGKcK6pTvCGXFgflMSG

dfm = pd.DataFrame(meta)
dfa = pd.DataFrame(arts)

for col in ['article_id']:
    dfm[col] = dfm[col].astype(str)
    dfa[col] = dfa[col].astype(str)

df = dfm.merge(dfa, on='article_id', how='inner')
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_kw = [
    'wall st', 'stocks', 'stock', 'shares', 'bond', 'bonds', 'treasury', 'fed', 'central bank',
    'bank', 'banks', 'earnings', 'profit', 'revenue', 'sales', 'ipo', 'merger', 'acquisition',
    'oil', 'crude', 'gas', 'energy', 'opec', 'inflation', 'gdp', 'economy', 'economic',
    'market', 'markets', 'currency', 'forex', 'dollar', 'euro', 'yen', 'interest rate',
    'futures', 'commodity', 'commodities', 'trade', 'tariff', 'manufacturing', 'unemployment', 'jobs',
    'company', 'companies', 'business', 'corporate', 'retail', 'finance', 'financial'
]
pat = re.compile('|'.join(re.escape(k) for k in business_kw))
is_business = text.str.contains(pat)

df = df[is_business].copy()
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

df = df[(df['year'] >= 2010) & (df['year'] <= 2020)]

counts = df.groupby('year')['article_id'].nunique().reindex(range(2010, 2021), fill_value=0)
avg_per_year = float(counts.mean())

out = {
    'average_business_articles_per_year_europe_2010_2020': avg_per_year,
    'total_business_articles_europe_2010_2020': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_hpBoCyEkmdQ8dpxE2BTDMZ5h': 'file_storage/call_hpBoCyEkmdQ8dpxE2BTDMZ5h.json', 'var_call_CHTsAxGKcK6pTvCGXFgflMSG': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
