code = """import json
stocks_path = var_call_cmY1EYc6USuwalwuipiyYYv3
with open(stocks_path) as f:
    stocks = json.load(f)

symbol_to_name = {s['Symbol']: s['Company Description'] for s in stocks}

results = var_call_UHWKktQWnXguQYLHmBVgcFp4

# take top 5 symbols
top5 = results[:5]
output = []
for r in top5:
    sym = r['Symbol']
    desc = symbol_to_name.get(sym, '')
    name = desc.split(' specializes')[0].split(' is ')[0].split(' operates')[0].split(' provides')[0]
    output.append({'Symbol': sym, 'CompanyName': name.strip(), 'Days': int(r['cnt'])})

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_cmY1EYc6USuwalwuipiyYYv3': 'file_storage/call_cmY1EYc6USuwalwuipiyYYv3.json', 'var_call_TDVsp11drIRDNtzkNNjX1In5': 'file_storage/call_TDVsp11drIRDNtzkNNjX1In5.json', 'var_call_qpOwjhPPK9vuUS54EKKa9X1V': 'file_storage/call_qpOwjhPPK9vuUS54EKKa9X1V.json', 'var_call_dhkr3Bb0tw1xn8GyytSbIYRV': 'file_storage/call_dhkr3Bb0tw1xn8GyytSbIYRV.json', 'var_call_UHWKktQWnXguQYLHmBVgcFp4': [{'Symbol': 'GLG', 'cnt': '42'}, {'Symbol': 'FAMI', 'cnt': '23'}, {'Symbol': 'CBAT', 'cnt': '23'}, {'Symbol': 'FTFT', 'cnt': '21'}, {'Symbol': 'BIOC', 'cnt': '21'}, {'Symbol': 'PECK', 'cnt': '19'}, {'Symbol': 'EYEG', 'cnt': '18'}, {'Symbol': 'BKYI', 'cnt': '16'}, {'Symbol': 'CPAH', 'cnt': '16'}, {'Symbol': 'NXTD', 'cnt': '15'}, {'Symbol': 'ORGO', 'cnt': '15'}, {'Symbol': 'IDEX', 'cnt': '15'}, {'Symbol': 'APEX', 'cnt': '15'}, {'Symbol': 'MCEP', 'cnt': '14'}, {'Symbol': 'CLRB', 'cnt': '14'}, {'Symbol': 'AGMH', 'cnt': '13'}, {'Symbol': 'CCCL', 'cnt': '13'}, {'Symbol': 'PEIX', 'cnt': '12'}, {'Symbol': 'OPTT', 'cnt': '12'}, {'Symbol': 'CORV', 'cnt': '10'}]}

exec(code, env_args)
