code = """import json
p = var_call_tKBSUm17HZWAwsEaWyIyu4b5
with open(p,'r') as f:
    obj=json.load(f)
symbols=obj['symbols']

parts=[]
for sym in symbols:
    parts.append('SELECT \'' + sym + '\' AS Symbol FROM "' + sym + '" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1')

query = '\nUNION ALL\n'.join(parts) + ';'

out=json.dumps({"query": query, "symbol_count": len(symbols)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_zjYjRfp8wuGsrjishFwvDIsi': 'file_storage/call_zjYjRfp8wuGsrjishFwvDIsi.json', 'var_call_z2cyof62djNmQtjHxGguLbb9': 'file_storage/call_z2cyof62djNmQtjHxGguLbb9.json', 'var_call_tKBSUm17HZWAwsEaWyIyu4b5': 'file_storage/call_tKBSUm17HZWAwsEaWyIyu4b5.json'}

exec(code, env_args)
