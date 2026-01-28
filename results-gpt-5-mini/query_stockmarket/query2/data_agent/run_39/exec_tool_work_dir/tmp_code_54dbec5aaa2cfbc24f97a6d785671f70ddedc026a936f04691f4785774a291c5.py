code = """import json
with open(var_call_zXmuyNql9EkNQeYrQCJ3b3cR, 'r') as f:
    symbols_with_table = json.load(f)

parts = []
for s in symbols_with_table:
    q = (
        "SELECT '" + s + "' AS Symbol, max_adj FROM (SELECT MAX(\"Adj Close\") AS max_adj FROM \"" + s + "\" "
        "WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') WHERE max_adj > 200"
    )
    parts.append(q)

if parts:
    final_sql = " UNION ALL ".join(parts) + ";"
else:
    final_sql = "SELECT NULL WHERE FALSE;"

out = {'sql': final_sql, 'count_tables': len(symbols_with_table)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Lj8XAxsX7AT97Di1xIKGsn9F': 'file_storage/call_Lj8XAxsX7AT97Di1xIKGsn9F.json', 'var_call_EmUNNKSWKE7BeUlKNfhNkVnb': 'file_storage/call_EmUNNKSWKE7BeUlKNfhNkVnb.json', 'var_call_UEVVCI3WmLsOjkdZ82ddOZZr': {'test': True}, 'var_call_zXmuyNql9EkNQeYrQCJ3b3cR': 'file_storage/call_zXmuyNql9EkNQeYrQCJ3b3cR.json'}

exec(code, env_args)
