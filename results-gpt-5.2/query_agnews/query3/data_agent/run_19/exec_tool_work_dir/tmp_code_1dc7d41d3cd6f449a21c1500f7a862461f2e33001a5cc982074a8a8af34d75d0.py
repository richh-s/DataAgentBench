code = """import json, pandas as pd

# Load metadata (Europe, 2010-2020) from file if needed
meta = var_call_d9dBXQwqLcCDu6tYFfP8ecja
if isinstance(meta, str):
    with open(meta, 'r', encoding='utf-8') as f:
        meta = json.load(f)

arts = var_call_UKlSyxpmQXH72ZONyb0woRiP

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = pd.to_numeric(meta_df['article_id'], errors='coerce')
arts_df['article_id'] = pd.to_numeric(arts_df['article_id'], errors='coerce')

# year
meta_df['year'] = pd.to_datetime(meta_df['publication_date'], errors='coerce').dt.year
meta_df = meta_df.dropna(subset=['article_id','year'])
meta_df['year'] = meta_df['year'].astype(int)

# join to get title/description
df = meta_df.merge(arts_df, on='article_id', how='inner')

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    business_terms = [
        'stock', 'stocks', 'wall st', 'wall street', 'market', 'markets', 'shares', 'bond', 'bonds',
        'earnings', 'profit', 'revenue', 'sales', 'quarter', 'q1', 'q2', 'q3', 'q4',
        'ipo', 'merger', 'acquisition', 'takeover', 'buyout', 'deal',
        'bank', 'banks', 'banking', 'loan', 'loans', 'credit',
        'oil', 'crude', 'gas', 'energy prices',
        'economy', 'economic', 'inflation', 'recession', 'gdp',
        'company', 'companies', 'firm', 'investment', 'investor', 'private equity',
        'currency', 'dollar', 'euro', 'yen', 'pound',
        'trade', 'exports', 'imports', 'tariff',
        'unemployment', 'jobs', 'labor',
        'fed', 'central bank', 'interest rate', 'rates'
    ]
    # score
    score = sum(1 for t in business_terms if t in text)
    return score >= 2 or ('reuters -' in text and score >= 1)

biz_mask = df.apply(is_business, axis=1)
biz_df = df[biz_mask].copy()

counts = biz_df.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = counts.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles_2010_2020': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_d9dBXQwqLcCDu6tYFfP8ecja': 'file_storage/call_d9dBXQwqLcCDu6tYFfP8ecja.json', 'var_call_UKlSyxpmQXH72ZONyb0woRiP': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
