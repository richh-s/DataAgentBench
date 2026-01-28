code = """import json

tickers = var_call_4IhY958XFUiXD0QnoVk2cc2d['tickers']
values_rows = ','.join(["('"+t.replace("'","''")+"')" for t in tickers])

# Use DuckDB's query_table function to access by name dynamically.
sql = (
"WITH tickers(ticker) AS (SELECT * FROM (VALUES " + values_rows + "))\n"
"SELECT t.ticker,\n"
"       (SELECT COUNT(*)\n"
"        FROM query_table(t.ticker)\n"
"        WHERE CAST(Date AS DATE) BETWEEN DATE '2019-01-01' AND DATE '2019-12-31'\n"
"          AND Low IS NOT NULL AND Low <> 0 AND High IS NOT NULL\n"
"          AND (High - Low) / Low > 0.20\n"
"       ) AS days\n"
"FROM tickers t\n"
"ORDER BY days DESC, ticker ASC\n"
"LIMIT 5;"
)

print('__RESULT__:')
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_xUmnKzx0Unz6nHN1uFwG0Ltg': 'file_storage/call_xUmnKzx0Unz6nHN1uFwG0Ltg.json', 'var_call_4IhY958XFUiXD0QnoVk2cc2d': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'quoted_list_sql': '"AGMH","ALACU","AMHC","ANDA","APEX","BCLI","BHAT","BIOC","BKYI","BLFS","BOSC","BOTJ","BWEN","CBAT","CCCL","CDMOP","CEMI","CFBK","CFFA","CLRB","CORV","CPAAU","CPAH","CUBA","CVV","DZSI","ELSE","EXPC","EYEG","FAMI","FNCB","FSBW","FTFT","GDYN","GLG","GRNVU","GTEC","HCCOU","HNNA","HQI","HRTX","IDEX","IGIC","IOTS","ISNS","ITI","LACQ","MBCN","MBNKP","MCEP","MLND","MMAC","MNCLU","MNPR","NVEE","NXTD","OPOF","OPTT","ORGO","ORSNU","OTEL","PBFS","PBTS","PCSB","PECK","PEIX","PFIE","PLIN","POPE","QRHC","SES","SHSP","SNSS","SSNT","STKS","TGLS","TMSR","VERB","VMD","VRRM","VTIQW","VVPR","WHLM","WHLR","XBIOW","XPEL"', 'n': 86}, 'var_call_brt4ZecGG7J6lk0MawINLItU': [{'ticker': 'AGMH'}]}

exec(code, env_args)
