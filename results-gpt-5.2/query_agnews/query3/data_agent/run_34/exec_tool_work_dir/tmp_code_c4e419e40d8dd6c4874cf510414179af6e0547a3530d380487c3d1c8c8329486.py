code = """import json, pandas as pd, re

meta = var_call_y1VZDC60uHQCLvxqPwESFtYB
if isinstance(meta, str):
    with open(meta, 'r') as f:
        meta = json.load(f)
arts = var_call_Lb3eWWowrTVOFrhUxnwshEGB

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

df = meta_df.merge(arts_df, on='article_id', how='inner')
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

keywords = [
    'stock','stocks','market','markets','wall st','wall street','nasdaq','dow','s&p','shares','share',
    'earnings','profit','revenue','quarter',
    'oil','crude','gas','opec',
    'inflation','gdp','economy','economic','recession',
    'bank','banks','credit','loan','mortgage','interest rate','fed','ecb',
    'currency','euro','dollar','yen','forex',
    'company','companies','corp','inc','ltd','acquisition','merger','ipo',
    'trade','tariff','export','import','manufacturing','retail','sales'
]
pat = r'(' + '|'.join([re.escape(k) for k in keywords]) + r')'

df['is_business'] = text.str.contains(pat, regex=True, na=False)

df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

df_bus = df[(df['is_business']) & (df['year'].between(2010, 2020))]
counts = df_bus.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = counts.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(counts.sum()),
    'years': {str(int(k)): int(v) for k,v in counts.items()}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_y1VZDC60uHQCLvxqPwESFtYB': 'file_storage/call_y1VZDC60uHQCLvxqPwESFtYB.json', 'var_call_Lb3eWWowrTVOFrhUxnwshEGB': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
