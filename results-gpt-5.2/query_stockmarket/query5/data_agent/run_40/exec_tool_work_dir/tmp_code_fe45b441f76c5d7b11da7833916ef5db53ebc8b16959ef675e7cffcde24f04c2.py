code = """import json, math

avail = var_call_qcc6IesNwNJRYnCqY1KZqXpl['available']

# build list of per-symbol SQL queries
queries = []
for sym in avail:
    queries.append(
        "SELECT '{sym}' AS Symbol, SUM(CASE WHEN Low>0 AND (High-Low)/Low > 0.2 THEN 1 ELSE 0 END) AS days_gt20pct FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01';".format(sym=sym)
    )

print('__RESULT__:')
print(json.dumps({'n': len(queries), 'first': queries[0], 'last': queries[-1]}))"""

env_args = {'var_call_Zn1ziHBgt0lm454JT5C7GiNT': 'file_storage/call_Zn1ziHBgt0lm454JT5C7GiNT.json', 'var_call_FYEjIjKBttbGajFqd6mFIEyR': 'file_storage/call_FYEjIjKBttbGajFqd6mFIEyR.json', 'var_call_TacH1SzeiloqaPHt8X1kJMhw': 'file_storage/call_TacH1SzeiloqaPHt8X1kJMhw.json', 'var_call_qcc6IesNwNJRYnCqY1KZqXpl': {'available': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'missing': [], 'n_available': 86, 'n_missing': 0}, 'var_call_ZdUjJu4T4c2onF5YsXlz9rTD': [{'Symbol': 'AGMH', 'days_gt20pct': '13.0'}], 'var_call_jay3UrDFVagtJcj8dYFNDsRZ': [{'Symbol': 'AGMH', 'days_gt20pct': '13.0'}], 'var_call_fslGUed2xRDmFmG4PqmMN6Mc': [{'Symbol': 'ALACU', 'days_gt20pct': '0.0'}], 'var_call_Bxetd5OMzmwCWlRBFyjQi2B1': [{'Symbol': 'AMHC', 'days_gt20pct': 'nan'}], 'var_call_EoTzqztzoseWtPFFWYvm0n5g': [{'Symbol': 'ANDA', 'days_gt20pct': '0.0'}], 'var_call_Ko18NHkNAfzDr3lbu8yyVq5t': [{'Symbol': 'APEX', 'days_gt20pct': '15.0'}]}

exec(code, env_args)
