code = """import json

tickers = var_call_4IhY958XFUiXD0QnoVk2cc2d['tickers']
values_rows = ','.join(["('"+t.replace("'","''")+"')" for t in tickers])

lines = [
    "WITH tickers(ticker) AS (SELECT * FROM (VALUES " + values_rows + "))",
    "SELECT t.ticker,",
    "       (SELECT COUNT(*)",
    "        FROM query_table(t.ticker)",
    "        WHERE CAST(Date AS DATE) BETWEEN DATE '2019-01-01' AND DATE '2019-12-31'",
    "          AND Low IS NOT NULL AND Low <> 0 AND High IS NOT NULL",
    "          AND (High - Low) / Low > 0.20",
    "       ) AS days",
    "FROM tickers t",
    "ORDER BY days DESC, ticker ASC",
    "LIMIT 5;",
]

sql = "\n".join(lines)
print('__RESULT__:')
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_xUmnKzx0Unz6nHN1uFwG0Ltg': 'file_storage/call_xUmnKzx0Unz6nHN1uFwG0Ltg.json', 'var_call_4IhY958XFUiXD0QnoVk2cc2d': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'quoted_list_sql': '"AGMH","ALACU","AMHC","ANDA","APEX","BCLI","BHAT","BIOC","BKYI","BLFS","BOSC","BOTJ","BWEN","CBAT","CCCL","CDMOP","CEMI","CFBK","CFFA","CLRB","CORV","CPAAU","CPAH","CUBA","CVV","DZSI","ELSE","EXPC","EYEG","FAMI","FNCB","FSBW","FTFT","GDYN","GLG","GRNVU","GTEC","HCCOU","HNNA","HQI","HRTX","IDEX","IGIC","IOTS","ISNS","ITI","LACQ","MBCN","MBNKP","MCEP","MLND","MMAC","MNCLU","MNPR","NVEE","NXTD","OPOF","OPTT","ORGO","ORSNU","OTEL","PBFS","PBTS","PCSB","PECK","PEIX","PFIE","PLIN","POPE","QRHC","SES","SHSP","SNSS","SSNT","STKS","TGLS","TMSR","VERB","VMD","VRRM","VTIQW","VVPR","WHLM","WHLR","XBIOW","XPEL"', 'n': 86}, 'var_call_brt4ZecGG7J6lk0MawINLItU': [{'ticker': 'AGMH'}]}

exec(code, env_args)
