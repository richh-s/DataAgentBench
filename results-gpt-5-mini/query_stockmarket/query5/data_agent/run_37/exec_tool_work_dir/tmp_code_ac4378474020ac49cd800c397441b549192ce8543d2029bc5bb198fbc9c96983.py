code = """import json
with open(var_call_VqxF3xG5XGRmxZHnEI5CHGMJ, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_sOBRWuxkOyvJlDzcPXen5MsU, 'r') as f:
    trade_tables = json.load(f)

symbol_to_company = {rec['Symbol'].upper(): rec.get('Company Description','') for rec in stockinfo}
trade_set = set([t.upper() for t in trade_tables])
symbols = sorted([s for s in symbol_to_company.keys() if s in trade_set])

queries = []
for s in symbols:
    q = f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' AND ((\"High\" - \"Low\") > 0.2 * \"Low\")"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'symbols': symbols, 'queries': queries}))"""

env_args = {'var_call_VqxF3xG5XGRmxZHnEI5CHGMJ': 'file_storage/call_VqxF3xG5XGRmxZHnEI5CHGMJ.json', 'var_call_sOBRWuxkOyvJlDzcPXen5MsU': 'file_storage/call_sOBRWuxkOyvJlDzcPXen5MsU.json', 'var_call_5cuTBpqGleEMyWZK9EI5Ao9X': 'file_storage/call_5cuTBpqGleEMyWZK9EI5Ao9X.json', 'var_call_koNAOQ6bHLQBEVitand5U4Nq': 'file_storage/call_koNAOQ6bHLQBEVitand5U4Nq.json', 'var_call_khp7mwRGOdbD9fpbPSxRZyC8': {'num_symbols': 86, 'symbols_preview': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}, 'var_call_A6GCDbrDppSYIQlcsLEZjo2e': 'file_storage/call_A6GCDbrDppSYIQlcsLEZjo2e.json', 'var_call_wFHBgjnyvyVAJRd4Bh8udLrA': []}

exec(code, env_args)
