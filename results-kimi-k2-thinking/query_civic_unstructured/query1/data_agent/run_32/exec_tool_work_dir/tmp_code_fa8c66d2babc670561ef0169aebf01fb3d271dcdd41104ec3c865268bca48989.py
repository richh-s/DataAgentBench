code = """import json
import re

civic_docs_path = var_functions.query_db:5
funding_path = var_functions.query_db:2

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funding_dict = {}
for rec in funding_records:
    name = rec.get('Project_Name', '')
    amount = int(rec.get('Amount', 0))
    if amount > 50000:
        funding_dict[name] = amount

design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            lines = section.split('\n')
            for line in lines:
                clean_line = line.strip()
                if len(clean_line) < 5:
                    continue
                
                skip_found = False
                skip_patterns = ['Complete Design:', 'Advertise:', 'Begin Construction:', 'Final Design:', 'Project Schedule:', 'Updates:']
                for pattern in skip_patterns:
                    if pattern in clean_line:
                        skip_found = True
                        break
                
                if skip_found:
                    continue
                
                if clean_line.startswith('cid:') or clean_line.startswith('(cid:'):
                    continue
                if 'Project is' in clean_line:
                    continue
                
                clean_line = re.sub(r'\(cid:\d+\)', '', clean_line).strip()
                
                if clean_line and clean_line in funding_dict:
                    design_projects.add(clean_line)

for project_name in funding_dict:
    if project_name in design_projects:
        continue
    
    for doc in civic_docs:
        text = doc.get('text', '')
        if project_name in text:
            idx = text.find(project_name)
            snippet = text[max(0, idx-300):min(len(text), idx+len(project_name)+300)].lower()
            
            if 'design' in snippet and 'fema' not in project_name.lower():
                design_projects.add(project_name)
                break

count = len(design_projects)
print('__RESULT__:')
print(str(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
