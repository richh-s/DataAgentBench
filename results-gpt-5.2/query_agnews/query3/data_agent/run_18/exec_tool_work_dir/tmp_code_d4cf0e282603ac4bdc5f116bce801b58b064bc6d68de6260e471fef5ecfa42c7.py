code = """import json, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

meta = load_maybe_path(var_call_boWh3WJ0aqtqCvggL8sV03nz)
arts = load_maybe_path(var_call_fofjjkfa3ezwlS5S51vjNbAr)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# simple keyword-based business classifier
business_keywords = [
    'market','stocks','stock','shares','share','bond','bonds','treasury','dow','nasdaq','s&p',
    'earnings','profit','revenue','sales','guidance','ipo','merger','acquisition','buyout',
    'bank','banks','banking','credit','loan','loans','mortgage','fed','central bank','interest rate','rates',
    'oil','crude','gas','energy','opec','inflation','economy','economic','gdp','unemployment',
    'company','companies','corporate','ceo','cfo','firm','business','finance','financial','currency','dollar','euro','yen',
    'trade','exports','import','tariff','manufacturing','retail','consumer','spending','investment','investor','fund','hedge'
]

def is_business(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    return any(k in text for k in business_keywords)

arts_df['is_business'] = arts_df.apply(is_business, axis=1)

joined = meta_df.merge(arts_df[['article_id','is_business']], on='article_id', how='inner')
joined = joined[joined['is_business']].copy()
joined['year'] = pd.to_datetime(joined['publication_date'], errors='coerce').dt.year
joined = joined[(joined['year']>=2010) & (joined['year']<=2020)]

counts = joined.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg_per_year = float(counts.mean())

result = {
    'avg_business_articles_per_year_europe_2010_2020': avg_per_year,
    'total_business_articles': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_boWh3WJ0aqtqCvggL8sV03nz': 'file_storage/call_boWh3WJ0aqtqCvggL8sV03nz.json', 'var_call_fofjjkfa3ezwlS5S51vjNbAr': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
