code = """import json
# Load the stored results from previous tool calls
with open(var_call_zS6ooOlqOTROyoR6BVuOpZjd, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_VE63NDAtYBpaiHZ8oLi7Rhez, 'r') as f:
    tables = json.load(f)
# Build mapping of symbols to company description for Market Category 'S' (already filtered by query)
companies = {rec['Symbol']: rec['Company Description'] for rec in stockinfo}
# Filter to those that have a table in the stocktrade_database
tables_set = set(tables)
intersection = [s for s in companies.keys() if s in tables_set]
# Build the UNION ALL SQL across all intersection symbols
parts = []
for sym in intersection:
    part = "SELECT '{sym}' AS symbol, SUM(CASE WHEN Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\" THEN 1 ELSE 0 END) AS cnt FROM \"{sym}\"".format(sym=sym)
    parts.append(part)
union_sql = '\nUNION ALL\n'.join(parts)
final_sql = f"SELECT symbol, cnt FROM (\n{union_sql}\n) ORDER BY cnt DESC LIMIT 100;"
# Prepare companies subset mapping
companies_subset = {s: companies[s] for s in intersection}
output = {'sql': final_sql, 'companies': companies_subset}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_zS6ooOlqOTROyoR6BVuOpZjd': 'file_storage/call_zS6ooOlqOTROyoR6BVuOpZjd.json', 'var_call_VE63NDAtYBpaiHZ8oLi7Rhez': 'file_storage/call_VE63NDAtYBpaiHZ8oLi7Rhez.json'}

exec(code, env_args)
