code = """import json

# Access funding data that is already filtered for Amount > 50000
funding_records = var_functions.query_db:90
funding_names = [item['Project_Name'] for item in funding_records]

# Access civic documents
civic_documents = var_functions.query_db:6

# Extract design capital projects from documents
design_projects = set()

for doc in civic_documents:
    text = doc.get('text', '')
    
    # Check for capital improvement projects with design status
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if not line or len(line) < 5:
                continue
            
            # Skip non-project lines
            if line.startswith('Page') or 'Schedule:' in line or 'Updates:' in line:
                continue
            if line.startswith('202') or line.startswith('Item '):
                continue
                
            # Check context for design status
            pos = text.find(line)
            if pos >= 0:
                context = text[pos:pos+400]
                if 'Design' in context:
                    # Clean project name
                    clean = line.replace('•', '').replace('○', '').strip()
                    if 8 < len(clean) < 200:
                        design_projects.add(clean)

# Count design projects with funding > 50000
count = 0
for proj in design_projects:
    proj_lower = proj.lower()
    for funded in funding_names:
        funded_lower = funded.lower()
        # Check name similarity
        if proj_lower in funded_lower or funded_lower in proj_lower:
            if abs(len(proj) - len(funded)) < 40:
                count += 1
                break

result = dict(count=count)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json', 'var_functions.execute_python:106': {'count': 7}}

exec(code, env_args)
