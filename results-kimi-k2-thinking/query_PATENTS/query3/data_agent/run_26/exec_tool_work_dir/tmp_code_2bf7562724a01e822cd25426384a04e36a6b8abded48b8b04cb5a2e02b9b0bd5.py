code = """import json
import re

# Load UC patents data
result_file = locals()['var_functions.query_db:6']
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = result_file

# Extract all UNIV CALIFORNIA publication numbers
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Find all publication numbers in the text
    matches = re.findall(r'[A-Z]{2}-[A-Z0-9-]+', patents_info)
    for match in matches:
        uc_pub_numbers.add(match)

# Convert to list for SQL IN clause
uc_pub_numbers_list = list(uc_pub_numbers)

# Create a string of publication numbers for SQL query
pub_numbers_str = ', '.join([f'"{num}"' for num in uc_pub_numbers_list[:10]])  # Just first 10 for testing

print('__RESULT__:')
print(json.dumps(f"UC publication numbers sample: {pub_numbers_str[:200]}..."))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'Found 5 patents from UNIV CALIFORNIA', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Found 169 patents assigned to UNIV CALIFORNIA', 'var_functions.execute_python:10': 'Found 1112 unique cited publication numbers', 'var_functions.query_db:12': [], 'var_functions.execute_python:14': 'Found 114 UNIV CALIFORNIA publication numbers', 'var_functions.execute_python:16': ['US-70199003-A', 'AU-2007297661-A', 'WO-2012158833-A3', 'US-2018053351-W', 'AU-2004253879-A1', 'KR-20107024636-A', 'WO-2023239670-A1', 'US-2017145219-A1', 'EP-07753965-A', 'RO-7944874-A'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'Total patents in database: 277813'}

exec(code, env_args)
