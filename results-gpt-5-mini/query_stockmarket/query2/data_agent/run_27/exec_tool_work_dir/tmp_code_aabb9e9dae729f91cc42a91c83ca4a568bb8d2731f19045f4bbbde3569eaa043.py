code = """import json
path = var_call_8UvW6KsMY3Sq7CHGXoSaQiC8
data = json.load(open(path, 'r'))
symbols = [rec['Symbol'] for rec in data]
parts = []
for s in symbols:
    part = ('SELECT * FROM (SELECT \'{sym}\' AS symbol, MAX("Adj Close") AS max_adj '
            'FROM "{sym}" WHERE Date >= \'2015-01-01\' AND Date <= \'2015-12-31\') '
            'WHERE max_adj > 200').format(sym=s)
    parts.append(part)

sql = '\nUNION ALL\n'.join(parts) if parts else "SELECT NULL as symbol, NULL as max_adj WHERE 0=1"
print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_8UvW6KsMY3Sq7CHGXoSaQiC8': 'file_storage/call_8UvW6KsMY3Sq7CHGXoSaQiC8.json'}

exec(code, env_args)
