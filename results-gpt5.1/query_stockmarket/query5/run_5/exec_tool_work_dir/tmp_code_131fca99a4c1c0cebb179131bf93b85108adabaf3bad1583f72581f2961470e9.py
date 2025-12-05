code = """import json

with open(var_call_lNPGRwGHeTZgSqRHrqBEloGo, 'r') as f:
    stockinfo_records = json.load(f)

symbol_to_name = {r['Symbol']: r['Company Description'] for r in stockinfo_records}

result_rows = []
for row in var_call_nqS6RrzCflMP5InBfkK1DOP0:
    sym = row['Symbol']
    desc = symbol_to_name.get(sym, '')
    # Assume company name is the first sentence before the first period
    name = desc.split('.')[0].strip()
    result_rows.append({'Symbol': sym, 'Company Name': name})

out = json.dumps(result_rows)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_VuZPSbgDhdXLEOCyvdWeHMJE': 'file_storage/call_VuZPSbgDhdXLEOCyvdWeHMJE.json', 'var_call_lNPGRwGHeTZgSqRHrqBEloGo': 'file_storage/call_lNPGRwGHeTZgSqRHrqBEloGo.json', 'var_call_OKxgkwwEoIXHGVaRfxN0Gmmq': 'file_storage/call_OKxgkwwEoIXHGVaRfxN0Gmmq.json', 'var_call_nqS6RrzCflMP5InBfkK1DOP0': [{'Symbol': 'BIOC', 'cnt': '21'}, {'Symbol': 'BKYI', 'cnt': '16'}, {'Symbol': 'APEX', 'cnt': '15'}, {'Symbol': 'AGMH', 'cnt': '13'}, {'Symbol': 'BHAT', 'cnt': '10'}]}

exec(code, env_args)
