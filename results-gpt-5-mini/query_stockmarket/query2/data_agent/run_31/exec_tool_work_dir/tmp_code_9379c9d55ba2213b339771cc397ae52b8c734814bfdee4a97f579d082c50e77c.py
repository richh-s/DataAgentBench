code = """import json
# var_call_nkeAYvg53uExQmoxgksjf11P and var_call_IVsTNURPyVMjtErO88g5xAxA are available from previous tool calls
stockinfo_records = None
stocktrade_tables = None
# Load from storage variables
try:
    stockinfo_records = __import__('json').load(open(var_call_nkeAYvg53uExQmoxgksjf11P))
except Exception:
    stockinfo_records = var_call_nkeAYvg53uExQmoxgksjf11P
try:
    stocktrade_tables = __import__('json').load(open(var_call_IVsTNURPyVMjtErO88g5xAxA))
except Exception:
    stocktrade_tables = var_call_IVsTNURPyVMjtErO88g5xAxA

# extract symbols from stockinfo_records
symbols = [r['Symbol'] for r in stockinfo_records]
# intersection with stocktrade_tables
tables_set = set(stocktrade_tables)
symbols_in_trade = [s for s in symbols if s in tables_set]

# Build SQL query with UNION ALL of SELECTs checking Adj Close > 200 in 2015
selects = []
for s in symbols_in_trade:
    # escape double quotes in symbol if any (shouldn't be)
    tbl = s.replace('"', '""')
    sel = f'SELECT "{s}" AS Symbol FROM "{tbl}" WHERE "Date" >= \'2015-01-01\' AND "Date" <= \'2015-12-31\' AND "Adj Close" > 200 LIMIT 1'
    selects.append(sel)

if not selects:
    sql = "SELECT '' AS Symbol WHERE 1=0;"
else:
    sql = '\nUNION ALL\n'.join(selects) + ';'

print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_nkeAYvg53uExQmoxgksjf11P': 'file_storage/call_nkeAYvg53uExQmoxgksjf11P.json', 'var_call_IVsTNURPyVMjtErO88g5xAxA': 'file_storage/call_IVsTNURPyVMjtErO88g5xAxA.json'}

exec(code, env_args)
