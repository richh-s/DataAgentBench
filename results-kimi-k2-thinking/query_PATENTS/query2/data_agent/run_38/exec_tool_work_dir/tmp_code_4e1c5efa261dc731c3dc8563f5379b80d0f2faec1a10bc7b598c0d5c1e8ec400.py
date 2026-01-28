code = """import json
import re
from datetime import datetime

# Access the stored result file path
result_file = locals()['var_functions.query_db:6']

# Load the data
with open(result_file, 'r') as f:
    patents_data = json.load(f)

# Sample record for inspection
sample = patents_data[0]

# Parse the CPC field to extract CPC codes
cpc_data = json.loads(sample['cpc']) if sample['cpc'] else []
cpc_codes = [item['code'] for item in cpc_data]

result = {
    'total_records': len(patents_data),
    'sample_cpc_codes': cpc_codes,
    'sample_grant_date': sample['grant_date']
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
