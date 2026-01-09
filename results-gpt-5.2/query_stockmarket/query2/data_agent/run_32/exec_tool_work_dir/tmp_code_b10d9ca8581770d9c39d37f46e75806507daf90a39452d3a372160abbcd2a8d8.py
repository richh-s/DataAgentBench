code = """import json

def load_records(v):
    if isinstance(v, str):
        with open(v,'r') as f:
            return json.load(f)
    return v

syms = load_records(var_call_cxUz4FCtwLwK13kwgV4VSxlj)['symbols']
parts=[]
for s in syms[:50]:
    s_sql = s.replace("'","''")
    parts.append("SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{t}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'".format(s=s_sql, t=s))
q=' UNION ALL '.join(parts)
print('__RESULT__:')
print(json.dumps({'q': q, 'n': len(parts)}))"""

env_args = {'var_call_WUWNAstTHRWuxShkejbmmb3q': 'file_storage/call_WUWNAstTHRWuxShkejbmmb3q.json', 'var_call_wN5P7wyYzbAWkh7ELYtCJadn': 'file_storage/call_wN5P7wyYzbAWkh7ELYtCJadn.json', 'var_call_cxUz4FCtwLwK13kwgV4VSxlj': 'file_storage/call_cxUz4FCtwLwK13kwgV4VSxlj.json', 'var_call_bzIiHOXKAVaDurLZUe3EHHme': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_DGidQhEOR4s7IAaFoMGUI6sO': [{'symbol': 'AAAU', 'max_adj_close_2015': 'nan'}], 'var_call_MWglBBk8bzXx5ui4ILjZUsvp': {'q': "SELECT 'AAAU' AS symbol UNION ALL SELECT 'AADR' AS symbol UNION ALL SELECT 'ABEQ' AS symbol UNION ALL SELECT 'ACSG' AS symbol UNION ALL SELECT 'ACWF' AS symbol"}}

exec(code, env_args)
