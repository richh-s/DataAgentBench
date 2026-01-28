code = """import json
with open(var_call_3CdQj3Q6YQ8u0U19WMxZbALc, 'r') as f:
    matched = json.load(f)
# extract symbols
symbols = [r['Symbol'] for r in matched]
# build union query parts, but limit to symbols that are valid table names in DuckDB. We assume all are valid.
parts = []
for s in symbols:
    part = f"SELECT '{s}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" AND \"Date\">=\'2017-01-01\' AND \"Date\"<=\'2017-12-31\' THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN \"Close\"<\"Open\" AND \"Date\">=\'2017-01-01\' AND \"Date\"<=\'2017-12-31\' THEN 1 ELSE 0 END) AS down_days FROM \"{s}\" WHERE \"Date\">=\'2017-01-01\' AND \"Date\"<=\'2017-12-31\'"
    parts.append(part)
union_sql = " UNION ALL ".join(parts)
final_sql = f"SELECT symbol, up_days, down_days FROM ({union_sql}) WHERE up_days>down_days ORDER BY up_days DESC LIMIT 10;"
# we request top 10 to ensure we have enough in case mapping names later.
print('__RESULT__:')
print(json.dumps(final_sql))"""

env_args = {'var_call_JgVdZ5lPpvNbcr53P85FVhko': 'file_storage/call_JgVdZ5lPpvNbcr53P85FVhko.json', 'var_call_pg5PrTVxGV9a7THHNxzy7odL': 'file_storage/call_pg5PrTVxGV9a7THHNxzy7odL.json', 'var_call_3CdQj3Q6YQ8u0U19WMxZbALc': 'file_storage/call_3CdQj3Q6YQ8u0U19WMxZbALc.json'}

exec(code, env_args)
