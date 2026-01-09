code = """import json, pandas as pd, re

meta_src = var_call_tz1dhU4Awf3iHFAz1xrnAf2n
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src
arts = var_call_w7cW1s4sv9fce2pFpGspMVAv

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

for c in ['article_id']:
    df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce')
    df_arts[c] = pd.to_numeric(df_arts[c], errors='coerce')

df = df_meta.merge(df_arts, on='article_id', how='left')
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

df = df[(df['year']>=2010) & (df['year']<=2020) & (df['region']=='Europe')]

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_kw = [
    'stock','stocks','wall st','wall street','market','markets','dow','nasdaq','s&p','share','shares','equity','equities',
    'bank','banks','banking','fed','central bank','interest rate','rates','bond','bonds','treasury','yield',
    'earnings','profit','revenue','sales','forecast','guidance','quarter',
    'economy','economic','inflation','gdp','recession','unemployment','jobs','consumer',
    'oil','crude','gas','energy','prices','price','commodity','commodities','gold','copper',
    'trade','tariff','export','imports','merger','acquisition','ipo','company','companies','corporate','ceo','cfo',
    'investment','investor','fund','hedge','private equity','venture','startup',
    'currency','dollar','euro','yen','forex','exchange rate'
]
pat = '(' + '|'.join([re.escape(k) for k in business_kw]) + ')'

df['is_business'] = text.str.contains(pat, regex=True, na=False)

by_year = df[df['is_business']].groupby('year')['article_id'].count().reindex(range(2010,2021), fill_value=0)
avg_per_year = by_year.mean()

out = json.dumps({
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(by_year.sum()),
    'years_count': 11
})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_tz1dhU4Awf3iHFAz1xrnAf2n': 'file_storage/call_tz1dhU4Awf3iHFAz1xrnAf2n.json', 'var_call_w7cW1s4sv9fce2pFpGspMVAv': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
