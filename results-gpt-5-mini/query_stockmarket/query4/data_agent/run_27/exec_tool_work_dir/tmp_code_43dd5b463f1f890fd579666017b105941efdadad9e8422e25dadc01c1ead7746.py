code = """import json
with open(var_call_3CdQj3Q6YQ8u0U19WMxZbALc, 'r') as f:
    matched = json.load(f)
symbols = [r['Symbol'] for r in matched][:200]
union_parts = []
for s in symbols:
    tbl = s.replace('"','""')
    sql = ("SELECT '{}' as symbol, "
           "SUM(CASE WHEN \"Close\">\"Open\" AND \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31' THEN 1 ELSE 0 END) as up_days, "
           "SUM(CASE WHEN \"Close\"<\"Open\" AND \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31' THEN 1 ELSE 0 END) as down_days "
           "FROM \"{}\" WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'").format(s,tbl)
    union_parts.append(sql)
final_sql = " UNION ALL ".join(union_parts)
final = "SELECT symbol, up_days, down_days FROM ({}) WHERE up_days>down_days ORDER BY up_days DESC LIMIT 10;".format(final_sql)
print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_JgVdZ5lPpvNbcr53P85FVhko': 'file_storage/call_JgVdZ5lPpvNbcr53P85FVhko.json', 'var_call_pg5PrTVxGV9a7THHNxzy7odL': 'file_storage/call_pg5PrTVxGV9a7THHNxzy7odL.json', 'var_call_3CdQj3Q6YQ8u0U19WMxZbALc': 'file_storage/call_3CdQj3Q6YQ8u0U19WMxZbALc.json'}

exec(code, env_args)
