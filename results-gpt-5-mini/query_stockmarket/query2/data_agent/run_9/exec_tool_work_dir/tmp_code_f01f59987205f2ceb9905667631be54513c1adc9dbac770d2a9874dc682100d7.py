code = """import json
# Load the common symbols file
with open(var_call_sPUq8PJYpCCHgVos6fsyIewx, 'r') as f:
    symbols = json.load(f)
selects = []
for s in symbols:
    # escape single quotes if any
    lit = s.replace("'", "''")
    sel = f"(SELECT '{lit}' AS Symbol FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1)"
    selects.append(sel)
sql = "\nUNION ALL\n".join(selects) + "\nORDER BY Symbol;"
out = {'sql': sql, 'candidate_count': len(symbols)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_d6OF5lNHFpCkdROe3WXhSEIn': 'file_storage/call_d6OF5lNHFpCkdROe3WXhSEIn.json', 'var_call_pWaf7Rt5WZqXxRrWb0Xhaa1p': 'file_storage/call_pWaf7Rt5WZqXxRrWb0Xhaa1p.json', 'var_call_sPUq8PJYpCCHgVos6fsyIewx': 'file_storage/call_sPUq8PJYpCCHgVos6fsyIewx.json'}

exec(code, env_args)
