code = """import json, pandas as pd

# Load full Europe metadata from file
path = var_call_Yef5OWDWdgvc5n1ewATJRYIA
with open(path, 'r') as f:
    europe_meta = json.load(f)

articles = var_call_sJizxzSOeKO62w1urYb6RzQI

meta_df = pd.DataFrame(europe_meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

art_df = pd.DataFrame(articles)
art_df['article_id'] = art_df['article_id'].astype(int)

# Join
df = meta_df.merge(art_df, on='article_id', how='left')

# Simple business classification heuristic
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_keywords = [
    'stock', 'stocks', 'market', 'markets', 'wall st', 'wall street', 'dow jones', 'nasdaq', 's&p',
    'ftse', 'dax', 'nikkei', 'bond', 'bonds', 'treasury', 'treasuries',
    'oil', 'crude', 'gold', 'commodity', 'commodities',
    'economy', 'economic', 'growth', 'recession', 'inflation', 'gdp',
    'bank', 'banks', 'banking', 'loan', 'loans', 'mortgage', 'credit', 'debt',
    'company', 'companies', 'corporate', 'business', 'firm', 'firms', 'enterprise',
    'profit', 'profits', 'loss', 'losses', 'revenue', 'earnings', 'dividend',
    'merger', 'acquisition', 'm&a', 'ipo', 'initial public offering',
    'share', 'shares', 'shareholder', 'shareholders', 'fund', 'funds', 'hedge fund',
    'currency', 'currencies', 'forex', 'foreign exchange',
    'trade', 'trading', 'tariff', 'tariffs',
    'finance', 'financial', 'fiscal', 'budget',
    'retail', 'sales', 'startup', 'start-up', 'entrepreneur', 'venture capital',
]

pattern = '|'.join([k.replace(' ', '\\s+') for k in business_keywords])
mask_business = text.str.contains(pattern, regex=True)

biz_df = df[mask_business].copy()

counts_per_year = biz_df.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = counts_per_year.mean()

result = round(float(avg_per_year), 2)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Yef5OWDWdgvc5n1ewATJRYIA': 'file_storage/call_Yef5OWDWdgvc5n1ewATJRYIA.json', 'var_call_sJizxzSOeKO62w1urYb6RzQI': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
