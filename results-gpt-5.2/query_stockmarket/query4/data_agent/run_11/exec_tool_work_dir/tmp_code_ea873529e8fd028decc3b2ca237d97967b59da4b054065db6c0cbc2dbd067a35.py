code = """import json
src = var_call_tBV3GJDNoaydc95nVxMZLmQP
if isinstance(src, str):
    with open(src,'r') as f:
        data=json.load(f)
else:
    data=src
symbols=data['symbols']
company_map=data['company_map']

lines=[]
lines.append('symbol,company_name,up_days,down_days')
for s in symbols:
    comp = company_map.get(s,'').replace('"','""')
    lines.append(f'{s},"{comp}",,')

out='\n'.join(lines[:6])
# just output first few lines as placeholder
print('__RESULT__:')
print(json.dumps({'preview': out, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_Ccu3gVLBYmt6aODTNoRLYShv': 'file_storage/call_Ccu3gVLBYmt6aODTNoRLYShv.json', 'var_call_Vuu3fiiPc3q8j0Wv61fKeY8b': 'file_storage/call_Vuu3fiiPc3q8j0Wv61fKeY8b.json', 'var_call_tBV3GJDNoaydc95nVxMZLmQP': 'file_storage/call_tBV3GJDNoaydc95nVxMZLmQP.json'}

exec(code, env_args)
