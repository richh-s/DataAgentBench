code = """import json, pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str):
        with open(path_or_obj, 'r') as f:
            return json.load(f)
    return path_or_obj

info = load_json_maybe(var_call_9x43jhvltlIk3SV75Wkfhm1D)
tables = load_json_maybe(var_call_2AhcoWPmgTbeg1mwSm0bl5Iu)

df_info = pd.DataFrame(info)
nyse_syms = set(df_info['Symbol'].dropna().astype(str))
trade_set = set(tables)
syms = sorted(list(nyse_syms & trade_set))

# create chunks of symbols for SQL unnest
chunk_size = 250
chunks = [syms[i:i+chunk_size] for i in range(0, len(syms), chunk_size)]

print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'n_chunks': len(chunks), 'first_chunk': chunks[0][:10]}))"""

env_args = {'var_call_2AhcoWPmgTbeg1mwSm0bl5Iu': 'file_storage/call_2AhcoWPmgTbeg1mwSm0bl5Iu.json', 'var_call_9x43jhvltlIk3SV75Wkfhm1D': 'file_storage/call_9x43jhvltlIk3SV75Wkfhm1D.json', 'var_call_PcX3URHolGNr3LCrnXyGvtYl': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_gcCoUDDwmTZgAujoo3GWRYxN': {'ok': True, 'n': 5}, 'var_call_sVFDtSgXuR1uhJiGj3xemzGS': [{'cnt': '2753'}]}

exec(code, env_args)
