code = """import json, pandas as pd
from pathlib import Path

# Load metadata result (may be file path)
meta_src = var_call_2NQvPeTlAsOYXBtwQYVrlo5t
if isinstance(meta_src, str) and Path(meta_src).exists():
    meta = json.loads(Path(meta_src).read_text())
else:
    meta = meta_src

arts = var_call_HhgP1Hp0pwsUtpmZbezDm7vj

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

# Simple keyword-based categorization for Business
text = (arts_df['title'].fillna('') + ' ' + arts_df['description'].fillna('')).str.lower()
keywords = [
    'stock','stocks','market','markets','wall st','wall street','nasdaq','dow','s&p',
    'earnings','profit','revenue','quarter','ipo','shares','share','investor','investment','bank',
    'banks','fed','central bank','interest rate','rates','bond','bonds','debt','credit','loan','loans',
    'merger','acquisition','takeover','buyout','deal','currency','dollar','euro','yen','forex',
    'oil','crude','gas','opec','inflation','gdp','economy','economic','trade','tariff','jobs','unemployment',
    'company','companies','ceo','corporate','business','finance','financial','industry'
]
pattern = r'(' + r'|'.join([pd.re.escape(k) for k in keywords]) + r')'
arts_df['is_business'] = text.str.contains(pattern, regex=True)

# Join Europe 2010-2020 metadata with business classification
joined = meta_df.merge(arts_df[['article_id','is_business']], on='article_id', how='inner')
biz = joined[joined['is_business']]

counts = biz.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'yearly_counts': {int(k): int(v) for k,v in counts.items()},
    'total_business_articles': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_2NQvPeTlAsOYXBtwQYVrlo5t': 'file_storage/call_2NQvPeTlAsOYXBtwQYVrlo5t.json', 'var_call_HhgP1Hp0pwsUtpmZbezDm7vj': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
