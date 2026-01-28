code = """import json, pandas as pd

# Load metadata counts per year (Europe, all categories)
year_counts = pd.DataFrame(var_call_uiFI4CxiHJdenRBBmvDRDVjM)
year_counts['year'] = year_counts['year'].astype(int)
year_counts['cnt'] = year_counts['cnt'].astype(int)

# Load articles (may be large; if stored as file path, read it)
articles_data = var_call_ahMGW1fSqhh97AcLtMrQ0z2s
if isinstance(articles_data, str):
    with open(articles_data, 'r', encoding='utf-8') as f:
        articles_data = json.load(f)
articles = pd.DataFrame(articles_data)
articles['article_id'] = articles['article_id'].astype(int)
articles['title'] = articles['title'].fillna('')
articles['description'] = articles['description'].fillna('')
text = (articles['title'] + ' ' + articles['description']).str.lower()

# Simple keyword-based classifier for Business
biz_kw = [
    'stock','stocks','wall st','wall street','market','markets','shares','share','bond','bonds','treasury','nasdaq','dow','s&p',
    'earnings','profit','loss','revenue','sales','quarter','q1','q2','q3','q4','forecast','outlook','guidance',
    'company','companies','firm','bank','banks','banking','investment','investor','investors','fund','funds','hedge',
    'merger','acquisition','ipo','offering','buyout','deal','contracts','contract',
    'oil','crude','gas','energy','prices','price','inflation','economy','economic','gdp','jobs','unemployment','rates','interest rate',
    'fed','central bank','ecb','boe','boj','imf','opec','currency','dollar','euro','yen','forex',
    'trade','tariff','export','imports','manufacturing','factory','retail','consumer','business'
]
pattern = r'(' + '|'.join([pd.re.escape(k) for k in biz_kw]) + r')'
articles['is_business'] = text.str.contains(pattern, regex=True)

biz_ids = set(articles.loc[articles['is_business'], 'article_id'].tolist())

# Need business counts among Europe 2010-2020: join by article_id with metadata filtered
# Query metadata for Europe 2010-2020 at article level? We'll approximate by distributing? No: do exact by pulling article_ids+year.

print('__RESULT__:')
print(json.dumps({'business_id_count': len(biz_ids)}))"""

env_args = {'var_call_uiFI4CxiHJdenRBBmvDRDVjM': [{'year': '2010', 'cnt': '1306'}, {'year': '2011', 'cnt': '1316'}, {'year': '2012', 'cnt': '1355'}, {'year': '2013', 'cnt': '1354'}, {'year': '2014', 'cnt': '1372'}, {'year': '2015', 'cnt': '1357'}, {'year': '2016', 'cnt': '1364'}, {'year': '2017', 'cnt': '1391'}, {'year': '2018', 'cnt': '1351'}, {'year': '2019', 'cnt': '1328'}, {'year': '2020', 'cnt': '1366'}], 'var_call_ahMGW1fSqhh97AcLtMrQ0z2s': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
