code = """import json, pandas as pd

meta = var_call_uljFRvJzXMSI5cWpF55yhuh0
if isinstance(meta, str):
    with open(meta, 'r') as f:
        meta = json.load(f)
df_meta = pd.DataFrame(meta)
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_meta['year'] = pd.to_datetime(df_meta['publication_date'], errors='coerce').dt.year
df_meta = df_meta[(df_meta['year']>=2010) & (df_meta['year']<=2020)]

arts = var_call_pZg0UKhmQZFgsdXH2NCUEiuT
if isinstance(arts, str):
    with open(arts,'r') as f:
        arts = json.load(f)
df_arts = pd.DataFrame(arts)
df_arts['article_id'] = df_arts['article_id'].astype(int)

df = df_meta.merge(df_arts, on='article_id', how='left')

def is_business(row):
    title = row.get('title')
    desc = row.get('description')
    title = '' if title is None or (isinstance(title,float) and pd.isna(title)) else str(title)
    desc = '' if desc is None or (isinstance(desc,float) and pd.isna(desc)) else str(desc)
    text = (title + ' ' + desc).lower()
    kws = [
        'stock','stocks','wall st','wall street','market','markets','nasdaq','dow','s&p',
        'economy','economic','gdp','inflation','recession','jobs','unemployment',
        'oil','crude','gas','opec',
        'bank','banks','banking','interest rate','rates','fed','ecb','central bank',
        'currency','euro','dollar','yen','forex',
        'earnings','profit','revenue','sales','ipo','merger','acquisition','deal',
        'company','companies','corporate','firm','investment','investor','fund','private equity',
        'trade','tariff','exports','imports'
    ]
    return any(k in text for k in kws)

biz_mask = df.apply(is_business, axis=1)
df_biz = df[biz_mask].copy()

counts = df_biz.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles_2010_2020': int(counts.sum()),
    'years_counted': int(counts.shape[0])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_uljFRvJzXMSI5cWpF55yhuh0': 'file_storage/call_uljFRvJzXMSI5cWpF55yhuh0.json', 'var_call_pZg0UKhmQZFgsdXH2NCUEiuT': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
