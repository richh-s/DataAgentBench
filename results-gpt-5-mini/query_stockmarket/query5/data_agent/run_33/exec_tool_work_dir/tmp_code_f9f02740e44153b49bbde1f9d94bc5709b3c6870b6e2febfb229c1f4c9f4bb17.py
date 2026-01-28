code = """import json
symbols = var_call_kn6t5PiaGlKEsUdc2Tg9wxFw
# Build SQL with UNION ALL
parts = []
for s in symbols:
    part = f"SELECT '{s}' AS symbol, SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * \"Low\" AND \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' THEN 1 ELSE 0 END) AS cnt FROM \"{s}\""
    parts.append(part)
sql = " UNION ALL ".join(parts)
sql = sql + " ORDER BY cnt DESC LIMIT 5;"
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_rfyYtktMLhimR4IA6eLZMmWU': 'file_storage/call_rfyYtktMLhimR4IA6eLZMmWU.json', 'var_call_WZvVJbgIU7sze4ErwQGAeoXY': 'file_storage/call_WZvVJbgIU7sze4ErwQGAeoXY.json', 'var_call_kn6t5PiaGlKEsUdc2Tg9wxFw': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
