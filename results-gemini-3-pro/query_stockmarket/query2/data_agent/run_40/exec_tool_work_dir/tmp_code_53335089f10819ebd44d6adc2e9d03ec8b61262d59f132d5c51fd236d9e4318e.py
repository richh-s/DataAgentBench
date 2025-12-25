code = """import json

# Load ETFs
with open(locals()['var_function-call-8651100051121965824'], 'r') as f:
    etf_data = json.load(f)
etf_symbols = [item['Symbol'] for item in etf_data]

# Load Tables
with open(locals()['var_function-call-10552792860447953947'], 'r') as f:
    tables = json.load(f)

# Find intersection
valid_etfs = sorted(list(set(etf_symbols).intersection(set(tables))))

# Create chunks
chunk_size = 300
chunks = [valid_etfs[i:i + chunk_size] for i in range(0, len(valid_etfs), chunk_size)]

queries = []
for chunk in chunks:
    parts = []
    for sym in chunk:
        part = "SELECT '" + sym + "' as Symbol FROM \"" + sym + "\" WHERE \"Adj Close\" > 200 AND Date >= '2015-01-01' AND Date <= '2015-12-31' LIMIT 1"
        parts.append(part)
    full_query = " UNION ALL ".join(parts)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-8651100051121965824': 'file_storage/function-call-8651100051121965824.json', 'var_function-call-10552792860447953947': 'file_storage/function-call-10552792860447953947.json', 'var_function-call-4775747613018573872': {'count': 1435, 'first_50': ['LQDH', 'FLMB', 'IQIN', 'SLX', 'JPSE', 'VIDI', 'ULVM', 'EWP', 'EWM', 'JOYY', 'GII', 'DIV', 'AFK', 'FLIY', 'EMQQ', 'XMHQ', 'USTB', 'EFAX', 'IWP', 'EUSA', 'CNXT', 'VIXY', 'GSJY', 'EWZ', 'LCR', 'TFLO', 'IBDL', 'PFFD', 'IG', 'ZJPN', 'FXG', 'JHMS', 'GEM', 'ZHOK', 'AAAU', 'LRGF', 'SSPY', 'EWY', 'DMRS', 'PULS', 'AOK', 'SPHQ', 'MMIT', 'EMNT', 'EUMV', 'REET', 'VPL', 'SRVR', 'SLV', 'SGDJ']}}

exec(code, env_args)
