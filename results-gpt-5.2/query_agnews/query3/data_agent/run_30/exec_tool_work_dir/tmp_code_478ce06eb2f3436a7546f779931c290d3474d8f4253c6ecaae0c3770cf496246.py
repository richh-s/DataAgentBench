code = """import json, pandas as pd, re

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

meta = load_records(var_call_JbbLgkBzq2pGS9SsF5Gtwh1r)
arts = load_records(var_call_G6jQdlVyzerTE78SLfgA3wkF)

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

for c in ['article_id']:
    df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce')
    df_arts[c] = pd.to_numeric(df_arts[c], errors='coerce')

df = df_meta.merge(df_arts, on='article_id', how='inner')

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()
keywords = [
    'stock','stocks','wall st','dow','nasdaq','s&p','share','shares','earnings','profit','revenue',
    'inflation','gdp','economy','economic','bank','banks','central bank','ecb','fed','interest rate',
    'bond','bonds','debt','credit','mortgage','loan','loans','investment','investor','hedge fund',
    'oil','crude','gas','currency','euro','dollar','forex','trade','tariff',
    'merger','acquisition','ipo','market','markets','retail','sales','jobs','unemployment'
]
pattern = r'(' + '|'.join([re.escape(k) for k in keywords]) + r')'

is_business = text.str.contains(pattern, regex=True)

year = pd.to_datetime(df['publication_date'], errors='coerce').dt.year
mask_year = year.between(2010, 2020)

df_biz = df[is_business & mask_year].copy()
df_biz['year'] = year[is_business & mask_year]

counts = df_biz.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(counts.sum()),
    'years': 11
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JbbLgkBzq2pGS9SsF5Gtwh1r': 'file_storage/call_JbbLgkBzq2pGS9SsF5Gtwh1r.json', 'var_call_G6jQdlVyzerTE78SLfgA3wkF': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
