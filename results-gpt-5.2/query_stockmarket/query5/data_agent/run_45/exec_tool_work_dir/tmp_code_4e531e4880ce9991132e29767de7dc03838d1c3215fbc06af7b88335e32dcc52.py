code = """import json, pandas as pd

# load symbols and company names (capital market)
path_syms = var_call_amLl3egspmPXOWcjN0p7lmdH
with open(path_syms,'r') as f:
    syms_recs = json.load(f)
df_syms = pd.DataFrame(syms_recs)

# load available trade tables
path_tbls = var_call_Pzw9xCiY0v3DYHEYXC9fs1W7
with open(path_tbls,'r') as f:
    tbls = json.load(f)
avail = set([r['table_name'] for r in tbls])

# intersect
df_syms['has_table'] = df_syms['Symbol'].isin(avail)
keep = df_syms[df_syms['has_table']].copy()
symbols = sorted(keep['Symbol'].unique().tolist())

# build union all query for 2019 with condition and count
parts = []
for s in symbols:
    # quote table name
    parts.append(f"SELECT '{s}' AS Symbol, COUNT(*) AS n_days\nFROM \"{s}\"\nWHERE Date >= '2019-01-01' AND Date < '2020-01-01'\n  AND Low IS NOT NULL AND Low > 0\n  AND High IS NOT NULL\n  AND (High - Low) / Low > 0.20")

query = "\nUNION ALL\n".join(parts)

out = {
    'n_symbols_with_tables': len(symbols),
    'query': query
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_amLl3egspmPXOWcjN0p7lmdH': 'file_storage/call_amLl3egspmPXOWcjN0p7lmdH.json', 'var_call_Nuhe7u8qifzrmspz1p76Lmzh': {'n_symbols': 86, 'chunk_size': 200, 'n_chunks': 1, 'chunks': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']]}, 'var_call_Pzw9xCiY0v3DYHEYXC9fs1W7': 'file_storage/call_Pzw9xCiY0v3DYHEYXC9fs1W7.json'}

exec(code, env_args)
