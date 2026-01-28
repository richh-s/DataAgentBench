code = """import json
# Load the previous tool results from files whose paths are in the provided variables
with open(var_call_gS4FSnUcnhKgrZzAmEzsMtuc, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_Ddl9uDLtMJpf1r6JrUODvNuK, 'r') as f:
    trade_tables = json.load(f)

# Build set of NYSE non-ETF symbols from stockinfo (stockinfo query already filtered Listing Exchange = 'N' and ETF != 'Y')
symbols = [rec['Symbol'] for rec in stockinfo]
symbol_set = set(symbols)

# Intersect with available trade tables
available = [t for t in trade_tables if t in symbol_set]

# For safety, sort available symbols
available_sorted = sorted(available)

# Build SQL union of per-table aggregates for 2017
selects = []
for sym in available_sorted:
    # Quote table name with double quotes to be safe
    sel = (
        f"SELECT '{sym}' AS symbol, "
        "SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_count, "
        "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_count "
        f"FROM \"{sym}\" WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'"
    )
    selects.append(sel)

union_sql = '\nUNION ALL\n'.join(selects)
final_sql = (
    "SELECT symbol, up_count, down_count FROM (\n" + union_sql + "\n)\n"
    "WHERE up_count > down_count\n"
    "ORDER BY up_count DESC\n"
    "LIMIT 5;"
)

# Build mapping symbol->company description
mapping = {rec['Symbol']: rec.get('Company Description','') for rec in stockinfo}

out = {'sql': final_sql, 'mapping': mapping, 'available_count': len(available_sorted)}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_gS4FSnUcnhKgrZzAmEzsMtuc': 'file_storage/call_gS4FSnUcnhKgrZzAmEzsMtuc.json', 'var_call_Ddl9uDLtMJpf1r6JrUODvNuK': 'file_storage/call_Ddl9uDLtMJpf1r6JrUODvNuK.json'}

exec(code, env_args)
