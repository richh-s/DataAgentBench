code = """import json, pandas as pd

# Load metadata (may be file path)
meta = var_call_lFdywDSuhZ9RaugKyonNfafs
if isinstance(meta, str):
    with open(meta, 'r', encoding='utf-8') as f:
        meta = json.load(f)

arts = var_call_g66MeiBEyfnqKgU9r5fX44Lo

dfm = pd.DataFrame(meta)
dfa = pd.DataFrame(arts)

# Normalize types
dfm['article_id'] = dfm['article_id'].astype(int)
dfa['article_id'] = dfa['article_id'].astype(int)

# Join Europe 2010-2020 articles with text
joined = dfm.merge(dfa, on='article_id', how='inner')
joined['year'] = joined['publication_date'].str.slice(0,4).astype(int)

# Heuristic classification for Business based on title+description keywords
text = (joined['title'].fillna('') + ' ' + joined['description'].fillna('')).str.lower()

business_kw = [
    'stock', 'stocks', 'wall st', 'wall street', 'market', 'markets', 'shares', 'equity', 'equities',
    'bond', 'bonds', 'treasury', 'fed', 'federal reserve', 'ecb', 'central bank', 'interest rate', 'rates',
    'inflation', 'gdp', 'economy', 'economic', 'recession', 'growth', 'unemployment',
    'oil', 'crude', 'gas', 'energy', 'opec',
    'bank', 'banks', 'banking', 'loan', 'loans', 'mortgage', 'credit',
    'profit', 'profits', 'earnings', 'revenue', 'sales', 'forecast', 'guidance',
    'company', 'companies', 'corp', 'corporate', 'ceo', 'cfo', 'ipo',
    'merger', 'acquisition', 'buyout', 'deal', 'investment', 'investor', 'private equity',
    'dollar', 'euro', 'yen', 'currency', 'fx', 'forex',
    'trade', 'tariff', 'exports', 'imports',
    'prices', 'commodities'
]
pattern = r'\\b(' + '|'.join([pd.re.escape(k) for k in business_kw]) + r')\\b'
# pandas has no re.escape; use python re
import re
pattern = r'\\b(' + '|'.join([re.escape(k) for k in business_kw]) + r')\\b'

is_business = text.str.contains(pattern, regex=True)
joined_b = joined[is_business].copy()

counts = joined_b.groupby('year')['article_id'].nunique().reindex(range(2010, 2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(counts.sum()),
    'years': {int(k): int(v) for k,v in counts.to_dict().items()}
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lFdywDSuhZ9RaugKyonNfafs': 'file_storage/call_lFdywDSuhZ9RaugKyonNfafs.json', 'var_call_g66MeiBEyfnqKgU9r5fX44Lo': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
