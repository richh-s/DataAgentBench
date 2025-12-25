code = """import json

res = json.loads(var_call_c69S7TAh1s5YtgQLn5WnNlbd)
syms = res['symbols']

chunks = []
for i in range(0, len(syms), 200):
    chunk = syms[i:i+200]
    union_parts = []
    for s in chunk:
        q = "SELECT '" + s + "' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM '" + s + "' WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
        union_parts.append(q)
    full_q = " UNION ALL ".join(union_parts)
    chunks.append(full_q)

print("__RESULT__:")
print(json.dumps({"num_chunks": len(chunks), "first_chunk": chunks[0]}))"""

env_args = {'var_call_INMjZwxTuggVM0UvElB2DSPD': 'file_storage/call_INMjZwxTuggVM0UvElB2DSPD.json', 'var_call_4Vk7HCYpFXCGm55S4w8dVQQP': 'file_storage/call_4Vk7HCYpFXCGm55S4w8dVQQP.json', 'var_call_c69S7TAh1s5YtgQLn5WnNlbd': {'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY'], 'total_symbols': 1435}}

exec(code, env_args)
