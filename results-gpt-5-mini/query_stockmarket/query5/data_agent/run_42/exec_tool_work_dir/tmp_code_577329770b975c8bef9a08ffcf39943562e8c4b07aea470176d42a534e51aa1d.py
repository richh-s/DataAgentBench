code = """import json
# Access previous results
s_symbols = var_call_fcoDNKXYDJMAGzR7gydgtI9j
tables = var_call_VTyc75leeSMyszc5Bj5kuEds
# If tables is a file path, load it
if isinstance(tables, str):
    import os
    with open(tables, 'r') as f:
        tables = json.load(f)
# Ensure all uppercase
tables_set = set(tables)
# Compute intersection
symbols_to_query = [sym for sym in s_symbols if sym in tables_set]
# Build UNION ALL query pieces
pieces = []
for sym in symbols_to_query:
    # quote symbol with double quotes for DuckDB
    pieces.append(f"SELECT '{sym}' AS symbol, COUNT(*) AS cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low")
union_sql = "\nUNION ALL\n".join(pieces)
full_sql = f"SELECT symbol, cnt FROM (\n{union_sql}\n) ORDER BY cnt DESC LIMIT 5;"
# Output the SQL and the number of symbols
out = {"num_symbols": len(symbols_to_query), "sql": full_sql}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_8xCDs1LrHdq65SHNpZ4C4JAn': 'file_storage/call_8xCDs1LrHdq65SHNpZ4C4JAn.json', 'var_call_fcoDNKXYDJMAGzR7gydgtI9j': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_VTyc75leeSMyszc5Bj5kuEds': 'file_storage/call_VTyc75leeSMyszc5Bj5kuEds.json'}

exec(code, env_args)
