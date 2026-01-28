code = """import json
import re

# Load all UNIV CALIFORNIA patents from the query result file
file_path = var_functions.query_db:5

# Read the JSON file
with open(file_path, 'r') as f:
    univ_california_patents = json.load(f)

# Extract publication numbers for UNIV CALIFORNIA patents
univ_california_pub_nums = set()
for patent in univ_california_patents:
    patents_info = patent['Patents_info']
    # Look for publication number patterns
    # Patterns: "pub. number US-2022074631-A1" or "publication number US-11421276-B2"
    match = re.search(r'(?:pub\.?|publication) number\s+([A-Z]{2}-[A-Z0-9-]+)', patents_info, re.IGNORECASE)
    if match:
        pub_num = match.group(1)
        univ_california_pub_nums.add(pub_num)

print('__RESULT__:')
print(json.dumps({
    'count': len(univ_california_patents),
    'publication_numbers': list(univ_california_pub_nums)[:10],  # Show first 10
    'total_unique_pub_nums': len(univ_california_pub_nums)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
