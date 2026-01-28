code = """import json
symbols = var_call_RMWFFIuAO9KY40ynDKwwz33N
# Build union SQL
parts = []
for s in symbols:
    # Table names may need quoting
    part = f"SELECT '{s}' AS Symbol, SUM(CASE WHEN \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\" THEN 1 ELSE 0 END) AS cnt FROM \"{s}\""
    parts.append(part)
sql = "SELECT Symbol, cnt FROM (\n" + "\nUNION ALL\n".join(parts) + "\n) t ORDER BY cnt DESC LIMIT 5;"
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_CXV6AFYuhWf4cZ3SzcFw0jYo': 'file_storage/call_CXV6AFYuhWf4cZ3SzcFw0jYo.json', 'var_call_tXOtpY1HEpiyPlku0M5AGz86': 'file_storage/call_tXOtpY1HEpiyPlku0M5AGz86.json', 'var_call_RMWFFIuAO9KY40ynDKwwz33N': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
