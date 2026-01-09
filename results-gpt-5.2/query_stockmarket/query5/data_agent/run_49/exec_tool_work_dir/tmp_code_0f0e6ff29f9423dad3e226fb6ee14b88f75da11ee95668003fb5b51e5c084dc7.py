code = """import json

tickers = var_call_4IhY958XFUiXD0QnoVk2cc2d['tickers']

parts=[]
for t in tickers:
    t_sql = t.replace("'","''")
    t_ident = t.replace('"','""')
    parts.append(f"SELECT '{t_sql}' AS ticker, COUNT(*) AS days FROM main.\"{t_ident}\" WHERE CAST(Date AS DATE) BETWEEN DATE '2019-01-01' AND DATE '2019-12-31' AND Low IS NOT NULL AND Low <> 0 AND High IS NOT NULL AND (High - Low)/Low > 0.20")

sql = " UNION ALL ".join(parts) + " ORDER BY days DESC, ticker ASC LIMIT 5;"
print('__RESULT__:')
print(json.dumps({'sql': sql}))"""

env_args = {'var_call_xUmnKzx0Unz6nHN1uFwG0Ltg': 'file_storage/call_xUmnKzx0Unz6nHN1uFwG0Ltg.json', 'var_call_4IhY958XFUiXD0QnoVk2cc2d': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'quoted_list_sql': '"AGMH","ALACU","AMHC","ANDA","APEX","BCLI","BHAT","BIOC","BKYI","BLFS","BOSC","BOTJ","BWEN","CBAT","CCCL","CDMOP","CEMI","CFBK","CFFA","CLRB","CORV","CPAAU","CPAH","CUBA","CVV","DZSI","ELSE","EXPC","EYEG","FAMI","FNCB","FSBW","FTFT","GDYN","GLG","GRNVU","GTEC","HCCOU","HNNA","HQI","HRTX","IDEX","IGIC","IOTS","ISNS","ITI","LACQ","MBCN","MBNKP","MCEP","MLND","MMAC","MNCLU","MNPR","NVEE","NXTD","OPOF","OPTT","ORGO","ORSNU","OTEL","PBFS","PBTS","PCSB","PECK","PEIX","PFIE","PLIN","POPE","QRHC","SES","SHSP","SNSS","SSNT","STKS","TGLS","TMSR","VERB","VMD","VRRM","VTIQW","VVPR","WHLM","WHLR","XBIOW","XPEL"', 'n': 86}, 'var_call_brt4ZecGG7J6lk0MawINLItU': [{'ticker': 'AGMH'}], 'var_call_Xy5YA0r24klyzXq1t6CgBKur': [{'test': 'ok'}], 'var_call_801Xwl9ETPtO1ixutZmvNTUo': [{'n': '2753'}], 'var_call_Gd183LHWpnHjkRlb6ib2RSnY': [{'table_name': 'AGMH'}], 'var_call_qKSaQJYY9cDUp81a7MBUJhSZ': [{'days': '13'}], 'var_call_2HOWTlkbkS12aFvXRrq4O0aI': 'file_storage/call_2HOWTlkbkS12aFvXRrq4O0aI.json', 'var_call_mgE0sdEJdVBTmUd47nKUZINn': {'sql': "SELECT 'AGMH' AS ticker, COUNT(*) AS days FROM main. + t_ident +  WHERE CAST(Date AS DATE) BETWEEN DATE '2019-01-01' AND DATE '2019-12-31' AND Low IS NOT NULL AND Low <> 0 AND High IS NOT NULL AND (High - Low)/Low > 0.20 UNION ALL SELECT 'ALACU' AS ticker, COUNT(*) AS days FROM main. + t_ident +  WHERE CAST(Date AS DATE) BETWEEN DATE '2019-01-01' AND DATE '2019-12-31' AND Low IS NOT NULL AND Low <> 0 AND High IS NOT NULL AND (High - Low)/Low > 0.20 UNION ALL SELECT 'AMHC' AS ticker, COUNT(*) AS ", 'total_len': 19899}, 'var_call_aQI7MVRKHGgFlAYBDJHB3LZX': [{'table_name': 'AGMH'}, {'table_name': 'ALACU'}, {'table_name': 'AMHC'}, {'table_name': 'ANDA'}, {'table_name': 'APEX'}], 'var_call_IU5MaCVgQvLei8qUsKOAKhHi': [{'ticker': 'AGMH', 'days': '13'}, {'ticker': 'ALACU', 'days': '0'}]}

exec(code, env_args)
