code = """import json

# Read the full civic_docs result
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    documents = json.load(f)

# Extract park-related projects
park_projects = []

for doc in documents:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if 'park' in line.lower() and len(line) < 150:
            skip = False
            headers = ['capital improvement', 'disaster recovery', 'status report', 'discussion', 'recommended action']
            for h in headers:
                if h in line.lower():
                    skip = True
            if line.startswith('(') or not line:
                skip = True
            
            if not skip:
                proj = {'name': line, 'completed_2022': False}
                
                # Look ahead for completion info
                for j in range(i, min(len(lines), i+15)):
                    if 'completed' in lines[j].lower() and '2022' in lines[j]:
                        proj['completed_2022'] = True
                        break
                
                park_projects.append(proj)

# Deduplicate
unique = {p['name']: p for p in park_projects}
park_list = list(unique.values())

completed = [p for p in park_list if p['completed_2022']]

print('__RESULT__:')
print(json.dumps({
    'total_park': len(park_list),
    'completed_2022': len(completed),
    'names': [p['name'] for p in completed]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
