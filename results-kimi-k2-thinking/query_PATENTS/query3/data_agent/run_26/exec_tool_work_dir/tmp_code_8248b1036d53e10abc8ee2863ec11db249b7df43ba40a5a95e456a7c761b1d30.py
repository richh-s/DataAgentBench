code = """import json
import re

# Load UC patents data
result_file = locals()['var_functions.query_db:6']
if isinstance(result_file, str) and result_file.endswith('.json'):
    with open(result_file, 'r') as f:
        uc_patents = json.load(f)
else:
    uc_patents = result_file

# Extract publication numbers of all UC patents
uc_pub_numbers = set()
for patent in uc_patents:
    patents_info = patent.get('Patents_info', '')
    # Find all publication numbers in the text
    matches = re.findall(r'[A-Z]{2}-[A-Z0-9-]+', patents_info)
    for match in matches:
        uc_pub_numbers.add(match)

# Split into chunks for multiple queries
uc_pub_numbers_list = list(uc_pub_numbers)
chunk_size = 50
chunks = [uc_pub_numbers_list[i:i + chunk_size] for i in range(0, len(uc_pub_numbers_list), chunk_size)]

print('__RESULT__:')
print(json.dumps(f"Total UC publication numbers: {len(uc_pub_numbers_list)}, divided into {len(chunks)} chunks"))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'Found 5 patents from UNIV CALIFORNIA', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'Found 169 patents assigned to UNIV CALIFORNIA', 'var_functions.execute_python:10': 'Found 1112 unique cited publication numbers', 'var_functions.query_db:12': [], 'var_functions.execute_python:14': 'Found 114 UNIV CALIFORNIA publication numbers', 'var_functions.execute_python:16': ['US-70199003-A', 'AU-2007297661-A', 'WO-2012158833-A3', 'US-2018053351-W', 'AU-2004253879-A1', 'KR-20107024636-A', 'WO-2023239670-A1', 'US-2017145219-A1', 'EP-07753965-A', 'RO-7944874-A'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': 'Total patents in database: 277813', 'var_functions.execute_python:22': 'UC publication numbers sample: "CA-2718348-C", "HK-18104296-A", "AU-2019275518-B2", "CA-3027364-A", "US-2018053351-W", "IL-24402916-A", "AU-2007297661-A1", "US-2022016812-W", "CN-201280035828-A", "US-2017281687-A1"...'}

exec(code, env_args)
