code = """import json, pandas as pd

# Load Europe articles (2010-2020) metadata
meta_src = var_call_eNzxKJwXoSQzQzzT3dO2JWet
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_ZvmQHT2o9hiV8AQMKDdZJHDp

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize ids to int
meta_df['article_id'] = pd.to_numeric(meta_df['article_id'])
arts_df['article_id'] = pd.to_numeric(arts_df['article_id'])

# join to get text
df = meta_df.merge(arts_df, on='article_id', how='inner')

def is_business(title, desc):
    text = f"{title or ''} {desc or ''}".lower()
    keywords = [
        'stock','stocks','share','shares','wall st','wall street','dow','nasdaq','s&p',
        'earnings','revenue','profit','loss','ipo','bond','bonds','yield','inflation','gdp',
        'economy','economic','market','markets','trade','tariff','oil','crude','gas','opec',
        'company','companies','firm','bank','banks','central bank','ecb','boe','fed',
        'currency','euro','dollar','forex','investment','investor','merger','acquisition',
        'futures','commodity','commodities','finance','financial','business'
    ]
    return any(k in text for k in keywords)

bus_mask = df.apply(lambda r: is_business(r.get('title',''), r.get('description','')), axis=1)
bus_df = df[bus_mask].copy()

bus_df['year'] = pd.to_datetime(bus_df['publication_date'], errors='coerce').dt.year
counts = bus_df.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    "average_business_articles_per_year_europe_2010_2020": float(avg_per_year),
    "total_business_articles": int(counts.sum()),
    "years": 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_eNzxKJwXoSQzQzzT3dO2JWet': 'file_storage/call_eNzxKJwXoSQzQzzT3dO2JWet.json', 'var_call_ZvmQHT2o9hiV8AQMKDdZJHDp': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
