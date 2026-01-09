code = """import json, pandas as pd, re

# Load europe article-year rows
europe_rows = var_call_JSKsnAnBLkHDLFcGqPNfBcd3
if isinstance(europe_rows, str):
    with open(europe_rows, 'r', encoding='utf-8') as f:
        europe_rows = json.load(f)
europe = pd.DataFrame(europe_rows)
europe['article_id'] = europe['article_id'].astype(int)
europe['year'] = europe['year'].astype(int)

# Load articles
articles_data = var_call_ahMGW1fSqhh97AcLtMrQ0z2s
if isinstance(articles_data, str):
    with open(articles_data, 'r', encoding='utf-8') as f:
        articles_data = json.load(f)
articles = pd.DataFrame(articles_data)
articles['article_id'] = articles['article_id'].astype(int)
articles['title'] = articles['title'].fillna('')
articles['description'] = articles['description'].fillna('')
text = (articles['title'] + ' ' + articles['description']).str.lower()

biz_kw = [
    'stock','stocks','wall st','wall street','market','markets','shares','share','bond','bonds','treasury','nasdaq','dow','s&p',
    'earnings','profit','loss','revenue','sales','quarter','forecast','outlook','guidance',
    'company','companies','firm','bank','banks','banking','investment','investor','investors','fund','funds','hedge',
    'merger','acquisition','ipo','offering','buyout','deal',
    'oil','crude','gas','energy','prices','price','inflation','economy','economic','gdp','jobs','unemployment','rates','interest',
    'fed','central bank','ecb','imf','opec','currency','dollar','euro','yen','forex',
    'trade','tariff','export','import','manufacturing','retail','consumer','business'
]
pattern = re.compile(r'(' + '|'.join([re.escape(k) for k in biz_kw]) + r')')
articles['is_business'] = text.str.contains(pattern)

biz = articles.loc[articles['is_business'], ['article_id']].drop_duplicates()

merged = europe.merge(biz, on='article_id', how='inner')
counts = merged.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg = counts.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': float(avg),
    'yearly_counts': {str(k): int(v) for k,v in counts.items()},
    'total_business_articles': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uiFI4CxiHJdenRBBmvDRDVjM': [{'year': '2010', 'cnt': '1306'}, {'year': '2011', 'cnt': '1316'}, {'year': '2012', 'cnt': '1355'}, {'year': '2013', 'cnt': '1354'}, {'year': '2014', 'cnt': '1372'}, {'year': '2015', 'cnt': '1357'}, {'year': '2016', 'cnt': '1364'}, {'year': '2017', 'cnt': '1391'}, {'year': '2018', 'cnt': '1351'}, {'year': '2019', 'cnt': '1328'}, {'year': '2020', 'cnt': '1366'}], 'var_call_ahMGW1fSqhh97AcLtMrQ0z2s': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_JSKsnAnBLkHDLFcGqPNfBcd3': 'file_storage/call_JSKsnAnBLkHDLFcGqPNfBcd3.json', 'var_call_naOCgPnrYtLwXxRlVJ02JpLO': {'biz_ids_count': 5}}

exec(code, env_args)
