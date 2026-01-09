code = """import json, pandas as pd

# Load Europe article_ids 2010-2020
path = var_call_da7v5W5coIKblhDwi0OLnXML
with open(path, 'r') as f:
    europe_ids = set(int(r['article_id']) for r in json.load(f))

# Load all articles (titles/descriptions)
arts = pd.DataFrame(var_call_AAbvWDpyYJVGBmOtid09R4Xx)
arts['article_id'] = arts['article_id'].astype(int)
arts = arts[arts['article_id'].isin(europe_ids)].copy()
arts['text'] = (arts['title'].fillna('') + ' ' + arts['description'].fillna('')).str.lower()

# Heuristic classifier for Business
biz_terms = [
    'reuters -', 'wall st', 'stocks', 'stock', 'shares', 'market', 'earnings', 'profit', 'loss', 'revenue',
    'sales', 'quarter', 'fiscal', 'ipo', 'bond', 'bonds', 'yield', 'interest rate', 'fed', 'central bank',
    'inflation', 'gdp', 'economy', 'economic', 'oil', 'crude', 'gas', 'bank', 'banks', 'credit', 'loan',
    'mortgage', 'forex', 'currency', 'dollar', 'euro', 'yen', 'trade', 'export', 'import', 'tariff',
    'company', 'corp', 'inc', 'ltd', 'plc', 'merger', 'acquisition', 'deal', 'invest', 'investment',
    'fund', 'hedge', 'private equity', 'venture', 'startup', 'ceo', 'cfo', 'dividend'
]
pattern = '|'.join(pd.Series(biz_terms).map(lambda x: x.replace(' ', '\\s+')).tolist())
arts['is_business'] = arts['text'].str.contains(pattern, regex=True)

# Map business article_ids back to metadata to count per year
biz_ids = tuple(arts.loc[arts['is_business'], 'article_id'].astype(int).tolist())

# If none, return 0
if len(biz_ids)==0:
    avg = 0.0
else:
    # Query metadata for business ids with per-year counts
    # We'll compute from already available year counts by filtering ids? Need metadata rows.
    pass

# Pull metadata rows for europe 2010-2020 (article_id, year)
# Use the small aggregated counts? can't filter. We'll load via sqlite query not possible in python.
print('__RESULT__:')
print(json.dumps({'biz_count': int(arts['is_business'].sum()), 'total_europe_2010_2020': int(len(arts))}))"""

env_args = {'var_call_s1iTJNknIoDprKQsu4eeYjch': [{'year': '2010', 'cnt': '1306'}, {'year': '2011', 'cnt': '1316'}, {'year': '2012', 'cnt': '1355'}, {'year': '2013', 'cnt': '1354'}, {'year': '2014', 'cnt': '1372'}, {'year': '2015', 'cnt': '1357'}, {'year': '2016', 'cnt': '1364'}, {'year': '2017', 'cnt': '1391'}, {'year': '2018', 'cnt': '1351'}, {'year': '2019', 'cnt': '1328'}, {'year': '2020', 'cnt': '1366'}], 'var_call_da7v5W5coIKblhDwi0OLnXML': 'file_storage/call_da7v5W5coIKblhDwi0OLnXML.json', 'var_call_AAbvWDpyYJVGBmOtid09R4Xx': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
