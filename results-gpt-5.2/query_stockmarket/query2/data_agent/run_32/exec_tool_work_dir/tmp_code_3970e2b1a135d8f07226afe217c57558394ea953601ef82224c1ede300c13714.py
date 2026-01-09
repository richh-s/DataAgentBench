code = """import json

def load(v):
    if isinstance(v, str):
        with open(v,'r') as f:
            return json.load(f)
    return v

d = load(var_call_cxUz4FCtwLwK13kwgV4VSxlj)
syms = d['symbols']

# Build a DuckDB query that unions max Adj Close in 2015 for each symbol
parts = []
for s in syms:
    tbl = s.replace('"','""')
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{tbl}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'")

query = "\nUNION ALL\n".join(parts)
print('__RESULT__:')
print(json.dumps({'query': query, 'n_tables': len(parts)}))"""

env_args = {'var_call_WUWNAstTHRWuxShkejbmmb3q': 'file_storage/call_WUWNAstTHRWuxShkejbmmb3q.json', 'var_call_wN5P7wyYzbAWkh7ELYtCJadn': 'file_storage/call_wN5P7wyYzbAWkh7ELYtCJadn.json', 'var_call_cxUz4FCtwLwK13kwgV4VSxlj': 'file_storage/call_cxUz4FCtwLwK13kwgV4VSxlj.json'}

exec(code, env_args)
