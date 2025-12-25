code = """import json, pandas as pd

with open(var_call_g7efMmaQy8JV8MrexZJedPto, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_75HT1U5oUH1I5E6Yq7ak9YWn

meta_df = pd.DataFrame(europe_meta)
art_df = pd.DataFrame(articles)

meta_df['article_id'] = meta_df['article_id'].astype(int)
art_df['article_id'] = art_df['article_id'].astype(int)

df = meta_df.merge(art_df, on='article_id', how='inner')

business_keywords = ['stock', 'stocks', 'market', 'markets', 'wall st', 'wall street', 'dow', 'nasdaq', 's&p', 'bond', 'bonds', 'treasury', 'treasuries', 'oil', 'crude', 'gold', 'merger', 'acquisition', 'earnings', 'profit', 'profits', 'losses', 'ipo', 'share', 'shares', 'currency', 'currencies', 'dollar', 'euro', 'yen', 'business', 'company', 'companies', 'corporate', 'economy', 'economic', 'finance', 'financial', 'fund', 'funds', 'bank', 'banks', 'banking', 'investment', 'investor', 'investors', 'revenue', 'sales', 'retail', 'trade', 'trading']
kw = [k.lower() for k in business_keywords]

def is_business(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    return any(k in text for k in kw)

df['is_business'] = df.apply(is_business, axis=1)

bdf = df[df['is_business']].copy()

bdf['year'] = bdf['publication_date'].str.slice(0,4).astype(int)

bdf = bdf[(bdf['year'] >= 2010) & (bdf['year'] <= 2020)]

counts_per_year = bdf.groupby('year').size()

all_years = list(range(2010, 2021))
counts = [int(counts_per_year.get(y, 0)) for y in all_years]

avg_per_year = float(sum(counts)) / float(len(all_years)) if all_years else 0.0

counts_per_year_dict = {str(int(y)): int(counts_per_year.get(y, 0)) for y in all_years}

result = {'counts_per_year': counts_per_year_dict, 'average_business_articles_per_year_europe_2010_2020': avg_per_year}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_g7efMmaQy8JV8MrexZJedPto': 'file_storage/call_g7efMmaQy8JV8MrexZJedPto.json', 'var_call_75HT1U5oUH1I5E6Yq7ak9YWn': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
