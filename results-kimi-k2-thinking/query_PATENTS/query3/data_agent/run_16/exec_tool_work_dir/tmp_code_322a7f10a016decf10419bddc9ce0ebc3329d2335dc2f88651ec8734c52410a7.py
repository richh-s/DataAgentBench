code = """import json
import re

# Access the stored data
uc_data_key = 'var_functions.query_db:14'
uc_file_path = locals()[uc_data_key]

print('Loading UC data from:', uc_file_path)

with open(uc_file_path, 'r') as f:
    uc_patents = json.load(f)

print('Number of patents assigned to UNIV CALIFORNIA:', len(uc_patents))

# Extract publication numbers for UC patents
uc_pub_numbers = []
for patent in uc_patents[:10]:  # Check first 10 for debugging
    info = patent['Patents_info']
    print('Processing:', info[:100] + '...')
    # Look for publication numbers in various formats
    match = re.search(r'pub\. number.*?([A-Z]{2}-[A-Z0-9-]+)', info)
    if not match:
        match = re.search(r'publication number.*?([A-Z]{2}-[A-Z0-9-]+)', info)
    if not match:
        match = re.search(r'(US-[A-Z0-9-]+)', info)
    
    if match:
        pub_num = match.group(1)
        print('  Found:', pub_num)
        uc_pub_numbers.append(pub_num)

print('\nExtracted publication numbers from first 10 patents')
print('Sample:', uc_pub_numbers)

result = {
    'uc_patents_count': len(uc_patents),
    'sample_uc_pub_numbers': uc_pub_numbers
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
