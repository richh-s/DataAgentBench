code = """import json
import re

# Read the full result from the previous query with UC patents
result_file = '/tmp/tmpk5h2_8o2.json'
with open(result_file, 'r') as f:
    uc_patents = json.load(f)

print('Total UNIV CALIFORNIA patents: ' + str(len(uc_patents)))

# Extract publication numbers from UC patents
uc_pub_numbers = []
for patent in uc_patents:
    info = patent['Patents_info']
    # Look for publication number patterns
    match = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z-]+)', info)
    if match:
        pub_num = match.group(1)
        uc_pub_numbers.append(pub_num)

print('Total UC publication numbers extracted: ' + str(len(uc_pub_numbers)))
print('First 10: ' + str(uc_pub_numbers[:10]))

# Save for later use
with open('/tmp/uc_pub_numbers.json', 'w') as f:
    json.dump(uc_pub_numbers, f)

print('Saved UC publication numbers to file')"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'total': '169'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
