code = """import json

def load_json_maybe(x):
    if isinstance(x, str):
        with open(x, 'r') as f:
            return json.load(f)
    return x

info = load_json_maybe(var_call_9x43jhvltlIk3SV75Wkfhm1D)
tables = set(load_json_maybe(var_call_2AhcoWPmgTbeg1mwSm0bl5Iu))
nyse = [r.get('Symbol') for r in info if r.get('Symbol') in tables]

parts = []
for sym in nyse:
    q = (
        "SELECT '{sym}' AS Symbol, "
        "SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, "
        "SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days "
        "FROM \"{sym}\" WHERE Date>='2017-01-01' AND Date<='2017-12-31'"
    ).format(sym=sym)
    parts.append(q)

union_sql = " UNION ALL ".join(parts)

out = {'n_syms': len(nyse), 'sql_len': len(union_sql), 'sql_preview': union_sql[:300]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_2AhcoWPmgTbeg1mwSm0bl5Iu': 'file_storage/call_2AhcoWPmgTbeg1mwSm0bl5Iu.json', 'var_call_9x43jhvltlIk3SV75Wkfhm1D': 'file_storage/call_9x43jhvltlIk3SV75Wkfhm1D.json', 'var_call_PcX3URHolGNr3LCrnXyGvtYl': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_gcCoUDDwmTZgAujoo3GWRYxN': {'ok': True, 'n': 5}, 'var_call_sVFDtSgXuR1uhJiGj3xemzGS': [{'cnt': '2753'}], 'var_call_SJBkav9SANFxwSXYdNgiGg5g': {'n_symbols': 234, 'n_chunks': 1, 'first_chunk': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_gHnttgm3rfA2U00yiYMcwMAn': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}], 'var_call_Lo4ndOg9ZaTM9TfJcEjdOJ0G': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}], 'var_call_30d8enOzVDh5eKqwK2q0KpXt': [{'Symbol': 'AEFC'}, {'Symbol': 'AIN'}]}

exec(code, env_args)
