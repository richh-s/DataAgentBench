code = """import json
# Load the stockinfo query result and the list of tables in stocktrade_database
with open(var_call_ulODgnzxdmB7bWwddmb5TRy0, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_KWNLUv7QwTFzxckaFGtF9TlS, 'r') as f:
    tables = json.load(f)

# Build mapping of symbols to company descriptions for Market Category S
mapping = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}

# Intersect with available tables in stocktrade_database
available_symbols = sorted([s for s in mapping.keys() if s in tables])

if not available_symbols:
    result = {'sql': '', 'mapping': mapping, 'symbols': []}
else:
    # Build UNION ALL query to count days in 2019 where (High - Low) > 0.2 * Low
    parts = []
    for s in available_symbols:
        part = f"SELECT '{s}' AS symbol, SUM(CASE WHEN Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\" THEN 1 ELSE 0 END) AS cnt FROM \"{s}\""
        parts.append(part)
    union = "\nUNION ALL\n".join(parts)
    sql = f"WITH counts AS (\n{union}\n)\nSELECT symbol, cnt FROM counts ORDER BY cnt DESC LIMIT 5;"
    result = {'sql': sql, 'mapping': mapping, 'symbols': available_symbols}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ulODgnzxdmB7bWwddmb5TRy0': 'file_storage/call_ulODgnzxdmB7bWwddmb5TRy0.json', 'var_call_KWNLUv7QwTFzxckaFGtF9TlS': 'file_storage/call_KWNLUv7QwTFzxckaFGtF9TlS.json'}

exec(code, env_args)
