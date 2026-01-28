code = """import json
symbols = json.load(open(var_call_h8yS9HOG4cLI010qfpi0ZWHS))
selects = []
for s in symbols:
    tbl = s.replace('"', '""')
    sel = f'SELECT "{s}" AS Symbol FROM "{tbl}" WHERE "Date" >= \'2015-01-01\' AND "Date" <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1'
    selects.append(sel)

if selects:
    sql = '\nUNION ALL\n'.join(selects) + ';'
else:
    sql = "SELECT '' AS Symbol WHERE 1=0;"

print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_nkeAYvg53uExQmoxgksjf11P': 'file_storage/call_nkeAYvg53uExQmoxgksjf11P.json', 'var_call_IVsTNURPyVMjtErO88g5xAxA': 'file_storage/call_IVsTNURPyVMjtErO88g5xAxA.json', 'var_call_h8yS9HOG4cLI010qfpi0ZWHS': 'file_storage/call_h8yS9HOG4cLI010qfpi0ZWHS.json'}

exec(code, env_args)
