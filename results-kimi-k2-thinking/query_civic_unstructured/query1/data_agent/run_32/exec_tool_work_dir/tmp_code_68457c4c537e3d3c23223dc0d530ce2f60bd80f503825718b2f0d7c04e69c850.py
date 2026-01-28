code = """import json
import re

# Read the civic documents data
civic_docs_path = var_functions.query_db:5
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
funding_path = var_functions.query_db:2
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Create a dictionary of funding amounts for easy lookup
funding_dict = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if amount > 50000:
        funding_dict[project_name] = amount

# Parse civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for capital design projects
    if 'Capital Improvement Projects (Design)' in text:
        sections = text.split('Capital Improvement Projects (Design)')
        if len(sections) > 1:
            design_section = sections[1].split('Capital Improvement Projects (Construction)')[0]
            
            lines = design_section.split('\n')
            for line in lines:
                line = line.strip()
                
                if len(line) < 5:
                    continue
                
                # Skip scheduling/project management lines
                if 'Complete Design:' in line or 'Advertise:' in line or 'Begin Construction:' in line:
                    continue
                if 'Final Design:' in line or 'Project Schedule:' in line or 'Updates:' in line:
                    continue
                if line.startswith('cid:') or line.startswith('(cid:'):
                    continue
                if line.startswith('●') or line.startswith('•'):
                    continue
                if 'Project is' in line:
                    continue
                
                # Clean up line
                clean_line = re.sub(r'\(cid:\d+\)', '', line).strip()
                
                if clean_line in funding_dict:
                    if clean_line not in [p['Project_Name'] for p in projects]:
                        projects.append({'Project_Name': clean_line, 'type': 'capital', 'status': 'design', 'amount': funding_dict[clean_line]})

# Search more broadly for capital design projects
for project_name in funding_dict.keys():
    if project_name in [p['Project_Name'] for p in projects]:
        continue
    
    for doc in civic_docs:
        text = doc.get('text', '')
        if project_name in text:
            idx = text.find(project_name)
            if idx >= 0:
                context_start = max(0, idx - 300)
                context_end = min(len(text), idx + len(project_name) + 300)
                context = text[context_start:context_end].lower()
                
                design_terms = ['design', 'complete design', 'final design']
                has_design = any(term in context for term in design_terms)
                is_capital = 'fema' not in project_name.lower() and 'disaster' not in context
                
                if has_design and is_capital:
                    projects.append({'Project_Name': project_name, 'type': 'capital', 'status': 'design', 'amount': funding_dict[project_name]})
                    break

count = len(projects)

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
