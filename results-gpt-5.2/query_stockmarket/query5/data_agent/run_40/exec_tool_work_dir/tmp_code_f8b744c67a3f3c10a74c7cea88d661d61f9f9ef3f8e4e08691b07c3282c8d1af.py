code = """import json

avail = var_call_qcc6IesNwNJRYnCqY1KZqXpl['available']
parts = []
for sym in avail:
    parts.append(
        "SELECT '{sym}' AS Symbol, SUM(CASE WHEN Low>0 AND (High-Low)/Low > 0.2 THEN 1 ELSE 0 END) AS cnt "
        "FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01'".format(sym=sym)
    )
query = "\nUNION ALL\n".join(parts) + ";"

print('__RESULT__:')
print(json.dumps({'query': query, 'n_symbols': len(avail)}))"""

env_args = {'var_call_Zn1ziHBgt0lm454JT5C7GiNT': 'file_storage/call_Zn1ziHBgt0lm454JT5C7GiNT.json', 'var_call_FYEjIjKBttbGajFqd6mFIEyR': 'file_storage/call_FYEjIjKBttbGajFqd6mFIEyR.json', 'var_call_TacH1SzeiloqaPHt8X1kJMhw': 'file_storage/call_TacH1SzeiloqaPHt8X1kJMhw.json', 'var_call_qcc6IesNwNJRYnCqY1KZqXpl': {'available': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'missing': [], 'n_available': 86, 'n_missing': 0}}

exec(code, env_args)
