code = """import json

f_path = locals()['var_functions.execute_python:2']
c_path = locals()['var_functions.query_db:8']

with open(f_path, 'r') as f:
    funding_data = json.load(f)

with open(c_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for > $50,000
funding_lookup = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        name = item['Project_Name'].strip()
        funding_lookup[name] = amount

# Extract capital design projects systematically
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Find sections about capital design projects
    sections = text.split('\n\n')
    in_design_section = False
    
    for section in sections:
        section = section.strip()
        
        # Check if this is a design section
        if 'Capital Improvement Projects' in section and 'Design' in section:
            in_design_section = True
            
            # Extract lines that are likely project names
            lines = section.split('\n')
            for line in lines:
                line = line.strip()
                
                # Skip empty lines, headers, metadata
                if not line or len(line) < 5:
                    continue
                if line.startswith('Capital Improvement Projects'):
                    continue
                if 'Updates:' in line or 'Schedule:' in line:
                    continue
                if line.startswith('(') or line.startswith('Page') or line.startswith('Agenda'):
                    continue
                if line.startswith('Staff') or line.startswith('City'):
                    continue
                if any(season in line for season in ['Spring', 'Summer', 'Fall', 'Winter']):
                    continue
                if 'COMPLETE DESIGN' in line.upper():
                    continue
                
                # Clean project name (remove parenthetical suffixes)
                clean_name = line.split('(')[0].strip()
                if clean_name and len(clean_name) > 5:
                    design_projects.add(clean_name)

# Match design projects with funding > $50,000
matched = 0
for design in design_projects:
    for fund_name in funding_lookup.keys():
        if design == fund_name or fund_name.startswith(design + ' ') or fund_name.startswith(design + '('):
            matched += 1
            break

result = str(matched)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:82': [{'count': '276'}], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:96': 7, 'var_functions.execute_python:102': 25}

exec(code, env_args)
