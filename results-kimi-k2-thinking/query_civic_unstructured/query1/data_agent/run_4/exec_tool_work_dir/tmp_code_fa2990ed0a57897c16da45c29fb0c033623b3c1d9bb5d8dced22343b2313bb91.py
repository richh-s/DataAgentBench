code = """import json

# Load data
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

civic_path = locals()['var_functions.query_db:8']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup for >$50,000
funding_dict = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        funding_dict[item['Project_Name'].strip()] = amount

# Extract project names with design status - simpler approach
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects' in text and 'Design' in text:
        lines = text.split('\n')
        in_section = False
        
        for line in lines:
            line = line.strip()
            
            if 'Capital Improvement Projects' in line and 'Design' in line:
                in_section = True
                continue
                
            if in_section:
                if line.startswith('Capital') and ('Construction' in line or 'Not Started' in line):
                    break
                if line.startswith('DISASTER'):
                    break
                    
                if line and len(line) > 5 and not line.startswith('(') and 'Updates:' not in line and 'Schedule:' not in line and 'Page' not in line and 'cid:' not in line and not line.startswith('Staff') and not line.startswith('City'):
                    if 'Spring' not in line and 'Summer' not in line and 'Fall' not in line and 'Winter' not in line:
                        if 'COMPLETE DESIGN' not in line.upper():
                            design_projects.append(line)

# Remove duplicates
design_projects = list(set(design_projects))

# Match with funding data using simple string matching
matches = 0
for design in design_projects:
    for fund in funding_dict.keys():
        if design == fund:
            matches += 1
            break
        elif fund.startswith(design + ' '):
            matches += 1
            break
        elif fund.startswith(design + '('):
            matches += 1
            break

print('__RESULT__:', matches)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
