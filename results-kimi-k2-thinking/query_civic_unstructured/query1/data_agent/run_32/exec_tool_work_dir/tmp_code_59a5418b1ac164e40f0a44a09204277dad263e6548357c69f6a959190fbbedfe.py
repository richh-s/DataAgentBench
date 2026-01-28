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

# Find capital design projects
design_projects = []
project_names_found = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look specifically in Design section
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_part = parts[1].split('Capital Improvement Projects (Construction)')[0]
            lines = design_part.split('\n')
            
            for line in lines:
                clean_line = line.strip()
                
                # Skip empty and management lines
                if len(clean_line) < 5:
                    continue
                if any(skip in clean_line for skip in ['Complete Design:', 'Advertise:', 'Begin Construction:']):
                    continue
                if any(skip in clean_line for skip in ['Final Design:', 'Project Schedule:', 'Updates:']):
                    continue
                if clean_line.startswith('cid:') or clean_line.startswith('(cid:'):
                    continue
                if clean_line.startswith('●'):
                    continue
                if clean_line.startswith('•'):
                    continue
                if 'Project is' in clean_line:
                    continue
                
                # Check if project name has funding
                if clean_line in funding_dict:
                    if clean_line not in project_names_found:
                        design_projects.append({
                            'name': clean_line,
                            'amount': funding_dict[clean_line]
                        })
                        project_names_found.add(clean_line)

# Extended search for missed projects
for project_name in funding_dict:
    if project_name in project_names_found:
        continue
    
    for doc in civic_docs:
        text = doc.get('text', '')
        if project_name in text:
            idx = text.find(project_name)
            context_start = max(0, idx - 300)
            context_end = min(len(text), idx + len(project_name) + 300)
            context = text[context_start:context_end].lower()
            
            design_terms = ['design', 'complete design', 'final design']
            has_design = any(term in context for term in design_terms)
            is_capital = 'fema' not in project_name.lower() and 'disaster' not in context
            
            if has_design and is_capital:
                design_projects.append({
                    'name': project_name,
                    'amount': funding_dict[project_name]
                })
                project_names_found.add(project_name)
                break

print('__RESULT__:')
print(json.dumps(len(design_projects)))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
