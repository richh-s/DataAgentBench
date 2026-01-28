code = """import json
# load the intersection list
path = var_call_WlSU9xZpPyQ0i1kfOeTn8eHa
with open(path, 'r') as f:
    symbols = json.load(f)
# build SQL query: for each symbol generate SELECT 'SYM' as symbol, MAX("Adj Close") as max_adj FROM "SYM" WHERE "Date">='2015-01-01' AND "Date"<='2015-12-31'
parts = []
for sym in symbols:
    # wrap symbol in double quotes for DuckDB (table names)
    part = f'SELECT "{sym}" AS symbol, MAX("Adj Close") AS max_adj FROM "{sym}" WHERE "Date">=\'2015-01-01\' AND "Date"<=\'2015-12-31\''
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts) + ';'
# print result as JSON string
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_GMErwPiZAV8ACBIMFcLWeylx': 'file_storage/call_GMErwPiZAV8ACBIMFcLWeylx.json', 'var_call_7wxjtS5eDBAybdsY4hHUlbkg': 'file_storage/call_7wxjtS5eDBAybdsY4hHUlbkg.json', 'var_call_7LTpHrqwyFIkW2SUcmkW6iZJ': 'file_storage/call_7LTpHrqwyFIkW2SUcmkW6iZJ.json', 'var_call_WlSU9xZpPyQ0i1kfOeTn8eHa': 'file_storage/call_WlSU9xZpPyQ0i1kfOeTn8eHa.json', 'var_call_fCNdc4cBAlyrpTi223ltHHdk': [], 'var_call_nT4QnccOIHbS3BwOdkS2wTCX': [], 'var_call_5vow5bsU9fsILCThGdBNMQSg': [], 'var_call_lbhLK335ayIqyehGNZJ9oapl': [{'max_adj': '193.3121490478516'}]}

exec(code, env_args)
