code = """import json, pandas as pd

# Load Europe 2010-2020 metadata
meta_src = var_call_8V5cQzPAzova67XO6zmytQ9F
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts_src = var_call_RNqm7ROcrviGPHrnMHu5rrMg
if isinstance(arts_src, str):
    with open(arts_src, 'r', encoding='utf-8') as f:
        arts = json.load(f)
else:
    arts = arts_src

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize types
meta_df['article_id'] = meta_df['article_id'].astype(str)
arts_df['article_id'] = arts_df['article_id'].astype(str)
meta_df['year'] = meta_df['publication_date'].str.slice(0,4).astype(int)

# Keyword-based classifier for Business
biz_kw = [
    'stock','stocks','wall st','wall street','market','markets','shares','bond','bonds','treasury','yield','yields',
    'nasdaq','dow','s&p','sp500','s&p 500','ftse','dax','nikkei','hang seng',
    'economy','economic','gdp','inflation','deflation','recession','jobs','unemployment','payroll',
    'company','companies','firm','bank','banks','banking','loan','loans','mortgage','credit','debt',
    'profit','profits','earnings','revenue','sales','forecast','guidance',
    'deal','merger','acquisition','ipo','buyout','private equity','hedge fund',
    'oil','crude','gas','energy prices','commodity','commodities','gold','copper',
    'currency','currencies','dollar','euro','yen','pound','forex','exchange rate',
    'rate hike','interest rate','fed','central bank','ecb'
]

def is_business(text: str) -> bool:
    if not isinstance(text, str):
        return False
    t = text.lower()
    return any(k in t for k in biz_kw)

merged = meta_df.merge(arts_df, on='article_id', how='left')
merged['text'] = (merged['title'].fillna('') + ' ' + merged['description'].fillna('')).str.strip()
merged['is_business'] = merged['text'].apply(is_business)

biz = merged[merged['is_business']]
counts_by_year = biz.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = float(counts_by_year.mean())

out = {
    'average_business_articles_per_year_europe_2010_2020': avg_per_year,
    'total_business_articles': int(counts_by_year.sum()),
    'years_counted': 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8V5cQzPAzova67XO6zmytQ9F': 'file_storage/call_8V5cQzPAzova67XO6zmytQ9F.json', 'var_call_RNqm7ROcrviGPHrnMHu5rrMg': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
