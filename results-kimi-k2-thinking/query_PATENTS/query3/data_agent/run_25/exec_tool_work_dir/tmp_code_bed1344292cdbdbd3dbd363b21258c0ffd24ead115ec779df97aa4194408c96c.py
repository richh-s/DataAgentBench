code = """import json
import re

# Load data from previous query
data = locals()['var_functions.query_db:8']
if isinstance(data, str):
    with open(data, 'r') as f:
        data = json.load(f)

# Analyze patterns in Patents_info
assignees = []
sample_patents_info = []
for i, row in enumerate(data[:100]):  # Sample first 100 rows
    patents_info = row.get('Patents_info', '')
    sample_patents_info.append(patents_info)
    
    # Try to extract assignee
    patterns = [
        r'^(.*?) holds the US',  
        r'^(.*?) holds the US',
        r'^(.*?) holds the US',
        r'In US, the (?:application|patent filing|patent application) (?:\(.*?\) )?(?:is(?: belonging to| assigned to| held by| owned by))? (.+?)(?: and has|,)',
        r'Application (?:\(.*?\) )?from US, (?:owned by|held by|assigned to|belonging to) (.+?)(?:,| with|$)',
        r'The US (?:application|patent filing|patent application) (?:\(.*?\) )?(?:is (?:assigned to|owned by|held by|belonging to)) (.+?)(?: and has|,|\. )',
        r'Patent (?:application|filing) (?:\(.*?\) )?(?:from US, )?(?:assigned to|held by|belonging to) (.+?)(?:,| with|$)',
        r'^(.+?) holds the US',
        r'^(.+?) holds the US'
    ]
    
    assignee = None
    for pattern in patterns:
        match = re.search(pattern, patents_info, re.IGNORECASE)
        if match:
            assignee = match.group(1).strip()
            break
    
    if assignee:
        assignees.append(assignee)
    else:
        assignees.append('UNKNOWN')

# Show samples
print('__RESULT__:')
print(json.dumps({
    'sample_patents_info': sample_patents_info[:20],
    'extracted_assignees': assignees[:20]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
