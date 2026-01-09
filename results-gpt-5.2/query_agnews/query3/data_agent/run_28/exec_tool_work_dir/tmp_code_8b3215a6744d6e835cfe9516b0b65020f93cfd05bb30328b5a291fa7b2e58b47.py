code = """import json, pandas as pd
from pathlib import Path

# Load Europe metadata (may be file path)
meta = var_call_XTvoMOv9eRi3iYI909Vw5BoZ
if isinstance(meta, str) and meta.endswith('.json'):
    meta = json.loads(Path(meta).read_text())

arts = var_call_HHRtLDeqjG5Qum38d6KxGLJh
if isinstance(arts, str) and arts.endswith('.json'):
    arts = json.loads(Path(arts).read_text())

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# simple keyword-based business classifier
business_kw = [
    'stock','stocks','market','markets','wall st','wall street','nasdaq','dow','s&p',
    'economy','economic','gdp','inflation','deflation','recession','job','jobs','unemployment',
    'bank','banks','banking','central bank','ecb','fed','interest rate','rates',
    'company','companies','corp','corporate','earnings','profit','profits','revenue','sales',
    'merger','acquisition','ipo','shares','share','bond','bonds','debt','credit',
    'currency','euro','dollar','yen','pound','forex','exchange rate',
    'oil','crude','gas','energy prices','commodity','commodities','gold'
]

def is_business(title, desc):
    text = f"{title or ''} {desc or ''}".lower()
    return any(k in text for k in business_kw)

arts_df['is_business'] = arts_df.apply(lambda r: is_business(r.get('title',''), r.get('description','')), axis=1)

merged = meta_df.merge(arts_df[['article_id','is_business']], on='article_id', how='inner')
merged['year'] = merged['publication_date'].str.slice(0,4).astype(int)

biz = merged[merged['is_business']]
counts = biz.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg),
    'total_business_articles': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_XTvoMOv9eRi3iYI909Vw5BoZ': 'file_storage/call_XTvoMOv9eRi3iYI909Vw5BoZ.json', 'var_call_HHRtLDeqjG5Qum38d6KxGLJh': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
