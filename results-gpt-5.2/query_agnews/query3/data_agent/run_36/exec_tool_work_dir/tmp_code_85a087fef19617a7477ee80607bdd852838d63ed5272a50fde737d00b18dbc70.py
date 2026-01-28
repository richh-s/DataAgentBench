code = """import json, pandas as pd

# Load metadata (may be file path)
meta_src = var_call_S9CfMDpj1cAxfkfN7iyC5aE1
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_rEU7VaFbbyBDfrASVYqNW73N

df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# Normalize article_id to int
for df in (df_meta, df_arts):
    df['article_id'] = pd.to_numeric(df['article_id'], errors='coerce').astype('Int64')

# Join to get title/description for classification
df = df_meta.merge(df_arts, on='article_id', how='inner')

# Extract year
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year
# keep 2010-2020 inclusive (in case)
df = df[(df['year']>=2010) & (df['year']<=2020)]

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

# Simple keyword-based categorization
business_kw = [
    'business','market','markets','stock','stocks','wall st','dow','nasdaq','s&p',
    'earnings','profit','revenue','bank','banks','banking','finance','financial',
    'economy','economic','gdp','inflation','unemployment','trade','tariff','tariffs',
    'oil','crude','commodities','currency','currencies','forex','euro','bond','bonds',
    'rates','interest rate','central bank','ecb','fed','merger','acquisition','ipo','shares'
]
world_kw = ['iraq','afghanistan','israel','palestinian','war','military','rebels','government','election','terror','u.n.','united nations','diplomat','killed','attack']
sports_kw = ['vs.','defeated','match','tournament','league','nba','nfl','mlb','nhl','soccer','football','tennis','golf','olympic','championship','coach','season','goal','score']
tech_kw = ['software','internet','google','microsoft','apple','iphone','android','ai','robot','space','nasa','science','scientist','research','technology','chip','semiconductor','biotech','vaccine']

def has_any(s, kws):
    return s.apply(lambda x: any(k in x for k in kws))

is_sports = has_any(text, sports_kw)
is_tech = has_any(text, tech_kw)
is_world = has_any(text, world_kw)
is_business = has_any(text, business_kw)

# Assign category with priority to reduce false positives (oil often business; war often world)
cat = pd.Series(['Other']*len(df), index=df.index)
cat[is_sports] = 'Sports'
cat[~is_sports & is_tech] = 'Science/Technology'
cat[~is_sports & ~is_tech & is_world] = 'World'
cat[~is_sports & ~is_tech & ~is_world & is_business] = 'Business'
# If both world and business, choose based on presence of finance terms
cat[(~is_sports & ~is_tech) & is_world & is_business] = 'Business'

df['category'] = cat

# Filter to business
dfb = df[df['category']=='Business']

counts = dfb.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles_2010_2020': int(counts.sum()),
    'years': {int(k): int(v) for k,v in counts.items()}
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_S9CfMDpj1cAxfkfN7iyC5aE1': 'file_storage/call_S9CfMDpj1cAxfkfN7iyC5aE1.json', 'var_call_rEU7VaFbbyBDfrASVYqNW73N': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
