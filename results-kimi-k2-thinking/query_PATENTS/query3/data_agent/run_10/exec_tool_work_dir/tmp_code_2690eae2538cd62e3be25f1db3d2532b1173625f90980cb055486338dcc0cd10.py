code = """import json
import re

# Read the full result from the previous query
result_file = '/tmp/tmpk5h2_8o2.json'
with open(result_file, 'r') as f:
    uc_patents = json.load(f)

print('Total UNIV CALIFORNIA patents: ' + str(len(uc_patents)))

# Examine the structure of Patents_info
sample = uc_patents[0]
print('\nSample Patents_info:')
print(sample['Patents_info'])

# Extract publication number from a sample
pub_num_match = re.search(r'pub\. number ([^\.]+)', sample['Patents_info'])
if pub_num_match:
    pub_num = pub_num_match.group(1).strip()
    print('Extracted publication number: ' + pub_num)

# Check available columns
if len(uc_patents) > 0:
    print('\nAvailable columns:')
    for key in uc_patents[0].keys():
        print('- ' + key)

# Process all UC patents to extract publication numbers
uc_pub_numbers = []
for patent in uc_patents:
    info = patent['Patents_info']
    match = re.search(r'pub\. number ([^\.\,]+)', info)
    if match:
        pub_num = match.group(1).strip()
        uc_pub_numbers.append(pub_num)

print('\nTotal UC publication numbers extracted: ' + str(len(uc_pub_numbers)))
print('First 10: ' + str(uc_pub_numbers[:10]))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'total': '169'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
