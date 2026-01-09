code = """import json, pandas as pd

# Workaround: build query using json.dumps to avoid escaping issues
path_syms = var_call_amLl3egspmPXOWcjN0p7lmdH
with open(path_syms,'r') as f:
    syms_recs = json.load(f)
df_syms = pd.DataFrame(syms_recs)

path_tbls = var_call_Pzw9xCiY0v3DYHEYXC9fs1W7
with open(path_tbls,'r') as f:
    tbls = json.load(f)
avail = set(r['table_name'] for r in tbls)

symbols = sorted(df_syms[df_syms['Symbol'].isin(avail)]['Symbol'].unique().tolist())

parts = []
for s in symbols:
    parts.append("SELECT '{s}' AS Symbol, COUNT(*) AS n_days FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low IS NOT NULL AND Low > 0 AND High IS NOT NULL AND (High - Low) / Low > 0.20".replace('{s}', s))
query = " UNION ALL ".join(parts)

print('__RESULT__:')
print(json.dumps({'n_symbols_with_tables': len(symbols), 'query': query}))"""

env_args = {'var_call_amLl3egspmPXOWcjN0p7lmdH': 'file_storage/call_amLl3egspmPXOWcjN0p7lmdH.json', 'var_call_Nuhe7u8qifzrmspz1p76Lmzh': {'n_symbols': 86, 'chunk_size': 200, 'n_chunks': 1, 'chunks': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']]}, 'var_call_Pzw9xCiY0v3DYHEYXC9fs1W7': 'file_storage/call_Pzw9xCiY0v3DYHEYXC9fs1W7.json'}

exec(code, env_args)
