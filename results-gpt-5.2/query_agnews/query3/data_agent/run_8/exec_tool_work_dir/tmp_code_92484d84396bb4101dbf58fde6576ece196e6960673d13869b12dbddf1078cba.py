code = """import json, pandas as pd

meta_src = var_call_5k9I10gLVT21EDkbLnuj8YMK
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_xWKtAoGlsr10SGGprYowDesu

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# normalize ids to int
for df in (df_meta, df_arts):
    df['article_id'] = pd.to_numeric(df['article_id'], errors='coerce').astype('Int64')

df = df_meta.merge(df_arts, on='article_id', how='inner')

# categorize using simple keyword rules
biz_kw = [
    'stock','stocks','shares','wall st','wall street','market','markets','dow','nasdaq','s&p',
    'earnings','profit','revenue','bank','banks','loan','loans','credit','mortgage','fed','interest rate','rates',
    'economy','economic','inflation','gdp','jobs','unemployment','trade','tariff','exports','imports',
    'oil','crude','gas','energy','prices','price','gold','currency','dollar','euro','yen',
    'company','companies','firm','merger','acquisition','ipo','invest','investment','fund','hedge','private equity',
    'retail','sales','consumer','business','finance','financial','budget','debt','bonds'
]

def is_business(text):
    if text is None:
        return False
    t = str(text).lower()
    return any(k in t for k in biz_kw)

combo = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['is_business'] = combo.map(is_business)

df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

biz = df[(df['is_business']) & (df['year'].between(2010, 2020))]

counts = biz.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = float(counts.mean())

out = {
    'average_business_articles_per_year_europe_2010_2020': avg_per_year,
    'total_business_articles': int(counts.sum()),
    'years_counted': 11,
    'yearly_counts': {str(int(y)): int(c) for y,c in counts.items()}
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5k9I10gLVT21EDkbLnuj8YMK': 'file_storage/call_5k9I10gLVT21EDkbLnuj8YMK.json', 'var_call_xWKtAoGlsr10SGGprYowDesu': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
