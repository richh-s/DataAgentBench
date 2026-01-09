code = """import json

def build_query(symbols):
    parts = []
    for s in symbols:
        parts.append(
            "SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s)
        )
    if not parts:
        return None
    union_query = " UNION ALL ".join(parts)
    return "SELECT symbol, max_adj_close FROM ({u}) t WHERE max_adj_close > 200 ORDER BY symbol".format(u=union_query)

# test small
q = build_query(['SPY','DIA'])
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_call_kponoIuDHUEwq9e7xalQW6GZ': 'file_storage/call_kponoIuDHUEwq9e7xalQW6GZ.json', 'var_call_TwzwBf2CmUgz31GMXGZ9o0lB': 'file_storage/call_TwzwBf2CmUgz31GMXGZ9o0lB.json', 'var_call_Xrg9kOJDlc2kXxtL5GJXTznh': [{'symbol': 'SPY', 'max_adj_close': '193.3121490478516'}]}

exec(code, env_args)
