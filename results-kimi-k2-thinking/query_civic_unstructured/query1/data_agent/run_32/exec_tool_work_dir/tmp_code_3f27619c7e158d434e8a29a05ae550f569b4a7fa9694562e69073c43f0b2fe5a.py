code = """import json
import re

civic_docs_path = var_functions.query_db:5
funding_path = var_functions.query_db:2

# Load data
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Build funding dict with 50k+ projects
funding_dict = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if amount > 50000:
        funding_dict[project_name] = amount

design_projects = []
found_names = set()

# Look in Design sections
for doc in civic_docs:
    text = doc.get('text', '')
    
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            lines = [ln.strip() for ln in design_section.split('\n')]
            
            for line in lines:
                if len(line) < 5:
                    continue
                
                skip_patterns = ['Complete Design:', 'Advertise:', 'Begin Construction:', 
                               'Final Design:', 'Project Schedule:', 'Updates:']
                if any(p in line for p in skip_patterns):
                    continue
                
                if line.startswith('cid:') or line.startswith('(cid:') or line.startswith('●'):
                    continue
                
                if 'Project is' in line:
                    continue
                
                # Clean
                clean_line = re.sub(r'\(cid:\d+\)', '', line).strip()
                
                if clean_line in funding_dict and clean_line not in found_names:
                    design_projects.append(clean_line)
                    found_names.add(clean_line)

# Broader search
for project_name in funding_dict:
    if project_name in found_names:
        continue
    
    for doc in civic_docs:
        text = doc.get('text', '')
        if project_name in text:
            idx = text.find(project_name)
            context = text[max(0, idx-300):min(len(text), idx+len(project_name)+300)].lower()
            
            has_design = 'design' in context
            is_capital = 'fema' not in project_name.lower() and 'disaster' not in context
            
            if has_design and is_capital:
                design_projects.append(project_name)
                found_names.add(project_name)
                break

count = len(design_projects)
print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
