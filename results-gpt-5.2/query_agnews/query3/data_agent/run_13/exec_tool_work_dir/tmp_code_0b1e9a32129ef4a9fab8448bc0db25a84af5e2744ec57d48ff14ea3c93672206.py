code = """import json, pandas as pd

# load europe metadata rows
meta_src = var_call_MEMWyF1lO2RB1UrO0UqQhuP2
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

art = var_call_cgx9Irx7lDjvMufxqmEqLGoi

df_meta = pd.DataFrame(meta)
df_art = pd.DataFrame(art)

# parse year
df_meta['year'] = df_meta['publication_date'].str.slice(0,4).astype(int)

# classify category based on title+description keywords
text = (df_art['title'].fillna('') + ' ' + df_art['description'].fillna('')).str.lower()

def is_business(s: str) -> bool:
    kws = [
        'stock','stocks','wall st','wall street','dow','nasdaq','s&p',
        'market','markets','shares','share','equity','equities','bond','bonds','yield',
        'earnings','profit','revenue','quarter','q1','q2','q3','q4','ipo','merger','acquisition',
        'bank','banks','credit','loan','mortgage','interest rate','fed','ecb','central bank',
        'inflation','gdp','economy','economic','jobs','unemployment',
        'oil','crude','brent','wti','gas','prices','price','commodity','commodities',
        'currency','currencies','euro','dollar','forex','exchange rate',
        'company','companies','corporate','ceo','cfo','firm','investment','investor','investors',
        'trade','tariff','exports','imports','manufacturing','retail','sales'
    ]
    return any(k in s for k in kws)

# vectorized apply
bus_mask = text.apply(is_business)

df_art['is_business'] = bus_mask

# join with europe and year range (already filtered), count business per year
# ensure article_id same type
for d in (df_meta, df_art):
    d['article_id'] = d['article_id'].astype(str)

merged = df_meta.merge(df_art[['article_id','is_business']], on='article_id', how='inner')
merged = merged[merged['is_business']]

counts = merged.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles_europe_2010_2020': int(counts.sum()),
    'years_counted': 11,
    'by_year': {str(int(k)): int(v) for k,v in counts.items()}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_MEMWyF1lO2RB1UrO0UqQhuP2': 'file_storage/call_MEMWyF1lO2RB1UrO0UqQhuP2.json', 'var_call_cgx9Irx7lDjvMufxqmEqLGoi': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
