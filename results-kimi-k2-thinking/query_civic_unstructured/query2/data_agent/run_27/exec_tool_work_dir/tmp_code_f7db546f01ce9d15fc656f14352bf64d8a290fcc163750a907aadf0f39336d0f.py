code = """import json
import re

# Load civic documents from file
with open('var_functions.query_db:16.json', 'r') as f:
    civic_docs = json.load(f)

# Load funding data from file  
with open('var_functions.query_db:17.json', 'r') as f:
    funding_data = json.load(f)

print('Loaded ' + str(len(civic_docs)) + ' civic documents')
print('Loaded ' + str(len(funding_data)) + ' funding records')

# Sample data to understand structure
print('Sample civic doc keys: ' + str(list(civic_docs[0].keys())))
print('Sample civic doc filename: ' + str(civic_docs[0].get('filename')))
print('Sample funding record: ' + str(funding_data[0]))

# Check for date patterns in civic docs
sample_text = civic_docs[0].get('text', '')
# Look for completion dates
completion_patterns = ['completed', 'Complete Construction', 'Notice of completion', 'construction was completed']
for pattern in completion_patterns:
    if pattern.lower() in sample_text.lower():
        print(f'Found pattern "{pattern}" in sample text')
        # Show context around the pattern
        idx = sample_text.lower().find(pattern.lower())
        print('Context: ' + sample_text[max(0, idx-100):min(len(sample_text), idx+100)])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
