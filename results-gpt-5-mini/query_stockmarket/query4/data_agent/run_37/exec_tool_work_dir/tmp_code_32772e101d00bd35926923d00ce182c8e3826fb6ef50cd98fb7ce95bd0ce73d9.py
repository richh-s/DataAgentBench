code = """import json
with open(var_call_gS4FSnUcnhKgrZzAmEzsMtuc, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_Ddl9uDLtMJpf1r6JrUODvNuK, 'r') as f:
    trade_tables = json.load(f)

symbols = [rec['Symbol'] for rec in stockinfo]
symbol_set = set(symbols)
available = [t for t in trade_tables if t in symbol_set]
available_sorted = sorted(available)

selects = []
for sym in available_sorted:
    sel = f'''SELECT '{sym}' AS symbol, 
SUM(CASE WHEN "Close">"Open" THEN 1 ELSE 0 END) AS up_count, 
SUM(CASE WHEN "Close"<"Open" THEN 1 ELSE 0 END) AS down_count 
FROM "{sym}" WHERE "Date">='2017-01-01' AND "Date"<='2017-12-31' '''
    selects.append(sel)

union_sql = '\nUNION ALL\n'.join(selects)
final_sql = (
    "SELECT symbol, up_count, down_count FROM (\n" + union_sql + "\n)\n"
    "WHERE up_count > down_count\n"
    "ORDER BY up_count DESC\n"
    "LIMIT 5;"
)

mapping = {rec['Symbol']: rec.get('Company Description','') for rec in stockinfo}
out = {'sql': final_sql, 'mapping': mapping, 'available_count': len(available_sorted)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_gS4FSnUcnhKgrZzAmEzsMtuc': 'file_storage/call_gS4FSnUcnhKgrZzAmEzsMtuc.json', 'var_call_Ddl9uDLtMJpf1r6JrUODvNuK': 'file_storage/call_Ddl9uDLtMJpf1r6JrUODvNuK.json'}

exec(code, env_args)
