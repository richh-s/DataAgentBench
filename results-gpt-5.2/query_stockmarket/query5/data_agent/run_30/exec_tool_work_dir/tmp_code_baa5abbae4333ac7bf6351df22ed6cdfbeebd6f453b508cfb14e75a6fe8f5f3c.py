code = """import json
symbols = json.loads(var_call_nfU5s88ETHwBuqC2q8t1KQ3k)["symbols"]
parts = []
for t in symbols:
    parts.append(
        "SELECT '{sym}' AS Symbol, CAST(COUNT(*) AS BIGINT) AS days_cnt "
        "FROM \"{sym}\" "
        "WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        "AND Low IS NOT NULL AND Low > 0 AND High IS NOT NULL "
        "AND (High - Low) / Low > 0.2".format(sym=t)
    )
query = "\nUNION ALL\n".join(parts) + "\nORDER BY days_cnt DESC\nLIMIT 5;"
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_WEHmWuq38xwH8o3YmUPIUsUm': 'file_storage/call_WEHmWuq38xwH8o3YmUPIUsUm.json', 'var_call_YDYetXoUvp7hZkrB8iyZiWtm': 'file_storage/call_YDYetXoUvp7hZkrB8iyZiWtm.json', 'var_call_nfU5s88ETHwBuqC2q8t1KQ3k': {'n_symbols': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}}

exec(code, env_args)
