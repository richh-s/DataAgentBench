code = """import json, pandas as pd
from pathlib import Path

info = pd.DataFrame(json.loads(Path(var_call_RsghL4UroeHSwUjPcoLqnafK).read_text()))
syms = info['Symbol'].dropna().unique().tolist()

queries = []
for s in syms:
    q = "\n".join([
        f"SELECT '{s}' AS Symbol, CAST(COUNT(*) AS BIGINT) AS days_over_20pct",
        f"FROM \"{s}\"",
        "WHERE \"Date\" >= '2019-01-01' AND \"Date\" < '2020-01-01'",
        "  AND \"Low\" IS NOT NULL AND \"Low\" > 0",
        "  AND (\"High\" - \"Low\") / \"Low\" > 0.2",
    ])
    queries.append(q)

union_query = "\nUNION ALL\n".join(queries)
final_query = "\n".join([
    "WITH counts AS (",
    union_query,
    ")",
    "SELECT Symbol, days_over_20pct FROM counts ORDER BY days_over_20pct DESC, Symbol ASC LIMIT 5;"
])

print('__RESULT__:')
print(json.dumps({'len': len(final_query), 'preview': final_query[:1200]}))"""

env_args = {'var_call_RsghL4UroeHSwUjPcoLqnafK': 'file_storage/call_RsghL4UroeHSwUjPcoLqnafK.json', 'var_call_cgAd9NGNcdGgSVnLuC0reEW1': {'n_symbols': 86, 'chunks': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']], 'n_chunks': 1}, 'var_call_hafkDQXR6rEtIs35wsOfOvpJ': 'file_storage/call_hafkDQXR6rEtIs35wsOfOvpJ.json', 'var_call_2IuPSKh2AsXgrQI0liq6Xn2q': {'valid_n': 86, 'missing_n': 0, 'valid': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'missing_preview': []}, 'var_call_z5DKeBOrSwX7hxhm2pTGIiZj': {'s': "SELECT 'T' AS Symbol"}}

exec(code, env_args)
