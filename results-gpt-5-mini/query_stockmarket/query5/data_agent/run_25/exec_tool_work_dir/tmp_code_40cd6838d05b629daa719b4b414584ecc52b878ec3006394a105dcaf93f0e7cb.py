code = """import json
with open(var_call_cOi9OMUYcXvqMM1mSCci0y6k, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_ppF3FrkgSKRwnihegO5SvHTe, 'r') as f:
    tables = json.load(f)

symbols_s = [rec['Symbol'] for rec in stockinfo if rec.get('Market Category') == 'S']
symbols_s = [s.strip() for s in symbols_s]
tables_set = set(tables)
symbols_to_query = sorted([s for s in symbols_s if s in tables_set])

if not symbols_to_query:
    sql = "SELECT '' as Symbol, 0 as days LIMIT 0;"
else:
    parts = []
    for s in symbols_to_query:
        part = "SELECT '%s' AS Symbol, \"Date\", \"High\", \"Low\" FROM \"%s\" WHERE \"Date\" LIKE '2019-%%' AND (\"High\" - \"Low\") > 0.2 * \"Low\"" % (s, s)
        parts.append(part)
    union_sql = "\nUNION ALL\n".join(parts)
    sql = "SELECT Symbol, COUNT(*) as days FROM (\n%s\n) t GROUP BY Symbol ORDER BY days DESC LIMIT 5;" % union_sql

result = {"sql": sql, "symbols_count": len(symbols_to_query)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cOi9OMUYcXvqMM1mSCci0y6k': 'file_storage/call_cOi9OMUYcXvqMM1mSCci0y6k.json', 'var_call_ppF3FrkgSKRwnihegO5SvHTe': 'file_storage/call_ppF3FrkgSKRwnihegO5SvHTe.json'}

exec(code, env_args)
