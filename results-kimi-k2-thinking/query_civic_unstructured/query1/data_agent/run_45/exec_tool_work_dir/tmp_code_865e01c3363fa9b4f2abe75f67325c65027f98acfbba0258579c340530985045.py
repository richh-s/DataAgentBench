code = """import json, re

# Load the funding data
funding_file_path = var_functions.query_db:2
funding_file = open(funding_file_path, 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Load the civic documents
civic_file_path = var_functions.query_db:6
civic_file = open(civic_file_path, 'r')
civic_data = json.load(civic_file)
civic_file.close()

# Create funding map for projects > $50,000
funding_map = {}
for record in funding_data:
    amount = float(record.get('Amount', 0))
    if amount > 50000:
        name = record['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amount
        funding_map[clean_name] = amount

# Extract capital design projects from civic documents
capital_design_projects = set()

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
        elif 'Capital Improvement Projects (Construction)' in line:
            in_design_section = False
        
        if in_design_section and line and len(line) > 15:
            # Skip disaster projects
            if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line or 'fire' in line:
                continue
            
            # Skip meta lines
            meta_words = ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA', 'UPDATES:', 'SCHEDULE:']
            if any(word in line.upper() for word in meta_words):
                continue
            
            if line.startswith('('):
                continue
            
            capital_design_projects.add(line)

# Count matches with funding > $50,000
count = 0
for project in capital_design_projects:
    clean_project = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
    
    if project in funding_map or clean_project in funding_map:
        count += 1

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
