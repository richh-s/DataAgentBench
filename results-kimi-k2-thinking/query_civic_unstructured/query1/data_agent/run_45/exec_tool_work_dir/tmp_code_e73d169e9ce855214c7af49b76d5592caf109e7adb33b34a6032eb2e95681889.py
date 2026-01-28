code = """import json
import re

# Load funding data
funding_file = open(var_functions.query_db:2, 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Create funding map for projects > $50,000
funding_map = {}
for record in funding_data:
    amount = float(record.get('Amount', 0))
    if amount > 50000:
        name = record['Project_Name']
        clean_name = re.sub(r'\s*\([^)]*\)\s*$', '', name).strip()
        funding_map[name] = amount
        funding_map[clean_name] = amount

# Load civic documents
civic_file = open(var_functions.query_db:6, 'r')
civic_docs = json.load(civic_file)
civic_file.close()

# Find capital design projects and match with funding
count = 0

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Get design section
    remaining = text[design_start:]
    construction_start = remaining.find('Capital Improvement Projects (Construction)')
    if construction_start > 0:
        design_section = remaining[:construction_start]
    else:
        design_section = remaining
    
    # Extract lines that look like project names
    for line in design_section.split('\n'):
        line = line.strip()
        if len(line) > 15:
            # Skip meta lines
            skip_words = ['RECOMMENDED', 'ACTION', 'DISCUSSION', 'SUBJECT', 'PAGE', 'AGENDA', 'UPDATES:', 'SCHEDULE:']
            if any(word in line.upper() for word in skip_words):
                continue
            
            # Skip disaster projects
            if any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'fire']):
                continue
            
            # Check if project has funding > $50k
            clean_line = re.sub(r'\s*\([^)]*\)\s*$', '', line).strip()
            if line in funding_map or clean_line in funding_map:
                count += 1

result = {'count': count}
print('____RESULT____')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
