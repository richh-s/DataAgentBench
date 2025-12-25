code = """import json

k1 = 'var_function-call-8651100051121965824'
k2 = 'var_function-call-10552792860447953947'
with open(locals()[k1], 'r') as f:
    etf_data = json.load(f)
etf_symbols = [item['Symbol'] for item in etf_data]

with open(locals()[k2], 'r') as f:
    tables = json.load(f)

valid_etfs = sorted(list(set(etf_symbols).intersection(set(tables))))

chunk_size = 120
chunks = [valid_etfs[i:i + chunk_size] for i in range(0, len(valid_etfs), chunk_size)]

queries = []
# Template: SELECT 'SYM' FROM "SYM" WHERE "Adj Close" > 200 AND Date LIKE '2015%' LIMIT 1
# Using chr(39) for single quote, chr(34) for double quote
sq = chr(39)
dq = chr(34)

for chunk in chunks:
    parts = []
    for sym in chunk:
        # SELECT 'SYM' FROM "SYM" WHERE "Adj Close" > 200 AND Date LIKE '2015%' LIMIT 1
        # Note: DuckDB might expect double quotes for identifiers, single for strings.
        # Date is string.
        part = "SELECT " + sq + sym + sq + " as S FROM " + dq + sym + dq + " WHERE " + dq + "Adj Close" + dq + " > 200 AND Date LIKE " + sq + "2015%" + sq + " LIMIT 1"
        parts.append(part)
    full_query = " UNION ALL ".join(parts)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps({"queries": queries, "next_index": 1, "total": len(queries)}))"""

env_args = {'var_function-call-8651100051121965824': 'file_storage/function-call-8651100051121965824.json', 'var_function-call-10552792860447953947': 'file_storage/function-call-10552792860447953947.json', 'var_function-call-4775747613018573872': {'count': 1435, 'first_50': ['LQDH', 'FLMB', 'IQIN', 'SLX', 'JPSE', 'VIDI', 'ULVM', 'EWP', 'EWM', 'JOYY', 'GII', 'DIV', 'AFK', 'FLIY', 'EMQQ', 'XMHQ', 'USTB', 'EFAX', 'IWP', 'EUSA', 'CNXT', 'VIXY', 'GSJY', 'EWZ', 'LCR', 'TFLO', 'IBDL', 'PFFD', 'IG', 'ZJPN', 'FXG', 'JHMS', 'GEM', 'ZHOK', 'AAAU', 'LRGF', 'SSPY', 'EWY', 'DMRS', 'PULS', 'AOK', 'SPHQ', 'MMIT', 'EMNT', 'EUMV', 'REET', 'VPL', 'SRVR', 'SLV', 'SGDJ']}, 'var_function-call-17688035904698170674': 'test', 'var_function-call-7127615406140404747': 5, 'var_function-call-17178494102391298034': 'file_storage/function-call-17178494102391298034.json'}

exec(code, env_args)
