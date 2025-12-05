code = """import json
symbols = var_call_xky7XV6Mh9BqKKsjryf803ke
# build DuckDB SQL to compute, for each symbol, count of 2019 days with (High-Low)/Low>0.2
queries = []
for sym in symbols:
    q = f"SELECT '{sym}' AS Symbol, SUM(CASE WHEN Low>0 AND (High-Low)/Low>0.2 THEN 1 ELSE 0 END) AS cnt FROM '{sym}' WHERE Date >= '2019-01-01' AND Date <= '2019-12-31'"
    queries.append(q)
union_query = " UNION ALL ".join(queries)
full_query = f"SELECT Symbol, cnt FROM ({union_query}) ORDER BY cnt DESC LIMIT 5;"
result = json.dumps(full_query)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_6uWNcvecadNQoXv3keG6BKGM': 'file_storage/call_6uWNcvecadNQoXv3keG6BKGM.json', 'var_call_rzpzxI2Qytpp3tEwylwogsDJ': 'file_storage/call_rzpzxI2Qytpp3tEwylwogsDJ.json', 'var_call_xky7XV6Mh9BqKKsjryf803ke': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
