code = """import json
with open(var_call_zXmuyNql9EkNQeYrQCJ3b3cR, 'r') as f:
    symbols = json.load(f)

parts = []
DQ = chr(34)
for s in symbols:
    tbl = DQ + s + DQ
    part = "SELECT '" + s + "' AS Symbol, MAX(" + DQ + 'Adj Close' + DQ + ") AS max_adj FROM " + tbl + " WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' GROUP BY Symbol HAVING MAX(" + DQ + 'Adj Close' + DQ + ") > 200"
    parts.append(part)

final_sql = " UNION ALL ".join(parts) + ";"
# Output only the SQL (may be large)
print('__RESULT__:')
print(json.dumps(final_sql))"""

env_args = {'var_call_Lj8XAxsX7AT97Di1xIKGsn9F': 'file_storage/call_Lj8XAxsX7AT97Di1xIKGsn9F.json', 'var_call_EmUNNKSWKE7BeUlKNfhNkVnb': 'file_storage/call_EmUNNKSWKE7BeUlKNfhNkVnb.json', 'var_call_UEVVCI3WmLsOjkdZ82ddOZZr': {'test': True}, 'var_call_zXmuyNql9EkNQeYrQCJ3b3cR': 'file_storage/call_zXmuyNql9EkNQeYrQCJ3b3cR.json', 'var_call_FGW1Z4avDVHKJxeIxHJJ27ew': {'present': ['SPY', 'IVV', 'VOO', 'DIA', 'RSP', 'IWM', 'VTI', 'XLK', 'XLV', 'GDX', 'GLD', 'USO']}}

exec(code, env_args)
