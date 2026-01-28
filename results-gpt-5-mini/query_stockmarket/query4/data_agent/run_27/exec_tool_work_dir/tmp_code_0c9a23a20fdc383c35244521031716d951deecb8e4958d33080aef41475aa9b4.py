code = """import json
with open(var_call_3CdQj3Q6YQ8u0U19WMxZbALc, 'r') as f:
    matched = json.load(f)
symbols = [r['Symbol'] for r in matched]
parts = []
for s in symbols:
    part = ("SELECT '{sym}' AS symbol, "
            "SUM(CASE WHEN \"Close\">\"Open\" AND \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31' THEN 1 ELSE 0 END) AS up_days, "
            "SUM(CASE WHEN \"Close\"<\"Open\" AND \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31' THEN 1 ELSE 0 END) AS down_days "
            "FROM \"{tbl}\" WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'").format(sym=s, tbl=s)
    parts.append(part)
union_sql = " UNION ALL ".join(parts)
final_sql = "SELECT symbol, up_days, down_days FROM ({}) WHERE up_days>down_days ORDER BY up_days DESC LIMIT 10;".format(union_sql)
print("__RESULT__:")
print(json.dumps(final_sql))"""

env_args = {'var_call_JgVdZ5lPpvNbcr53P85FVhko': 'file_storage/call_JgVdZ5lPpvNbcr53P85FVhko.json', 'var_call_pg5PrTVxGV9a7THHNxzy7odL': 'file_storage/call_pg5PrTVxGV9a7THHNxzy7odL.json', 'var_call_3CdQj3Q6YQ8u0U19WMxZbALc': 'file_storage/call_3CdQj3Q6YQ8u0U19WMxZbALc.json'}

exec(code, env_args)
