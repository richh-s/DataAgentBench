code = """import json

# Read the data from the files
civic_file = locals()['var_functions.query_db:0']
funding_file = locals()['var_functions.query_db:1']

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

# Extract capital design projects
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section boundaries
    design_keywords = ['Design', 'DESIGN']
    construction_keywords = ['Construction', 'Not Started', 'Disaster Recovery']
    
    design_start = -1
    for dk in design_keywords:
        pos = text.find(dk)
        if pos > 0 and pos < len(text) - 10:
            design_start = pos
            break
    
    if design_start > 0:
        design_section = text[design_start:design_start+2000]
        lines = design_section.split(chr(10))
        
        for line in lines:
            line = line.strip()
            if 10 <= len(line) <= 150:
                if not line.isupper() and line[0].isalnum():
                    if '•' not in line and 'Page' not in line:
                        if ':' not in line[:30]:
                            projects.append(line.strip())

# Remove duplicates
projects = list(set(projects))

# Build funding dictionary
funding_dict = {}
for item in funding:
    try:
        amt = int(str(item['Amount']).replace(',', ''))
        funding_dict[item['Project_Name']] = amt
    except:
        pass

# Count projects with funding > 50000
count = 0
matched = []
for proj in projects:
    if proj in funding_dict and funding_dict[proj] > 50000:
        count += 1
        matched.append(proj)

print('__RESULT__:')
print(json.dumps({'count': count, 'sample_matched': matched[:10]}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json', 'var_functions.execute_python:14': {'available_variables': ['var_functions.query_db:0', 'var_functions.query_db:1', '__builtins__', 'json']}, 'var_functions.execute_python:18': {'civic_docs_length': 38, 'funding_length': 38, 'civic_docs_sample': 'fi'}, 'var_functions.execute_python:20': {'civic_var_type': "<class 'str'>", 'funding_var_type': "<class 'str'>", 'civic_var_preview': 'file_storage/functions.query_db:0.json', 'funding_var_preview': 'file_storage/functions.query_db:1.json'}}

exec(code, env_args)
