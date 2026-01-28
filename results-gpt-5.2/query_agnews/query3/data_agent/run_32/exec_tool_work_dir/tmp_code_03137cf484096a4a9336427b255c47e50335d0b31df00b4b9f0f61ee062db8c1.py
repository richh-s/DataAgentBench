code = """import json, pandas as pd

meta = var_call_P4Dyr0LdUwfGj1WyTfV4NAX8
arts = var_call_IMqsfW2ifWRzCnNUAEoaaSiD

# load meta from file if needed
if isinstance(meta, str):
    with open(meta, 'r', encoding='utf-8') as f:
        meta = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

# basic business classifier using keyword matching on title+description
business_kw = [
    'stock','stocks','wall st','wall street','dow','nasdaq','s&p','share','shares','equity','equities',
    'bond','bonds','treasury','yield','yields','rate','rates','interest','inflation','economy','economic',
    'gdp','market','markets','trading','trade','exports','import','imports','currency','currencies','dollar',
    'euro','yen','profit','profits','earnings','revenue','sales','quarter','q1','q2','q3','q4',
    'company','companies','firm','investment','investor','bank','banks','finance','financial','ipo','merger',
    'acquisition','oil','crude','opec','gas','energy','prices','price','jobs','unemployment','manufacturing',
    'retail','real estate','housing','aerospace','commercial'
]

def is_business(row):
    text = f"{row.get('title','')} {row.get('description','')}".lower()
    return any(k in text for k in business_kw)

arts_df['is_business'] = arts_df.apply(is_business, axis=1)

# join Europe 2010-2020 with articles content
df = meta_df.merge(arts_df[['article_id','is_business']], on='article_id', how='inner')

# extract year
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year
# keep only years 2010-2020 just in case
df = df[(df['year']>=2010) & (df['year']<=2020) & (df['is_business'])]

counts = df.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_P4Dyr0LdUwfGj1WyTfV4NAX8': 'file_storage/call_P4Dyr0LdUwfGj1WyTfV4NAX8.json', 'var_call_IMqsfW2ifWRzCnNUAEoaaSiD': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
