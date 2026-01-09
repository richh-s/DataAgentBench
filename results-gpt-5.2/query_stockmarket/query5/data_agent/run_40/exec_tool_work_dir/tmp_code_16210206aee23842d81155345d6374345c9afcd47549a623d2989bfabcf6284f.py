code = """import json
from pathlib import Path

avail = var_call_qcc6IesNwNJRYnCqY1KZqXpl['available']

sql = "WITH counts AS (\n"
for i, sym in enumerate(avail):
    part = f"SELECT '{sym}' AS Symbol, SUM(CASE WHEN Low>0 AND (High-Low)/Low > 0.2 THEN 1 ELSE 0 END) AS days_gt20pct FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01'"
    if i>0:
        sql += "UNION ALL\n"
    sql += part + "\n"
sql += ") SELECT * FROM counts ORDER BY days_gt20pct DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_Zn1ziHBgt0lm454JT5C7GiNT': 'file_storage/call_Zn1ziHBgt0lm454JT5C7GiNT.json', 'var_call_FYEjIjKBttbGajFqd6mFIEyR': 'file_storage/call_FYEjIjKBttbGajFqd6mFIEyR.json', 'var_call_TacH1SzeiloqaPHt8X1kJMhw': 'file_storage/call_TacH1SzeiloqaPHt8X1kJMhw.json', 'var_call_qcc6IesNwNJRYnCqY1KZqXpl': {'available': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'missing': [], 'n_available': 86, 'n_missing': 0}, 'var_call_ZdUjJu4T4c2onF5YsXlz9rTD': [{'Symbol': 'AGMH', 'days_gt20pct': '13.0'}]}

exec(code, env_args)
