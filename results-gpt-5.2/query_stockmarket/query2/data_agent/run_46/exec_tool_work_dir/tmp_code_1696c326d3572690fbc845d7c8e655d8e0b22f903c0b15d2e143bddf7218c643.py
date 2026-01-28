code = """import json
# Build full union query for all NYSE Arca ETFs
path = var_call_8BRy2xXU5qjQcBQIHostXyf0
with open(path,'r') as f:
    etfs=json.load(f)
syms=sorted({r['Symbol'] for r in etfs if r.get('Symbol')})
parts=[]
for s in syms:
    t='"'+s.replace('"','""')+'"'
    parts.append("SELECT '{0}' AS Symbol, MAX(\"Adj Close\")::DOUBLE AS max_adj_close_2015 FROM {1} WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'".format(s,t))
union_query='WITH per_symbol AS ('+' UNION ALL '.join(parts)+') SELECT Symbol, max_adj_close_2015 FROM per_symbol WHERE max_adj_close_2015 > 200 ORDER BY Symbol;'
print('__RESULT__:')
print(json.dumps({'query': union_query}))"""

env_args = {'var_call_8BRy2xXU5qjQcBQIHostXyf0': 'file_storage/call_8BRy2xXU5qjQcBQIHostXyf0.json', 'var_call_sNc7LSyyo3Q8oR8uQ2zyBJlI': 'file_storage/call_sNc7LSyyo3Q8oR8uQ2zyBJlI.json', 'var_call_D2A4AkssA2zdwP3ykx458LjE': {'symbols_in_metadata': 1435, 'symbols_with_price_table': 1435}, 'var_call_liv3de3OtIkEkZNAnm3uadTt': [], 'var_call_MjXFgBHIc0u7SOpz4alaVakO': [{'Symbol': 'SPY', 'max_adj_close_2015': '193.3121490478516'}], 'var_call_cLRv5kj9IF6gpsOJd8hNXDBH': [{'max_adj_close_2015': '120.37349700927734'}]}

exec(code, env_args)
