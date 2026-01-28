code = """import json
# Read storage variables (file paths)
path_symbols = var_call_Ad4UsH2M8L6uC8cGxj7jUQRQ
path_tables = var_call_SiXzvTbfmBNhOMQ5JDOIG3NS

data_symbols = json.load(open(path_symbols, 'r'))
data_tables = json.load(open(path_tables, 'r'))

# data_symbols is list of dicts with Symbol and Company Description
symbols_in_info = {rec['Symbol']: rec.get('Company Description', '') for rec in data_symbols}

# data_tables is list of table names (tickers)
set_tables = set(data_tables)

# Intersection: only consider symbols that are in trade DB and in stockinfo S list
common_symbols = [s for s in symbols_in_info.keys() if s in set_tables]

# Prepare output list of dicts
out = [{'Symbol': s, 'Company Description': symbols_in_info[s]} for s in common_symbols]

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_Ad4UsH2M8L6uC8cGxj7jUQRQ': 'file_storage/call_Ad4UsH2M8L6uC8cGxj7jUQRQ.json', 'var_call_SiXzvTbfmBNhOMQ5JDOIG3NS': 'file_storage/call_SiXzvTbfmBNhOMQ5JDOIG3NS.json'}

exec(code, env_args)
