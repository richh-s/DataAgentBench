code = """import json

key1 = 'var_function-call-15483899617551082624'
key2 = 'var_function-call-17197364182680462886'

path_etfs = locals()[key1]
path_tables = locals()[key2]

with open(path_etfs, 'r') as f:
    etf_list = json.load(f)
etf_symbols = [item['Symbol'] for item in etf_list]

with open(path_tables, 'r') as f:
    table_list = json.load(f)

valid_etfs = sorted(list(set(etf_symbols).intersection(set(table_list))))

queries = []
batch_size = 50
current_batch = []

for i, sym in enumerate(valid_etfs):
    current_batch.append(sym)
    if len(current_batch) == batch_size or i == len(valid_etfs) - 1:
        parts = []
        for s in current_batch:
            # Using date range instead of LIKE with %
            q = "SELECT '{0}' as Symbol FROM \"{0}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1".format(s)
            parts.append(q)
        
        full_query = " UNION ALL ".join(parts)
        queries.append(full_query)
        current_batch = []

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-15483899617551082624': 'file_storage/function-call-15483899617551082624.json', 'var_function-call-17197364182680462886': 'file_storage/function-call-17197364182680462886.json', 'var_function-call-2473417228619815935': {'count': 1435, 'preview': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
