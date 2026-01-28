code = """import json

# Access the stored file path
path_key = 'var_functions.query_db:2'
in_file = locals()[path_key]

# Read the data
with open(in_file, 'r') as f:
    data = json.load(f)

print('Total papers:', len(data))

# Simple extraction
import re
results = []

for doc in data:
    title = doc.get('filename', '').replace('.txt', '')
    text = doc.get('text', '')
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    if year == 2016 and 'physical activity' in text.lower():
        results.append(title)

print('2016 physical activity papers:', len(results))
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
