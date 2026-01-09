code = """import json
with open(var_call_Gx0fPAIHRtr9SkCxfjDwil6o,'r') as f:
    syms=[r['symbol'] for r in json.load(f)]
with open(var_call_nw88mOLNaNXYP9FlwW2dbIk1,'r') as f:
    tables=set([r['table_name'] for r in json.load(f)])
syms_in=[s for s in syms if s in tables]
# chunk into groups
chunks=[syms_in[i:i+200] for i in range(0,len(syms_in),200)]
queries=[]
for ch in chunks:
    parts=[]
    for s in ch:
        parts.append("SELECT '{}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{}\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'".format(s,s))
    union=" UNION ALL ".join(parts)
    queries.append("SELECT symbol, max_adj_close FROM ("+union+") t WHERE max_adj_close > 200")
print('__RESULT__:')
print(json.dumps({'n_symbols':len(syms_in),'n_chunks':len(chunks),'queries':queries[:3],'note':'queries array may be long'}))"""

env_args = {'var_call_Gx0fPAIHRtr9SkCxfjDwil6o': 'file_storage/call_Gx0fPAIHRtr9SkCxfjDwil6o.json', 'var_call_x46B2WTQq6zbsoWLQaJw9Uiv': 'file_storage/call_x46B2WTQq6zbsoWLQaJw9Uiv.json', 'var_call_nw88mOLNaNXYP9FlwW2dbIk1': 'file_storage/call_nw88mOLNaNXYP9FlwW2dbIk1.json'}

exec(code, env_args)
