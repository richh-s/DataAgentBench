code = """import json
path = var_call_o84Oh8SkIPFhXx6zUTdO5ZJn
with open(path,'r') as f:
    etfs=json.load(f)
syms=[r['Symbol'] for r in etfs]
chunks=[syms[i:i+180] for i in range(0,len(syms),180)]
chunk=chunks[0]
union_parts=[]
for s in chunk:
    part = "SELECT '{sym}' AS Symbol, MAX(CAST(\"Adj Close\" AS DOUBLE)) AS max_adj_close_2015 FROM \"{sym}\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31'".format(sym=s)
    union_parts.append(part)
query = " UNION ALL ".join(union_parts)
print('__RESULT__:')
print(json.dumps({'chunk_size':len(chunk),'sql_len':len(query), 'sql_preview':query[:220]}))"""

env_args = {'var_call_Sk4bpIXrh9p4aw5g9DSpoMFB': ['stockinfo'], 'var_call_oEphkAuLQrFiLRZIfAo1H2KM': 'file_storage/call_oEphkAuLQrFiLRZIfAo1H2KM.json', 'var_call_o84Oh8SkIPFhXx6zUTdO5ZJn': 'file_storage/call_o84Oh8SkIPFhXx6zUTdO5ZJn.json', 'var_call_8TdNBLZQYSpkT4nsMfgeBHfL': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_eak9UtAw8lTIkC8AhTKqi1M3': [{'Adj Close': '26.299287796020508'}], 'var_call_z4bXQxd0oM1AGn49DICAiPhJ': {'count': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_CRkwd4GGKxxl0lhlorEAnVvy': {'n': 1435, 'chunks': 8, 'chunk0': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_call_zTPu0EaThlsdYD6TRm2a5SMb': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'var_call_c87Eg3zrnfgxxYwlMsvHkcGZ': {'bad_count': 0, 'bad_examples': []}, 'var_call_npJw6svkIJRIcrCA17c7kEm5': [{'symbol': 'AADR', 'max_adj_close_2015': '39.58057403564453'}], 'var_call_NwHqYa8ZjJt4M1UsJp0mATad': {'min': 'AAAU', 'max': 'ZSL', 'contains_AAAU': True}, 'var_call_c2RxtGrnefQxaMb0gNmAncMj': [{'n': '0'}], 'var_call_2KceOjWpkvLagGowf3dfmTzw': [{'min_date': '2018-08-15', 'max_date': '2020-04-01', 'n': '410'}]}

exec(code, env_args)
