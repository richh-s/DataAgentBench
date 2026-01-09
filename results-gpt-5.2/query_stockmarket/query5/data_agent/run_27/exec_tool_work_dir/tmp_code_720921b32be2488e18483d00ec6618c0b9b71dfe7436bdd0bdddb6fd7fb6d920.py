code = """import json
symbols = var_call_rlwDd8ulTEwLmC8ih2zCyUyM['symbols']
chunks = [symbols[i:i+25] for i in range(0, len(symbols), 25)]
chunk_queries = []
for chunk in chunks:
    parts = []
    for sym in chunk:
        parts.append("SELECT '{0}' AS Symbol, COUNT(*) AS n_days FROM \"{0}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2".format(sym))
    sql = " UNION ALL ".join(parts)
    chunk_queries.append(sql)
print('__RESULT__:')
print(json.dumps(chunk_queries))"""

env_args = {'var_call_H1EzipIeXpIxlsCS4XeHhHeF': 'file_storage/call_H1EzipIeXpIxlsCS4XeHhHeF.json', 'var_call_QvNSzJv7DaVr49HT6l7W4OSF': 'file_storage/call_QvNSzJv7DaVr49HT6l7W4OSF.json', 'var_call_rlwDd8ulTEwLmC8ih2zCyUyM': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n_symbols': 86}, 'var_call_m7CZvSXbDh3NARzsC3b1whfO': [{'Symbol': 'AGMH', 'n_days': '13'}], 'var_call_BRXXbSA45huMx6g9JyPPkCtJ': [{'Symbol': 'AGMH', 'n_days': '13'}, {'Symbol': 'ALACU', 'n_days': '0'}], 'var_call_mSytEkpuBBY7FZfpLUkNm6ea': 'ok'}

exec(code, env_args)
