code = """import json, pandas as pd

def load_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

meta = load_result(var_call_BgWaTB8cCSRkch0ZTC1n0fMK)
arts = load_result(var_call_72ql9PHSKdrJZuyRqMVDYjez)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Heuristic business classifier based on title+description keywords
business_kw = [
    'business','market','stocks','stock','shares','equity','earnings','revenue','profit','loss','ipo','merger','acquisition','buyout',
    'company','firm','corporate','ceo','cfo','investor','investment','fund','hedge','private equity','venture',
    'bank','banking','lender','loan','credit','bond','bonds','yield','treasury','dollar','euro','currency','forex',
    'economy','economic','gdp','inflation','recession','growth','trade','tariff','export','import',
    'oil','crude','gas','energy','opec','gold','commodity','commodities','price','prices'
]

def is_business(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    return any(kw in text for kw in business_kw)

arts_df['is_business'] = arts_df.apply(is_business, axis=1)

joined = meta_df.merge(arts_df[['article_id','is_business']], on='article_id', how='inner')
joined['year'] = joined['publication_date'].str.slice(0,4).astype(int)

biz = joined[joined['is_business']]
counts = biz.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_BgWaTB8cCSRkch0ZTC1n0fMK': 'file_storage/call_BgWaTB8cCSRkch0ZTC1n0fMK.json', 'var_call_72ql9PHSKdrJZuyRqMVDYjez': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
