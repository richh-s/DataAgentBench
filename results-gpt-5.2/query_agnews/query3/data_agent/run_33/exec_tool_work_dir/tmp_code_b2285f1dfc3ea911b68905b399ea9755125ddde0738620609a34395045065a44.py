code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

meta = pd.DataFrame(load_records(var_call_E2SusgNF3SLjNkGdxFsb8UxB))
arts = pd.DataFrame(load_records(var_call_8fvLUa9UDHv0AvHE6wO0V8uh))

# Normalize types
arts['article_id'] = arts['article_id'].astype(int)
meta['year'] = meta['year'].astype(int)
meta['cnt'] = meta['cnt'].astype(int)

# Classify Business using keyword heuristic on title+description
text = (arts['title'].fillna('') + ' ' + arts['description'].fillna('')).str.lower()
# business signal terms
biz_terms = [
    'reuters -', 'earnings', 'stocks', 'stock', 'shares', 'wall st', 'wall street', 'nasdaq', 'dow',
    'ftse', 'dax', 'cac', 'market', 'markets', 'invest', 'investment', 'bank', 'banks', 'banking',
    'ipo', 'merger', 'acquisition', 'profit', 'revenue', 'sales', 'economy', 'economic', 'inflation',
    'oil', 'crude', 'opec', 'dollar', 'euro', 'yen', 'currency', 'forex', 'bond', 'bonds', 'yield',
    'fed', 'interest rate', 'central bank', 'gdp', 'trade', 'exports', 'imports', 'company', 'companies',
    'corporate', 'ceo', 'quarter', 'fiscal', 'startup', 'industry', 'business'
]
pattern = r'(' + '|'.join([pd.regex.escape(t) if hasattr(pd, 'regex') else t for t in biz_terms]) + r')'
# pandas doesn't have pd.regex.escape; use re
import re
pattern = r'(' + '|'.join([re.escape(t) for t in biz_terms]) + r')'
arts['is_business'] = text.str.contains(pattern, regex=True)

# Join with Europe 2010-2020 metadata
# Need article_metadata per article for Europe years; current meta is aggregated only. Re-query detailed.
print('__RESULT__:')
print(json.dumps({'need_detailed': True}))"""

env_args = {'var_call_E2SusgNF3SLjNkGdxFsb8UxB': [{'year': '2010', 'cnt': '1306'}, {'year': '2011', 'cnt': '1316'}, {'year': '2012', 'cnt': '1355'}, {'year': '2013', 'cnt': '1354'}, {'year': '2014', 'cnt': '1372'}, {'year': '2015', 'cnt': '1357'}, {'year': '2016', 'cnt': '1364'}, {'year': '2017', 'cnt': '1391'}, {'year': '2018', 'cnt': '1351'}, {'year': '2019', 'cnt': '1328'}, {'year': '2020', 'cnt': '1366'}], 'var_call_8fvLUa9UDHv0AvHE6wO0V8uh': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
