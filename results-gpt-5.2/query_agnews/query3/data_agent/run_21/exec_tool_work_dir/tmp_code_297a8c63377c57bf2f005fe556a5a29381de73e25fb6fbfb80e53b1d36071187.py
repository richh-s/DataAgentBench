code = """import json, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

meta = load_maybe_path(var_call_GvZNkNbfOQ4fJNhyFMtzZCN1)
arts = load_maybe_path(var_call_ngxTxRsa1p1EkuBgAlf7oB8c)

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# normalize types
for c in ['article_id']:
    df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce')
    df_arts[c] = pd.to_numeric(df_arts[c], errors='coerce')
df_meta = df_meta.dropna(subset=['article_id','publication_date'])
df_arts = df_arts.dropna(subset=['article_id'])

df = df_meta.merge(df_arts, on='article_id', how='inner')

# categorize via simple keyword rules in title+description
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_kw = [
    'stocks','stock','wall st','wall street','reuters','nasdaq','dow','s&p','earnings','profit','revenue',
    'company','companies','corp','corporation','inc','ltd','ipo','shares','bond','bonds','treasury','fed',
    'central bank','inflation','gdp','economy','economic','bank','banks','banking','credit','loan','loans',
    'oil','crude','gas','prices','price','market','markets','trade','tariff','currency','dollar','euro',
    'merger','acquisition','buyout','investment','investors','fund','hedge','private equity'
]

mask_business = text.apply(lambda s: any(k in s for k in business_kw))

# compute yearly counts for business
years = pd.to_datetime(df.loc[mask_business, 'publication_date'], errors='coerce').dt.year
counts = years.value_counts().to_dict()
# ensure all years 2010-2020 included with 0
counts_full = {y:int(counts.get(y,0)) for y in range(2010,2021)}
avg = sum(counts_full.values())/len(counts_full)

out = {'average_business_articles_per_year_europe_2010_2020': avg, 'total_business_articles': int(sum(counts_full.values())), 'years': counts_full}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_GvZNkNbfOQ4fJNhyFMtzZCN1': 'file_storage/call_GvZNkNbfOQ4fJNhyFMtzZCN1.json', 'var_call_ngxTxRsa1p1EkuBgAlf7oB8c': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
