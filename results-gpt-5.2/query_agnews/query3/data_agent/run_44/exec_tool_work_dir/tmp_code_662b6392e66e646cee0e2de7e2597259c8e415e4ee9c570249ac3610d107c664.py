code = """import json, pandas as pd

# Load metadata (Europe, 2010-2020)
meta_src = var_call_7qFaWBptMxsSiaIa6ebPq2Bc
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

# Load articles
arts = var_call_Fn1fC2kxkuDyrtqn8ts4JNtg

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize ids
meta_df['article_id'] = pd.to_numeric(meta_df['article_id'], errors='coerce')
arts_df['article_id'] = pd.to_numeric(arts_df['article_id'], errors='coerce')

# Merge and classify
df = meta_df.merge(arts_df, on='article_id', how='inner')

def is_business(text: str) -> bool:
    if text is None:
        return False
    t = str(text).lower()
    keywords = [
        'market','stocks','stock','shares','wall st','wall street','dow','nasdaq','s&p',
        'earnings','revenue','profit','loss','ipo','bond','bonds','yield','inflation','gdp',
        'economy','economic','trade','tariff','exports','imports','oil','crude','currency',
        'euro','dollar','pound','yen','bank','banks','central bank','ecb','fed','interest rate',
        'rate hike','rate cut','unemployment','jobs','company','companies','merger','acquisition',
        'takeover','deal','finance','financial','investor','investment','fund','hedge',
        'retail','sales','consumer','manufacturing','industry','business'
    ]
    return any(k in t for k in keywords)

combined = (df['title'].fillna('') + ' ' + df['description'].fillna(''))
df['is_business'] = combined.apply(is_business)

# Year and counts
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year
bus = df[df['is_business'] & df['year'].between(2010, 2020)]
counts = bus.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = float(counts.mean())

result = {
    'average_business_articles_per_year_europe_2010_2020': avg_per_year,
    'total_business_articles': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7qFaWBptMxsSiaIa6ebPq2Bc': 'file_storage/call_7qFaWBptMxsSiaIa6ebPq2Bc.json', 'var_call_Fn1fC2kxkuDyrtqn8ts4JNtg': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
