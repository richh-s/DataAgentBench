code = """import json

# Load civic documents file
civic_file = open(var_functions.query_db:60)
civic_docs = json.load(civic_file)
civic_file.close()

# Load funding file
fund_file = open(var_functions.query_db:48)
funding = json.load(fund_file)
fund_file.close()

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Look for park-related project names
        if line.find('Park') >= 0 and len(line) > 10:
            # Skip headers
            if line.find('Subject') >= 0 or line.find('Page') >= 0 or line.find('Item') >= 0:
                continue
            if line.startswith('('):
                continue
            
            # Check following lines for completion in 2022
            next_section = '\n'.join(lines[i:i+15])
            if next_section.lower().find('completed') >= 0 and next_section.find('2022') >= 0:
                park_projects.append(line)

# Remove duplicates
unique_parks = list(set(park_projects))

# Find funding matches
total_funding = 0
matches = []

for proj in unique_parks:
    proj_lower = proj.lower()
    for rec in funding:
        name = rec.get('Project_Name', '')
        if proj_lower in name.lower():
            amount = int(rec.get('Amount', 0))
            total_funding += amount
            matches.append([proj, name, amount])

result = {'count': len(unique_parks), 'total_funding': total_funding, 'projects': unique_parks, 'matches': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}, 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
