code = """import json, re

# Read the funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Read civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    documents = json.load(f)

# Extract park projects from funding data
park_funding_records = []
total_funding = 0

for record in funding_records:
    project_name = record.get('Project_Name', '')
    if 'park' in project_name.lower():
        amount = int(record.get('Amount', 0))
        park_funding_records.append({
            'name': project_name,
            'amount': amount
        })
        total_funding += amount

# Search civic documents for completion info specific to 2022
completed_2022_projects = []

for doc in documents:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Look for completions in 2022 with park references
    if '2022' in text and 'completed' in lower_text and 'park' in lower_text:
        # Extract relevant lines
        lines = text.split('\n')
        for i, line in enumerate(lines):
            ln = line.strip()
            # Look for project names containing park
            if 'park' in ln.lower() and len(ln) < 150:
                # Skip section headers
                if any(x in ln.lower() for x in ['capital improvement', 'disaster recovery', 'status report', 'discussion:', 'recommended action']):
                    continue
                if ln.startswith('(') or ln.startswith('cid:'):
                    continue
                
                # Check if this project was completed in 2022
                nearby_text = ' '.join(lines[i:min(i+8, len(lines))])
                if 'completed' in nearby_text.lower() and '2022' in nearby_text:
                    completed_2022_projects.append(ln)

result = {
    'park_funding_total_all': total_funding,
    'park_projects_found_in_funding': len(park_funding_records),
    'projects_completed_2022_count': len(completed_2022_projects),
    'completed_projects': completed_2022_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
