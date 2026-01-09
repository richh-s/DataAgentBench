code = """import json, pandas as pd, re

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

meta = load_records(var_call_2KJxM3mxhAzhCx0dl4YdVscg)
arts = load_records(var_call_PS02YJzI4PBxVhVZ5ivDjDhj)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

df = meta_df.merge(arts_df, on='article_id', how='inner')

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

biz_kw = [
    'stock','stocks','wall st','wall street','dow','nasdaq','s&p','share','shares','equity','equities',
    'bond','bonds','treasury','yield','yields','interest rate','fed','ecb','central bank',
    'profit','profits','earnings','revenue','sales','forecast','guidance','quarter',
    'ipo','merger','acquisition','buyout','bank','banks','banking','loan','loans','credit',
    'market','markets','economy','economic','inflation','gdp','recession','currency','dollar','euro',
    'oil','crude','gold','commodity','commodities','trade','tariff','exports','import',
    'company','companies','corp','corporation','ceo','cfo','invest','investment','investor','fund','funds'
]

pattern = r'(' + '|'.join([re.escape(k) for k in biz_kw]) + r')'
is_business = text.str.contains(pattern, regex=True)

biz_df = df[is_business].copy()
biz_df['year'] = pd.to_datetime(biz_df['publication_date'], errors='coerce').dt.year
biz_df = biz_df[(biz_df['year']>=2010) & (biz_df['year']<=2020)]

counts = biz_df.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

out = {
    'avg_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles_2010_2020': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_2KJxM3mxhAzhCx0dl4YdVscg': 'file_storage/call_2KJxM3mxhAzhCx0dl4YdVscg.json', 'var_call_PS02YJzI4PBxVhVZ5ivDjDhj': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
