code = """import json, pandas as pd

# Load Europe articles metadata (may be file path)
meta = var_call_X21HwToj0VEgvuwTqyQkE3Cf
if isinstance(meta, str):
    with open(meta, 'r') as f:
        meta = json.load(f)
meta_df = pd.DataFrame(meta)
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['year'] = pd.to_datetime(meta_df['publication_date']).dt.year

# Load articles (may be file path or list)
arts = var_call_I8WOXFhG9R0xHH1Bxw60FMCL
if isinstance(arts, str):
    with open(arts, 'r') as f:
        arts = json.load(f)
arts_df = pd.DataFrame(arts)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# Join to get text for Europe+years range
joined = meta_df.merge(arts_df, on='article_id', how='inner')
joined['text'] = (joined['title'].fillna('') + ' ' + joined['description'].fillna('')).str.lower()

# Simple keyword-based Business classifier
biz_keywords = [
    'stock','stocks','share','shares','equity','nasdaq','dow','s&p','sp500','ftse','dax','cac',
    'market','markets','invest','investment','investor','hedge fund','private equity','ipo','bond','bonds','yield',
    'economy','economic','gdp','inflation','deflation','recession','jobs','unemployment','payroll',
    'profit','profits','earnings','revenue','sales','guidance','forecast','quarter','q1','q2','q3','q4',
    'bank','banks','banking','central bank','ecb','boe','fed','interest rate','rates','loan','credit','mortgage',
    'oil','crude','brent','wti','gas','energy prices','commodity','commodities','gold','copper','wheat',
    'company','companies','corp','corporate','merger','acquisition','takeover','buyout','ceo','cfo',
    'trade','exports','import','tariff','sanction','currency','euro','dollar','yen','pound',
    'retail','consumer','price','prices'
]

def is_business(txt: str) -> bool:
    return any(k in txt for k in biz_keywords)

joined['is_business'] = joined['text'].map(is_business)

biz = joined[joined['is_business']].copy()
counts = biz.groupby('year')['article_id'].nunique()
# ensure all years 2010-2020 present
all_years = pd.Index(range(2010, 2021), name='year')
counts = counts.reindex(all_years, fill_value=0)
avg_per_year = float(counts.mean())

out = {
    'average_business_articles_per_year_europe_2010_2020': avg_per_year,
    'total_business_articles_2010_2020': int(counts.sum()),
    'years': {int(y): int(v) for y, v in counts.items()}
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_X21HwToj0VEgvuwTqyQkE3Cf': 'file_storage/call_X21HwToj0VEgvuwTqyQkE3Cf.json', 'var_call_I8WOXFhG9R0xHH1Bxw60FMCL': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
