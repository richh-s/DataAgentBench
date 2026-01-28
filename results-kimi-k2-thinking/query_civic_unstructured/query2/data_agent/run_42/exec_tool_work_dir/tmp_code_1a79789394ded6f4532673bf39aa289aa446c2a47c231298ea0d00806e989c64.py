code = """import json

# Read the funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Read civic documents
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    documents = json.load(f)

# Calculate total funding for all park projects
park_total = 0
park_names = []

for record in funding_records:
    name = record.get('Project_Name', '')
    if 'park' in name.lower():
        park_total += int(record.get('Amount', 0))
        park_names.append(name)

# Find park projects completed in 2022
completed_2022 = []

for doc in documents:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Check if line contains park project name  
        if 'park' in line.lower() and len(line) < 150:
            # Skip section headers and metadata
            skip_words = ['capital improvement', 'disaster recovery', 'status report']
            should_skip = False
            for word in skip_words:
                if word in line.lower():
                    should_skip = True
                    break
            
            if line.startswith('(') or line.startswith('cid:'):
                should_skip = True
                
            if not should_skip and line:
                # Check surrounding context for completion in 2022
                for j in range(max(0, i-5), min(len(lines), i+10)):
                    context = lines[j]
                    lower_context = context.lower()
                    if 'completed' in lower_context and '2022' in context:
                        completed_2022.append(line)
                        break

# Remove duplicates
unique_completed = list(set(completed_2022))
unique_park_names = list(set(park_names))

result = {
    'all_park_projects_found': len(unique_park_names),
    'all_park_funding_total': park_total,
    'completed_in_2022_count': len(unique_completed)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
