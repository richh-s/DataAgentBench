code = """import json

# Load the funding data
funding_file = open('var_functions.query_db:0', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Load the civic documents
civic_file = open('var_functions.query_db:2', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

# Create dictionary of funded projects with lower case names as keys
funded_lookup = {}
for record in funding_data:
    project_name = record['Project_Name'].strip().lower()
    funded_lookup[project_name] = int(record['Amount'])

# Extract project names from design section of civic documents
design_project_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    upper_text = text.upper()
    
    if 'CAPITAL IMPROVEMENT PROJECTS (DESIGN)' in upper_text:
        start = upper_text.index('CAPITAL IMPROVEMENT PROJECTS (DESIGN)')
        end = upper_text.find('CAPITAL IMPROVEMENT PROJECTS (CONSTRUCTION)', start)
        if end == -1:
            end = len(text)
        
        section = text[start:end]
        for line in section.split('\n'):
            line = line.strip()
            if line and len(line) > 5 and 'Updates:' not in line and 'Project Schedule:' not in line:
                if 'Capital Improvement' not in line and 'Page' not in line and len(line) < 200:
                    design_project_names.append(line.lower())

# Count unique projects with funding > $50,000
unique_design = list(set(design_project_names))
count = 0
for proj in unique_design:
    if proj in funded_lookup and funded_lookup[proj] > 50000:
        count = count + 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_docs': 5}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
