code = """import json
symbols = var_call_208OlUwD7jPPXElo7Ct6sMzq
# Build and execute union query in the DuckDB database stocktrade_database
# We'll chunk to avoid extremely long SQL; do 50 per chunk
chunks = [symbols[i:i+50] for i in range(0, len(symbols), 50)]
queries = []
for chunk in chunks:
    parts = []
    for s in chunk:
        parts.append(f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' AND ((\"High\" - \"Low\") > 0.2 * \"Low\")")
    full = ' UNION ALL '.join(parts)
    q = 'SELECT Symbol, cnt FROM (' + full + ') ORDER BY cnt DESC;'
    queries.append(q)
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_VqxF3xG5XGRmxZHnEI5CHGMJ': 'file_storage/call_VqxF3xG5XGRmxZHnEI5CHGMJ.json', 'var_call_sOBRWuxkOyvJlDzcPXen5MsU': 'file_storage/call_sOBRWuxkOyvJlDzcPXen5MsU.json', 'var_call_5cuTBpqGleEMyWZK9EI5Ao9X': 'file_storage/call_5cuTBpqGleEMyWZK9EI5Ao9X.json', 'var_call_koNAOQ6bHLQBEVitand5U4Nq': 'file_storage/call_koNAOQ6bHLQBEVitand5U4Nq.json', 'var_call_khp7mwRGOdbD9fpbPSxRZyC8': {'num_symbols': 86, 'symbols_preview': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}, 'var_call_A6GCDbrDppSYIQlcsLEZjo2e': 'file_storage/call_A6GCDbrDppSYIQlcsLEZjo2e.json', 'var_call_wFHBgjnyvyVAJRd4Bh8udLrA': [], 'var_call_208OlUwD7jPPXElo7Ct6sMzq': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
