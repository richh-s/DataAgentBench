code = """import json
import re
from datetime import datetime
from collections import defaultdict

# Load the full patent data from the stored file
patent_data_path = locals()['var_functions.query_db:5']
with open(patent_data_path, 'r') as f:
    patent_data = json.load(f)

# Load CPC level 5 symbols
cpc_symbols_path = locals()['var_functions.query_db:8']
with open(cpc_symbols_path, 'r') as f:
    cpc_level5_data = json.load(f)

# Create a set of level 5 CPC symbols
cpc_level5_symbols = set()
for record in cpc_level5_data:
    symbol = record['symbol']
    # Normalize symbol - remove any trailing slashes or spaces
    symbol = symbol.strip()
    cpc_level5_symbols.add(symbol)

# Test the set size
print('__RESULT__:')
print(json.dumps({
    'total_patents': len(patent_data),
    'total_level5_symbols': len(cpc_level5_symbols),
    'sample_level5_symbols': list(cpc_level5_symbols)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['cpc_definition'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'total_records': '277813'}], 'var_functions.execute_python:14': {'sample_dates': [[0, 'Aug 3rd, 2021'], [1, 'Oct 6th, 2020'], [2, 'Sep 21st, 2021'], [3, '2020, April 7th'], [4, 'Mar 23rd, 2021'], [5, 'March 2nd, 2021'], [6, '2021, November 9th'], [7, '30th June 2020'], [8, '2021 on Mar 16th'], [9, '9th Nov 2021']], 'sample_cpc_first_200': '[\n  {\n    "code": "C01B33/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "C01B35/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code"'}}

exec(code, env_args)
