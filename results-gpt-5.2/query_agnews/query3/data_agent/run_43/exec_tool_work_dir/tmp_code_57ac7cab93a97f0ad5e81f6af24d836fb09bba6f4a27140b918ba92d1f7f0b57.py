code = """import json, pandas as pd, re

meta_src = var_call_AsQVsqWgQck7dUq4WyMgZARr
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src
arts = var_call_i1IjH5CBoAdLAtRaOhwm1N6C

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

df = meta_df.merge(arts_df, on='article_id', how='inner')
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

biz_kw = ['stock','stocks','wall st','wall street','market','markets','shares','bond','bonds','treasury',
          'earnings','profit','revenue','sales','ipo','merger','acquisition','buyout','takeover',
          'company','companies','corp','inc','ltd','ceo','cfo','bank','banks','banking','interest rate',
          'inflation','gdp','economy','economic','fed','central bank','euro','dollar','yen',
          'oil','crude','gas','opec','gold','copper','commodity','commodities','trade','tariff',
          'unemployment','jobs','housing','real estate','retail','consumer','startup','investment','investor']
pattern = r'(' + '|'.join([re.escape(k) for k in biz_kw]) + r')'
is_business = text.str.contains(pattern, regex=True)

biz_df = df[is_business].copy()
biz_df['year'] = pd.to_datetime(biz_df['publication_date'], errors='coerce').dt.year

counts = biz_df.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)
avg = counts.mean()

out = {'average_business_articles_per_year_europe_2010_2020': float(avg)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AsQVsqWgQck7dUq4WyMgZARr': 'file_storage/call_AsQVsqWgQck7dUq4WyMgZARr.json', 'var_call_i1IjH5CBoAdLAtRaOhwm1N6C': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
