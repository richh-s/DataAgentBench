code = """import json
import re

# Load funding data  
funding_path = locals()['var_functions.execute_python:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:8']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Build funding lookup for projects > $50,000
funding_projects = {}
for item in funding_data:
    amount = int(item['Amount'])
    if amount > 50000:
        name = item['Project_Name'].strip()
        funding_projects[name] = amount

# Extract capital design projects from documents
all_design = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find capital design sections
    design_sections = re.findall(r'Capital Improvement Projects.*?\(Design\)(.*?)(?=\n\s*\n[A-Z]|\Z)', text, re.S)
    
    for section in design_sections:
        # Extract lines that look like project names
        lines = section.split('\n')
        for line in lines:
            line = line.strip()
            if not line or len(line) < 5:
                continue
                
            # Skip metadata
            if line.startswith('(') or 'cid:' in line:
                continue
            if any(word in line for word in ['Updates:', 'Schedule:', 'RECOMMENDED', 'DISCUSSION', 'Page', 'Agenda']):
                continue
            if any(phase in line for phase in ['Spring', 'Summer', 'Fall', 'Winter']):
                continue
            if any(prefix in line for prefix in ['Complete Design:', 'Advertise:', 'Begin Construction:']):
                continue
            if line.startswith('Staff') or line.startswith('City'):
                continue
                
            # Clean name and add
            clean_name = re.sub(r'\s*\([^)]*\)$', '', line)
            if clean_name:
                all_design.append(clean_name.strip())

# Remove duplicates
unique_design = list(set(all_design))

# Match with funding data
design_capital_funded = []
for design_name in unique_design:
    for fund_name in funding_projects.keys():
        if design_name == fund_proj or fund_name.startswith(design_name + ' ') or fund_name.startswith(design_name + '('):
            design_capital_funded.append(design_name)
            break

count = len(design_capital_funded)
print('__RESULT__:', count)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': 'file_storage/functions.execute_python:2.json', 'var_functions.list_db:5': ['civic_docs'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
