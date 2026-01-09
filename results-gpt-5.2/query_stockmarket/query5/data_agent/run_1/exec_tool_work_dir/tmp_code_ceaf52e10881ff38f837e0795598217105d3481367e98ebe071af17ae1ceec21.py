code = """import json
cand = json.loads(var_call_RoX66CPtmqtCfZ9Edn3f7c1z)['candidate_tickers']

queries = []
for t in cand:
    # quote identifier for duckdb
    q = f"SELECT '{t}' AS Symbol, COUNT(*)::BIGINT AS days_count FROM (SELECT Date, High, Low FROM \"{t}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low IS NOT NULL AND Low > 0 AND High IS NOT NULL AND (High - Low) / Low > 0.2) s;"
    queries.append(q)

union_query = "\nUNION ALL\n".join(queries) + "\nORDER BY days_count DESC, Symbol ASC\nLIMIT 5;"

print('__RESULT__:')
print(json.dumps({'sql': union_query}))"""

env_args = {'var_call_pDpILRLzxzoT5P1Kosgioq0m': 'file_storage/call_pDpILRLzxzoT5P1Kosgioq0m.json', 'var_call_MCUnaKaEKzfS0pL4YmqLF0EK': 'file_storage/call_MCUnaKaEKzfS0pL4YmqLF0EK.json', 'var_call_RoX66CPtmqtCfZ9Edn3f7c1z': {'candidate_tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}}

exec(code, env_args)
