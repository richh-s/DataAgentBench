code = """import json

def load_records(v):
    if isinstance(v, str):
        with open(v,'r') as f:
            return json.load(f)
    return v

syms = load_records(var_call_cxUz4FCtwLwK13kwgV4VSxlj)['symbols']
parts=[]
for s in syms[:5]:
    parts.append("SELECT '{s}' AS symbol".format(s=s))
q=' UNION ALL '.join(parts)
print('__RESULT__:')
print(json.dumps({'q': q}))"""

env_args = {'var_call_WUWNAstTHRWuxShkejbmmb3q': 'file_storage/call_WUWNAstTHRWuxShkejbmmb3q.json', 'var_call_wN5P7wyYzbAWkh7ELYtCJadn': 'file_storage/call_wN5P7wyYzbAWkh7ELYtCJadn.json', 'var_call_cxUz4FCtwLwK13kwgV4VSxlj': 'file_storage/call_cxUz4FCtwLwK13kwgV4VSxlj.json', 'var_call_bzIiHOXKAVaDurLZUe3EHHme': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_DGidQhEOR4s7IAaFoMGUI6sO': [{'symbol': 'AAAU', 'max_adj_close_2015': 'nan'}]}

exec(code, env_args)
