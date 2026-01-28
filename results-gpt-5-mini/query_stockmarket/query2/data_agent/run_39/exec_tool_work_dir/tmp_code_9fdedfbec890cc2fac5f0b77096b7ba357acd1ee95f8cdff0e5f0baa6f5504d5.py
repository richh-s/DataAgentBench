code = """import json
with open(var_call_zXmuyNql9EkNQeYrQCJ3b3cR, 'r') as f:
    symbols = json.load(f)

DQ = '"'
batch_size = 150
sql_list = []
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    parts = []
    for s in batch:
        tbl = DQ + s + DQ
        part = "SELECT '" + s + "' AS Symbol, MAX(" + DQ + 'Adj Close' + DQ + ") AS max_adj FROM " + tbl + " WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' GROUP BY Symbol HAVING MAX(" + DQ + 'Adj Close' + DQ + ") > 200"
        parts.append(part)
    sql = " UNION ALL ".join(parts) + ";"
    sql_list.append(sql)

print('__RESULT__:')
print(json.dumps(sql_list))"""

env_args = {'var_call_Lj8XAxsX7AT97Di1xIKGsn9F': 'file_storage/call_Lj8XAxsX7AT97Di1xIKGsn9F.json', 'var_call_EmUNNKSWKE7BeUlKNfhNkVnb': 'file_storage/call_EmUNNKSWKE7BeUlKNfhNkVnb.json', 'var_call_UEVVCI3WmLsOjkdZ82ddOZZr': {'test': True}, 'var_call_zXmuyNql9EkNQeYrQCJ3b3cR': 'file_storage/call_zXmuyNql9EkNQeYrQCJ3b3cR.json', 'var_call_FGW1Z4avDVHKJxeIxHJJ27ew': {'present': ['SPY', 'IVV', 'VOO', 'DIA', 'RSP', 'IWM', 'VTI', 'XLK', 'XLV', 'GDX', 'GLD', 'USO']}, 'var_call_WAiPbYz2Sf1aodfZu3Fvq3UM': 'file_storage/call_WAiPbYz2Sf1aodfZu3Fvq3UM.json', 'var_call_qFnGazoSWpn55ULqB7TPwII5': [{'Symbol': 'SPY', 'max_adj': '193.3121490478516'}, {'Symbol': 'IVV', 'max_adj': '193.5270538330078'}, {'Symbol': 'VOO', 'max_adj': '177.17626953125'}, {'Symbol': 'DIA', 'max_adj': '163.6190185546875'}, {'Symbol': 'RSP', 'max_adj': '76.05020141601562'}, {'Symbol': 'IWM', 'max_adj': '120.37349700927734'}, {'Symbol': 'VTI', 'max_adj': '100.54161834716795'}, {'Symbol': 'XLK', 'max_adj': '41.50289535522461'}, {'Symbol': 'XLV', 'max_adj': '71.13082122802734'}, {'Symbol': 'GDX', 'max_adj': '22.22186088562012'}, {'Symbol': 'GLD', 'max_adj': '125.2300033569336'}, {'Symbol': 'USO', 'max_adj': '20.81999969482422'}]}

exec(code, env_args)
