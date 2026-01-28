code = """import json
# Load the previous tool results from files
with open(var_call_VqxF3xG5XGRmxZHnEI5CHGMJ, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_sOBRWuxkOyvJlDzcPXen5MsU, 'r') as f:
    trade_tables = json.load(f)

# Build mapping from symbol to company description for Market Category 'S' (already filtered by earlier query)
symbol_to_company = {rec['Symbol'].upper(): rec.get('Company Description','') for rec in stockinfo}

# Compute intersection with available trade tables
trade_set = set([t.upper() for t in trade_tables])
symbols = sorted([s for s in symbol_to_company.keys() if s in trade_set])

# Build union SQL to count days in 2019 where (High - Low) > 0.2 * Low for each symbol
parts = []
for s in symbols:
    part = f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM \"{s}\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' AND ((\"High\" - \"Low\") > 0.2 * \"Low\")"
    parts.append(part)

if not parts:
    result = {'sql': '', 'symbol_to_company': symbol_to_company, 'symbols': symbols}
else:
    union_all = ' UNION ALL '.join(parts)
    full_sql = f"SELECT Symbol, cnt FROM ({union_all}) ORDER BY cnt DESC LIMIT 5;"
    result = {'sql': full_sql, 'symbol_to_company': symbol_to_company, 'symbols': symbols}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VqxF3xG5XGRmxZHnEI5CHGMJ': 'file_storage/call_VqxF3xG5XGRmxZHnEI5CHGMJ.json', 'var_call_sOBRWuxkOyvJlDzcPXen5MsU': 'file_storage/call_sOBRWuxkOyvJlDzcPXen5MsU.json'}

exec(code, env_args)
