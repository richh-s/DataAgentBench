code = """import json, pandas as pd

def load_result(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

meta = load_result(var_call_nt8aZTO7rFgh5ZVrxAjrceEd)
arts = load_result(var_call_bzmm4lCPx2PbVulZ8BV4Frol)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

meta_df['year'] = pd.to_datetime(meta_df['publication_date'], errors='coerce').dt.year
meta_df = meta_df[(meta_df['year']>=2010) & (meta_df['year']<=2020)]

# simple keyword-based classifier for Business
business_kw = [
    'stock','stocks','wall st','wall street','market','markets','shares','share',
    'bond','bonds','treasury','yield','yields','nasdaq','dow','s&p',
    'profit','profits','earnings','revenue','sales','ipo',
    'oil','crude','gas','energy','opec',
    'bank','banks','banking','fed','ecb','interest rate','rates','inflation',
    'economy','economic','gdp','trade','tariff','currency','dollar','euro','yen','forex',
    'company','companies','corporate','merger','acquisition','deal','ceo','cfo',
    'invest','investment','investor','fund','hedge','private equity','venture',
    'unemployment','jobs','employment','housing','real estate'
]

def is_business(title, desc):
    t = ((title or '') + ' ' + (desc or '')).lower()
    return any(k in t for k in business_kw)

arts_df['is_business'] = [is_business(t, d) for t, d in zip(arts_df.get('title'), arts_df.get('description'))]

merged = meta_df.merge(arts_df[['article_id','is_business']], on='article_id', how='inner')
biz = merged[merged['is_business']]

counts = biz.groupby('year')['article_id'].nunique()
# include all years 2010-2020 inclusive
all_years = pd.Index(range(2010,2021), name='year')
counts = counts.reindex(all_years, fill_value=0)

avg_per_year = float(counts.mean())

result = {
    'average_business_articles_per_year_europe_2010_2020': avg_per_year,
    'total_business_articles_2010_2020': int(counts.sum()),
    'years_counted': int(len(counts))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_nt8aZTO7rFgh5ZVrxAjrceEd': 'file_storage/call_nt8aZTO7rFgh5ZVrxAjrceEd.json', 'var_call_bzmm4lCPx2PbVulZ8BV4Frol': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
