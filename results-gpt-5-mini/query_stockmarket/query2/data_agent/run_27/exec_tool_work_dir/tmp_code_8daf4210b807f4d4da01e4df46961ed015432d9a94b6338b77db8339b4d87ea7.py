code = """import json
# load stockinfo symbols
path_info = var_call_8UvW6KsMY3Sq7CHGXoSaQiC8
data_info = json.load(open(path_info, 'r'))
symbols_info = [rec['Symbol'] for rec in data_info]
# load stocktrade tables
path_trade = var_call_HRvR8LlnRtRJNSMY9MC1q8G7
tables = json.load(open(path_trade, 'r'))
# intersection
symbols = [s for s in symbols_info if s in tables]
parts = []
for s in symbols:
    sym_esc = s.replace("'", "''")
    part = ("SELECT * FROM (SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj "
            "FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') "
            "WHERE max_adj > 200").format(sym=sym_esc)
    parts.append(part)

if parts:
    sql = '\nUNION ALL\n'.join(parts)
else:
    sql = "SELECT NULL as symbol, NULL as max_adj WHERE 0=1"

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_8UvW6KsMY3Sq7CHGXoSaQiC8': 'file_storage/call_8UvW6KsMY3Sq7CHGXoSaQiC8.json', 'var_call_HRvR8LlnRtRJNSMY9MC1q8G7': 'file_storage/call_HRvR8LlnRtRJNSMY9MC1q8G7.json'}

exec(code, env_args)
