code = """import json, pandas as pd

def load_records(maybe_path_or_records):
    if isinstance(maybe_path_or_records, str) and maybe_path_or_records.endswith('.json'):
        with open(maybe_path_or_records, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_records

meta = load_records(var_call_yGQamuWJaJrMXU4LkwFtuwQx)
arts = load_records(var_call_PnfoBnyOfnPzQJzbX2h5ZfuR)

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# normalize types
for c in ['article_id','year']:
    if c in df_meta.columns:
        df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce')

df_arts['article_id'] = pd.to_numeric(df_arts['article_id'], errors='coerce')

df = df_meta.merge(df_arts, on='article_id', how='inner')

business_kw = [
    'stock','stocks','shares','share','market','wall st','wall street','dow','nasdaq','s&p','sp500',
    'earnings','profit','loss','revenue','sales','quarter','forecast','guidance',
    'bank','banks','banking','fed','ecb','interest rate','rates','inflation','bond','bonds','treasury',
    'currency','euro','dollar','yen','forex',
    'oil','crude','gas','energy','opec',
    'company','firm','ceo','cfo','merger','acquisition','ipo','deal','invest','investment','fund',
    'economy','economic','gdp','unemployment','jobs','trade','tariff','export','import',
    'real estate','housing','mortgage'
]

def is_business(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    return any(k in t for k in business_kw)

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
mask = text.apply(is_business)

df_biz = df.loc[mask, ['year','article_id']].drop_duplicates()
counts = df_biz.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)
avg_per_year = float(counts.mean())

out = {
    'avg_business_articles_per_year_europe_2010_2020': avg_per_year,
    'total_business_articles_2010_2020': int(counts.sum()),
    'years': 11
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_yGQamuWJaJrMXU4LkwFtuwQx': 'file_storage/call_yGQamuWJaJrMXU4LkwFtuwQx.json', 'var_call_PnfoBnyOfnPzQJzbX2h5ZfuR': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
