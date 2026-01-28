code = """import json

# Load civic documents
civic_docs_path = var_functions.query_db:60
civic_docs = json.load(open(civic_docs_path))

# Load funding data  
funding_path = var_functions.query_db:48
funding = json.load(open(funding_path))

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if this document mentions parks, completion, and 2022
    if 'Park' in text and '2022' in text and ('completed' in text.lower() or 'completion' in text.lower()):
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            
            # Look for project names with Park
            if 'Park' in line and len(line) > 10:
                # Skip header lines
                if 'Subject' in line or 'Page' in line or 'Item' in line or '\n' in line:
                    continue
                if line.startswith('('):
                    continue
                
                # Check surrounding context for completion
                start = max(0, i-2)
                end = min(len(lines), i+10)
                context = ' '.join(lines[start:end])
                
                if 'completed' in context.lower() and '2022' in context:
                    park_projects.append(line)

# Remove duplicates
unique_projects = list(set(park_projects))

# Match with funding data
total_funding = 0
matches = []

for proj in unique_projects:
    for rec in funding:
        name = rec.get('Project_Name', '')
        # Simple substring match
        if proj.lower() in name.lower():
            total_funding += int(rec.get('Amount', 0))
            matches.append([proj, name, int(rec.get('Amount', 0))])

# Format output
result = {
    'project_count': len(unique_projects),
    'total_funding': total_funding,
    'projects': unique_projects,
    'funding_matches': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
