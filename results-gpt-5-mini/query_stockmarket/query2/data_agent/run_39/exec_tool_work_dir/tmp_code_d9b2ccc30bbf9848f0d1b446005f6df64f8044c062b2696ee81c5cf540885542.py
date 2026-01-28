code = """import json
with open(var_call_zXmuyNql9EkNQeYrQCJ3b3cR, 'r') as f:
    symbols = json.load(f)

parts = []
for s in symbols:
    part = ("SELECT '" + s + "' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"" + s + "\" "
            "WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' GROUP BY Symbol HAVING MAX(\"Adj Close\") > 200")
    parts.append(part)

if parts:
    final_sql = " UNION ALL ".join(parts) + ";"
else:
    final_sql = "SELECT NULL WHERE FALSE;"

print('__RESULT__:')
print(json.dumps({'sql': final_sql}))"""

env_args = {'var_call_Lj8XAxsX7AT97Di1xIKGsn9F': 'file_storage/call_Lj8XAxsX7AT97Di1xIKGsn9F.json', 'var_call_EmUNNKSWKE7BeUlKNfhNkVnb': 'file_storage/call_EmUNNKSWKE7BeUlKNfhNkVnb.json', 'var_call_UEVVCI3WmLsOjkdZ82ddOZZr': {'test': True}, 'var_call_zXmuyNql9EkNQeYrQCJ3b3cR': 'file_storage/call_zXmuyNql9EkNQeYrQCJ3b3cR.json', 'var_call_FGW1Z4avDVHKJxeIxHJJ27ew': {'present': ['SPY', 'IVV', 'VOO', 'DIA', 'RSP', 'IWM', 'VTI', 'XLK', 'XLV', 'GDX', 'GLD', 'USO']}}

exec(code, env_args)
