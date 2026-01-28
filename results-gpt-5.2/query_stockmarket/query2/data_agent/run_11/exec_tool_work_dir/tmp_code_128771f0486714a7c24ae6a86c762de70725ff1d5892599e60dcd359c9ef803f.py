code = """import json
import pandas as pd

# Load NYSE Arca ETFs
path = var_call_nOWlEQHUrbqOHXmVXSYbHeRt
with open(path,'r') as f:
    etfs = json.load(f)

df = pd.DataFrame(etfs)
# tickers to test: present in stocktrade_database tables list too
# We'll also load tables list
p2 = var_call_7z5eVmmDQejMlywaWhpIlzRp
# if it's a path, load it
if isinstance(p2, str):
    with open(p2,'r') as f:
        tables = json.load(f)
else:
    tables = p2

tables_set = set(tables)
df = df[df['Symbol'].isin(tables_set)].copy()

# output first 50 tickers list to use in subsequent SQL queries
tickers = df['Symbol'].tolist()[:50]
print('__RESULT__:')
print(json.dumps({'n_common': int(df.shape[0]), 'sample_50': tickers}))"""

env_args = {'var_call_qJiDwOwNX2pGcodn9dgo9XsI': ['stockinfo'], 'var_call_nOWlEQHUrbqOHXmVXSYbHeRt': 'file_storage/call_nOWlEQHUrbqOHXmVXSYbHeRt.json', 'var_call_7z5eVmmDQejMlywaWhpIlzRp': 'file_storage/call_7z5eVmmDQejMlywaWhpIlzRp.json', 'var_call_dn1SREokdWU5iEWahEGze1Dk': [{'name': 'AAAU'}], 'var_call_zHRHYg4x8sp4xS2rmb6nx51u': [{'max_adj': 'nan'}], 'var_call_CXknQMbvUdsPBFxTwE4Xf8UA': 'import json\npath = var_call_nOWlEQHUrbqOHXmVXSYbHeRt\nwith open(path,\'r\') as f:\n    etfs = json.load(f)\n\nqueries=[]\nfor r in etfs:\n    t=r[\'Symbol\']\n    if \'"\' in t:\n        continue\n    queries.append("SELECT \'{}\' AS symbol, MAX("Adj Close") AS max_adj_close_2015 FROM "{}" WHERE "Date" >= \'2015-01-01\' AND "Date" < \'2016-01-01\'".format(t,t))\n\nunion_sql=\' UNION ALL \'.join(queries)\nprint(union_sql[:200])\n', 'var_call_W5lpHdi4qC8qHLW3bkLOqxeA': '2015-01-01', 'var_call_Cyw8gopz72PT7iVCu1X72wI8': 'abc', 'var_call_DAqTWKIwKGZ5rLnkePt7pCRd': "WHERE d >= '2015-01-01'", 'var_call_Od417twrXebLg5JYQzCQcrgE': 'MAX(Adj Close)', 'var_call_2doHSKqTEdQJLK8JDPNqSzCO': [{'cid': '0', 'name': 'Date', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'Open', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'High', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'Low', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'Close', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Adj Close', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Volume', 'type': 'BIGINT', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_call_Dd3LhlEoEE0LAQaHbP8cbHHs': [{'max_adj': 'nan'}], 'var_call_l4p6baGCTsykFmSjGCI894fH': [{'c': '0'}], 'var_call_rbUG4cS9sDJDPmbQKRRjz28E': [{'min_d': '2018-08-15', 'max_d': '2020-04-01', 'c': '410'}], 'var_call_iXbdBrVhlktkaXIYq9nLJ5fa': [{'min_d': '1993-01-29', 'max_d': '2020-04-01', 'c': '6843'}], 'var_call_yhSkgj7VMw7V2lLvE62JFoJJ': [{'max_adj': '193.3121490478516'}], 'var_call_6JGFBQg89jUVLsrsSPMRFiUk': [{'Symbol': 'SPY', 'company_description': 'The SPDR S&P 500 is an exchange-traded fund that aims to provide investment results corresponding to the performance of the S&P 500 Index, offering investors a way to gain broad exposure to the U.S. stock market.'}]}

exec(code, env_args)
