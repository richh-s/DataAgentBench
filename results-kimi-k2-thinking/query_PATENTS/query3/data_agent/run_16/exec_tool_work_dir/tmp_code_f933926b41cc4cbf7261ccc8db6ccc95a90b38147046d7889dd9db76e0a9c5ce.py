code = """import json
import re

# Access the stored data
uc_file_key = 'var_functions.query_db:28'
uc_file_path = locals()[uc_file_key]

print('Loading UC patents from file path')

with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

print('Number of UC patents found:', len(uc_patents))

# Extract all UC publication numbers from Patents_info
uc_pub_numbers = []
for patent in uc_patents:
    info = patent['Patents_info']
    # Look for patterns with country code and publication number
    matches = re.findall(r'[A-Z]{2}-[A-Z0-9-]+', info)
    if matches:
        # Take the last one which is usually the publication number
        uc_pub_numbers.append(matches[-1])

print('First 20 UC publication numbers found:')
for i, pub in enumerate(uc_pub_numbers[:20]):
    print(i+1, pub)

# Save to file for next steps
result = {
    'uc_patents_count': len(uc_patents),
    'uc_pub_numbers_count': len(uc_pub_numbers),
    'first_10_pub_numbers': uc_pub_numbers[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': [{'total_patents': '277813'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
