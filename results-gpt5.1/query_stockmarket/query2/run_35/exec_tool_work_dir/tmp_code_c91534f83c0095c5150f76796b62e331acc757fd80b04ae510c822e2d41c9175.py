code = """import json

# load symbol list
path = var_call_ZWATNpyEiMv1JqlmKYVAm4Tu
with open(path, 'r') as f:
    etf_symbols = json.load(f)

# build a DuckDB SQL that unions all ETFs with condition; but DuckDB doesn't allow dynamic table names in one query easily via this interface
# Instead, we'll just return the subset symbol list; the driving query per-symbol must be executed separately.

result = json.dumps(etf_symbols[:50])
print("__RESULT__:")
print(result)"""

env_args = {'var_call_WUi3vmoHmC78nA9fqo38vTMV': 'file_storage/call_WUi3vmoHmC78nA9fqo38vTMV.json', 'var_call_ueGJMCiIOBoJqbiWYhZkMGIU': 'file_storage/call_ueGJMCiIOBoJqbiWYhZkMGIU.json', 'var_call_ZWATNpyEiMv1JqlmKYVAm4Tu': 'file_storage/call_ZWATNpyEiMv1JqlmKYVAm4Tu.json'}

exec(code, env_args)
