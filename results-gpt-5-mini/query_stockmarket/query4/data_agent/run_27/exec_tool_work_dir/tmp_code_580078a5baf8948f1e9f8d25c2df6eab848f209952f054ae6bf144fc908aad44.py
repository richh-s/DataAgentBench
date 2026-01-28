code = """import json
# read matched stockinfo results (symbols for NYSE non-ETF available in trade DB)
with open(var_call_3CdQj3Q6YQ8u0U19WMxZbALc, 'r') as f:
    matched = json.load(f)
symbols = [r['Symbol'] for r in matched]

parts = []
for s in symbols:
    # safe table identifier
    tbl = s.replace('"', '""')
    part = (
        "SELECT '{sym}' AS symbol, "
        "SUM(CASE WHEN \"Close\">\"Open\" THEN 1 ELSE 0 END) AS up_days, "
        "SUM(CASE WHEN \"Close\"<\"Open\" THEN 1 ELSE 0 END) AS down_days "
        "FROM \"{tbl}\" WHERE \"Date\">='2017-01-01' AND \"Date\"<='2017-12-31'"
    ).format(sym=s, tbl=tbl)
    parts.append(part)

union_sql = " UNION ALL ".join(parts)
final_sql = "SELECT symbol, up_days, down_days FROM ({}) WHERE up_days>down_days ORDER BY up_days DESC LIMIT 5;".format(union_sql)

print('__RESULT__:')
print(json.dumps(final_sql))"""

env_args = {'var_call_JgVdZ5lPpvNbcr53P85FVhko': 'file_storage/call_JgVdZ5lPpvNbcr53P85FVhko.json', 'var_call_pg5PrTVxGV9a7THHNxzy7odL': 'file_storage/call_pg5PrTVxGV9a7THHNxzy7odL.json', 'var_call_3CdQj3Q6YQ8u0U19WMxZbALc': 'file_storage/call_3CdQj3Q6YQ8u0U19WMxZbALc.json', 'var_call_QV8UTH7arKnVHjxz3ksLPxOA': {'count': 234, 'symbols_sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA']}}

exec(code, env_args)
