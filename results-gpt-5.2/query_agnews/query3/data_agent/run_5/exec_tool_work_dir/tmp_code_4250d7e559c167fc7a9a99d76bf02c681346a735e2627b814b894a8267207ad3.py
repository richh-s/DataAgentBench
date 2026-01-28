code = """import json, pandas as pd

# Load metadata (possibly from file)
md = var_call_NA3Frb8jCZGyd1cH3uPX39fE
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

arts = var_call_fBc4TllPzf03MOlPK22brh6v

df_md = pd.DataFrame(md)
df_a = pd.DataFrame(arts)

# Normalize types
for col in ['article_id']:
    df_md[col] = pd.to_numeric(df_md[col], errors='coerce')
    df_a[col] = pd.to_numeric(df_a[col], errors='coerce')

df_md['publication_date'] = pd.to_datetime(df_md['publication_date'], errors='coerce')
df_md = df_md.dropna(subset=['article_id','publication_date'])
df_md['year'] = df_md['publication_date'].dt.year.astype('int64')

# Merge to bring title/description
df = df_md.merge(df_a, on='article_id', how='inner')

def is_business(title, desc):
    text = f"{title or ''} {desc or ''}".lower()
    # business/econ/markets/finance indicators
    kws = [
        'reuters', 'wall st', 'wall street', 'stocks', 'stock', 'share', 'shares',
        'market', 'markets', 'dow', 'nasdaq', 's&p', 'bond', 'bonds', 'yield',
        'oil', 'crude', 'gas', 'opec', 'energy',
        'economy', 'economic', 'gdp', 'inflation', 'jobs', 'unemployment',
        'bank', 'banks', 'central bank', 'ecb', 'interest rate', 'rates',
        'dollar', 'euro', 'currency', 'forex',
        'company', 'companies', 'earnings', 'profit', 'revenue', 'quarter',
        'merger', 'acquisition', 'ipo', 'trade', 'tariff', 'export', 'import'
    ]
    return any(k in text for k in kws)

mask = df.apply(lambda r: is_business(r.get('title',''), r.get('description','')), axis=1)
df_biz = df[mask].copy()

# Count per year 2010-2020 inclusive
years = list(range(2010, 2021))
counts = df_biz.groupby('year')['article_id'].nunique().reindex(years, fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(counts.sum()),
    'years_counted': len(years)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NA3Frb8jCZGyd1cH3uPX39fE': 'file_storage/call_NA3Frb8jCZGyd1cH3uPX39fE.json', 'var_call_fBc4TllPzf03MOlPK22brh6v': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
