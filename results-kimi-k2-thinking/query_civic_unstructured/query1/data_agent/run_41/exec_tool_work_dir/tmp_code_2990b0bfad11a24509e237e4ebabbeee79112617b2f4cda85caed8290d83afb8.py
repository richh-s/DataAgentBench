code = """import json, re

funding_data = locals()['var_functions.query_db:32']
civic_path = locals()['var_functions.query_db:54']

with open(civic_path) as f:
    civic_data = json.load(f)

funding_lookup = {}
for item in funding_data:
    name = item['Project_Name']
    amount = int(item['Amount'])
    funding_lookup[name] = amount
    base = name.split(' (')[0]
    funding_lookup[base] = amount

design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    
    # Find the design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start > 0:
        # Get a reasonable chunk after this header
        design_text = text[design_start+100:design_start+4000]
        
        # Extract project names (look for patterns)
        # Find lines that are likely project names
        for match in re.finditer(r'\n([A-Z][a-zA-Z0-9 &\-\.]+)\n', design_text):
            project_name = match.group(1).strip()
            if len(project_name) > 10 and 'Updates' not in project_name:
                # Clean the name
                clean_name = project_name.rstrip('.')
                
                # Check if in funding lookup and amount > 50000
                if clean_name in funding_lookup:
                    amount = funding_lookup[clean_name]
                    if amount > 50000:
                        design_projects.add((clean_name, amount))

result = len(design_projects)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.list_db:52': ['civic_docs'], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
