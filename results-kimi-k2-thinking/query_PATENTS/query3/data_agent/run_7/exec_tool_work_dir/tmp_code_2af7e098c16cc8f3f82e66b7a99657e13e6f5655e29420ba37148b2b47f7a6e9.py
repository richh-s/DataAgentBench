code = """import json
import re

# Load the file path from the query result and read the data
file_path = '/tmp/tmpql7z7p3v.json'

with open(file_path, 'r') as f:
    data = json.load(f)

# Extract all UNIV CALIFORNIA publication numbers
univ_california_pub_nums = set()
for row in data:
    patents_info = row['Patents_info']
    # Look for publication numbers in various formats
    # Pattern: "pub. number XX-YYYYY-Z" or "publication number XX-YYYYY-Z"
    match = re.search(r'(?:pub\.?|publication)\s+number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        univ_california_pub_nums.add(pub_num)
    # Also look for patterns like "pub. number XX-YYYYY-Z."
    match2 = re.search(r'(?:pub\.?|publication)\s+number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info + '.', re.IGNORECASE)
    if match2:
        pub_num = match2.group(1)
        univ_california_pub_nums.add(pub_num)

print('__RESULT__:')
print(json.dumps({
    'total_records': len(data),
    'unique_publication_numbers': list(univ_california_pub_nums),
    'count': len(univ_california_pub_nums)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', '__builtins__', 'json']}, 'var_functions.list_db:14': ['cpc_definition'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'tmp_files': [], 'result_path': None, 'pwd': '/workspace'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
