code = """import json

def load_records(v):
    if isinstance(v, str):
        with open(v,'r') as f:
            return json.load(f)
    return v

syms = load_records(var_call_cxUz4FCtwLwK13kwgV4VSxlj)['symbols']

# chunk to avoid huge queries
chunks = [syms[i:i+200] for i in range(0, len(syms), 200)]
print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'n_chunks': len(chunks), 'first_chunk': chunks[0]}))"""

env_args = {'var_call_WUWNAstTHRWuxShkejbmmb3q': 'file_storage/call_WUWNAstTHRWuxShkejbmmb3q.json', 'var_call_wN5P7wyYzbAWkh7ELYtCJadn': 'file_storage/call_wN5P7wyYzbAWkh7ELYtCJadn.json', 'var_call_cxUz4FCtwLwK13kwgV4VSxlj': 'file_storage/call_cxUz4FCtwLwK13kwgV4VSxlj.json', 'var_call_bzIiHOXKAVaDurLZUe3EHHme': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_DGidQhEOR4s7IAaFoMGUI6sO': [{'symbol': 'AAAU', 'max_adj_close_2015': 'nan'}], 'var_call_MWglBBk8bzXx5ui4ILjZUsvp': {'q': "SELECT 'AAAU' AS symbol UNION ALL SELECT 'AADR' AS symbol UNION ALL SELECT 'ABEQ' AS symbol UNION ALL SELECT 'ACSG' AS symbol UNION ALL SELECT 'ACWF' AS symbol"}, 'var_call_fO0S1lmK401H5vNT4tc8NLzO': {'q': "SELECT 'AAAU' AS symbol, MAX(Adj Close) AS max_adj_close_2015 FROM AAAU WHERE Date >= '2015-01-01' AND Date < '2016-01-01'"}, 'var_call_tlFcFZGgAplyHtnhDg9nxiXE': [{'max_adj_close_2015': 'nan'}]}

exec(code, env_args)
