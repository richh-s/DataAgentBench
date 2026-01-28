code = """import json
with open(var_call_kponoIuDHUEwq9e7xalQW6GZ,'r') as f:
    info=json.load(f)
syms=sorted({r['Symbol'] for r in info})
batches=[syms[i:i+40] for i in range(0,len(syms),40)]
queries=[]
for b in batches:
    parts=[]
    for s in b:
        parts.append("SELECT '{s}' AS symbol, MAX(\\\"Adj Close\\\") AS max_adj_close FROM \\\"{s}\\\" WHERE \\\"Date\\\" BETWEEN '2015-01-01' AND '2015-12-31' HAVING MAX(\\\"Adj Close\\\") > 200".format(s=s))
    queries.append(" UNION ALL ".join(parts))
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_kponoIuDHUEwq9e7xalQW6GZ': 'file_storage/call_kponoIuDHUEwq9e7xalQW6GZ.json', 'var_call_TwzwBf2CmUgz31GMXGZ9o0lB': 'file_storage/call_TwzwBf2CmUgz31GMXGZ9o0lB.json', 'var_call_Xrg9kOJDlc2kXxtL5GJXTznh': [{'symbol': 'SPY', 'max_adj_close': '193.3121490478516'}], 'var_call_Q8z2nea3JG18qa0BPuomzZln': 'ok', 'var_call_7BMhlXRncCAyexjmMVlRDx0L': 'a', 'var_call_RZJn9nNTovXDj4fNNdtACmQ3': "SELECT 'SPY' AS symbol", 'var_call_Z7TEETrSunqDHTB52Nryqcoa': 'MAX("Adj Close")', 'var_call_L6iESwlBGwqvPW08MXHv52wW': [], 'var_call_ZZ3eMI1iiqZr0nQGEKMUITAZ': [], 'var_call_q8gzxyQ5B4YFg6HsmBc9f1XH': [], 'var_call_laiZKbodVMxGCjNIGqltd2Fq': [], 'var_call_N1kHcBmNh1ftDioZJNTPRyxP': [], 'var_call_SepGPHgPaPxQDT74DFipwxmn': 'MAX("Adj Close")', 'var_call_mWGD2Kw8wqHbcb2P93zuhIJg': 'SELECT \'SPY\' AS symbol, MAX("Adj Close") AS max_adj_close FROM "SPY" WHERE "Date" BETWEEN \'2015-01-01\' AND \'2015-12-31\' HAVING MAX("Adj Close") > 200', 'var_call_dyQoPhCEloK13T2NqpPIMwJC': {'n_symbols': 1435, 'n_batches': 36, 'first_query_len': 6453}}

exec(code, env_args)
