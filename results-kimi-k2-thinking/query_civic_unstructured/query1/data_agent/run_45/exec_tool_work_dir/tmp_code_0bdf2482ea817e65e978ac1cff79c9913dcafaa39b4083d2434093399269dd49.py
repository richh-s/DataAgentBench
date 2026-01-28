code = """import json
import re

# Load funding data
with open('/tmp/tmp_results/query_db_2.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('/tmp/tmp_results/query_db_6.json', 'r') as f:
    civic_documents = json.load(f)

# Create funding map for projects > $50,000
funding_map = {}
for record in funding_data:
    amount = float(record.get('Amount', 0))
    if amount > 50000:
        name = record['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amount
        funding_map[clean_name] = amount

# Extract capital design projects from civic documents and count matches
count = 0
matched_projects = []

for doc in civic_documents:
    text = doc.get('text', '')
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        
        # Track section
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
        elif 'Capital Improvement Projects (Construction)' in line:
            in_design_section = False
            continue
        
        if in_design_section and line and len(line) > 15:
            # Skip disaster projects
            if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                continue
            
            # Skip meta lines
            if any(word in line.upper() for word in ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA']):
                continue
            
            # Skip section headers and bullet points
            if any(phrase in line for phrase in ['Updates:', 'Schedule:', 'Capital Improvement Projects']):
                continue
            
            if line.startswith('(') or line.startswith('\\u2022'):
                continue
            
            # Check if project matches funding
            clean_line = re.sub(r'\s*\([^)]*\)\s*$', '', line).strip()
            if line in funding_map or clean_line in funding_map:
                count += 1
                amount = funding_map.get(line) or funding_map.get(clean_line, 0)
                matched_projects.append({'project': line, 'funding': amount})

print('Matches found:')
for p in matched_projects:
    print(f"- {p['project']}: ${p['funding']}")

result = {'count': count, 'projects': matched_projects}
print('\\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
