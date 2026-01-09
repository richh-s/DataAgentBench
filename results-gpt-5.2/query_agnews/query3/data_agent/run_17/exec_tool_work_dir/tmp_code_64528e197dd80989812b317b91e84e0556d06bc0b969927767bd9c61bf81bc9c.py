code = """import json, pandas as pd

# Load metadata (possibly large)
meta_src = var_call_WjrDOIRn1D600JZf03YSN64b
if isinstance(meta_src, str):
    with open(meta_src, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = meta_src

arts = var_call_lg1aMFAyJi5CrjeKWB3Gx8wh

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Simple keyword-based business classifier
business_keywords = [
    'stock','stocks','wall st','wall street','nasdaq','dow','s&p','bond','bonds','treasury','yield',
    'oil','crude','gas','opec','barrel','energy','inflation','gdp','economy','economic','recession',
    'market','markets','earnings','profit','loss','revenue','sales','quarter','forecast','outlook',
    'bank','banks','banking','central bank','fed','ecb','interest rate','rates','loan','credit',
    'currency','euro','dollar','yen','forex','exchange rate',
    'company','companies','firm','firms','ceo','cfo','ipo','acquisition','merger','buyout','private equity',
    'trade','tariff','exports','import','manufacturing','investment','investor','share','shares',
    'unemployment','jobs','retail','consumer'
]
kw = [k.lower() for k in business_keywords]

def is_business(text):
    if text is None:
        return False
    t = str(text).lower()
    return any(k in t for k in kw)

joined = meta_df.merge(arts_df, on='article_id', how='inner')
joined['text'] = (joined['title'].fillna('') + ' ' + joined['description'].fillna(''))
joined['is_business'] = joined['text'].map(is_business)

biz = joined[joined['is_business']].copy()
biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)

# counts per year 2010-2020 inclusive
years = list(range(2010, 2021))
counts = biz.groupby('year')['article_id'].nunique().reindex(years, fill_value=0)

avg_per_year = float(counts.mean())

result = {
    'average_business_articles_per_year_europe_2010_2020': avg_per_year,
    'total_business_articles_europe_2010_2020': int(counts.sum()),
    'years_counted': len(years)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_WjrDOIRn1D600JZf03YSN64b': 'file_storage/call_WjrDOIRn1D600JZf03YSN64b.json', 'var_call_lg1aMFAyJi5CrjeKWB3Gx8wh': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
