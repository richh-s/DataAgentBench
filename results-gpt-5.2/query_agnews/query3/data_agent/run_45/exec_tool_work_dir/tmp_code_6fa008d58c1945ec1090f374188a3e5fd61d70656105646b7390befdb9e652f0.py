code = """import json, pandas as pd

# Load metadata (Europe, 2010-2020)
meta_src = var_call_utg7p3ORjAWcy7pxUIXgr0rd
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

articles = var_call_8E11XG1tmEmsI0Pw5Rw1KXEW

df_meta = pd.DataFrame(meta)
df_art = pd.DataFrame(articles)

# normalize types
for c in ['article_id']:
    df_meta[c] = pd.to_numeric(df_meta[c], errors='coerce')
    df_art[c] = pd.to_numeric(df_art[c], errors='coerce')

df_meta['publication_date'] = pd.to_datetime(df_meta['publication_date'], errors='coerce')
df_meta = df_meta.dropna(subset=['article_id','publication_date'])
df_meta['year'] = df_meta['publication_date'].dt.year

# join to get title/description for classification
# only need those in meta
df = df_meta.merge(df_art, on='article_id', how='left')

# heuristic business classifier based on title+description
text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

business_terms = [
    'stock','stocks','shares','share','bond','bonds','equity','equities','wall st','wall street','dow','nasdaq','s&p','sp500',
    'earnings','revenue','profit','loss','quarter','q1','q2','q3','q4','ipo','merger','acquisition','buyout','takeover',
    'ceo','cfo','company','firm','bank','banks','banking','loan','credit','debt','default','interest rate','rates','fed',
    'central bank','inflation','gdp','economy','economic','recession','market','markets','investors','investment',
    'oil','crude','gold','commodity','commodities','currency','forex','euro','dollar','yen','trade','exports','imports',
    'unemployment','jobs','retail','consumer','sales','budget','deficit','tax','tariff','manufacturing','industry',
    'business','finance','financial','fund','hedge','private equity'
]

pattern = r'(' + '|'.join([pd.regex.escape(t) if hasattr(pd, 'regex') else t for t in business_terms]) + r')'
# pandas doesn't expose regex.escape reliably; use re
import re
pattern = r'(' + '|'.join([re.escape(t) for t in business_terms]) + r')'

is_business = text.str.contains(pattern, regex=True, na=False)

df_bus = df[is_business].copy()

counts = df_bus.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles_2010_2020': int(counts.sum()),
    'years': {int(k): int(v) for k,v in counts.items()}
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_utg7p3ORjAWcy7pxUIXgr0rd': 'file_storage/call_utg7p3ORjAWcy7pxUIXgr0rd.json', 'var_call_8E11XG1tmEmsI0Pw5Rw1KXEW': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
