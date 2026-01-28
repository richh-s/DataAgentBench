code = """import json, pandas as pd

# Load Europe metadata (possibly large file)
meta_src = var_call_kBJwSBBocp6L8SrP1sAyhTsP
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_PmMdZUeMgaRMQWkWr3RTjDHo

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join
df = meta_df.merge(arts_df, on='article_id', how='inner')

# Category classification (Business)
business_kw = [
    'stock','stocks','shares','bond','bonds','market','markets','wall st','wall street','dow','nasdaq','s&p',
    'earnings','profit','revenue','sales','forecast','outlook','guidance','ipo','merger','acquisition','buyout',
    'carlyle','private equity','hedge fund','bank','banks','banking','loan','credit','debt','mortgage',
    'economy','economic','inflation','gdp','jobs','unemployment','interest rate','rates','fed','ecb',
    'oil','crude','gas','energy','opec','gold','currency','dollar','euro','yen','forex',
    'trade','tariff','export','imports','deficit','surplus','company','companies','corporate','ceo','cfo',
    'finance','financial','investment','investor','business','industry','manufacturing','retail'
]

def is_business(text):
    if not isinstance(text, str):
        return False
    t = text.lower()
    return any(k in t for k in business_kw)

combined = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['is_business'] = combined.map(is_business)

# Year extraction
# publication_date format YYYY-MM-DD
# ensure string
pub = df['publication_date'].astype(str)
df['year'] = pub.str.slice(0,4).astype(int)

# Filter 2010-2020 (already) and business
dfb = df[(df['year']>=2010) & (df['year']<=2020) & (df['is_business'])]

counts = dfb.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg = float(counts.mean())

out = {
    'average_business_articles_per_year_europe_2010_2020': avg,
    'total_business_articles': int(counts.sum()),
    'years': 11,
    'per_year_counts': {str(k): int(v) for k,v in counts.to_dict().items()}
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_kBJwSBBocp6L8SrP1sAyhTsP': 'file_storage/call_kBJwSBBocp6L8SrP1sAyhTsP.json', 'var_call_PmMdZUeMgaRMQWkWr3RTjDHo': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
