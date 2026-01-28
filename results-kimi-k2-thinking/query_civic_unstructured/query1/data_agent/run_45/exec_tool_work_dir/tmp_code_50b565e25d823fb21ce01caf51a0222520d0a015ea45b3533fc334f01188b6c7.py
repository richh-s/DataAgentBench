code = """import json, re, sys

# Load data from the stored file paths
funding_file = var_functions.query_db:2
civic_file = var_functions.query_db:6

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Build funding map for projects > $50,000
funding_map = {}
for record in funding_data:
    amount = float(record.get('Amount', 0))
    if amount > 50000:
        name = record['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amount
        funding_map[clean_name] = amount

# Extract capital design projects from civic documents and match with funding
count = 0
matched_projects = []

for doc in civic_docs:
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
            if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                continue
            
            # Skip meta lines
            meta_words = ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA']
            if any(word in line.upper() for word in meta_words):
                continue
            
            # Skip section headers and bullet points
            if any(phrase in line for phrase in ['Updates:', 'Schedule:', 'Capital Improvement']):
                continue
            
            if line.startswith('/') or line.startswith('\'):
                continue
            
            # Clean and check if project has funding
            clean_line = re.sub(r'\s*\([^)]*\)\s*$', '', line).strip()
            if line in funding_map or clean_line in funding_map:
                count += 1
                amount = funding_map.get(line) or funding_map.get(clean_line, 0)
                matched_projects.append({'project': line, 'funding': amount})

result = {'count': count, 'projects': matched_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
