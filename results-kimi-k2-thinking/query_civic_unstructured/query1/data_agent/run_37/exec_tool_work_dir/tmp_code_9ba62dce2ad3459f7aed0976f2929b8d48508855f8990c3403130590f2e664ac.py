code = """import json
import re

# Load funding data
funding_path = var_functions.query_db_2
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic documents
civic_path = var_functions.query_db_5
with open(civic_path) as f:
    civic_docs = json.load(f)

print('Loaded data successfully. Funding records:', len(funding_data), 'Civic docs:', len(civic_docs))

# Step 1: Create map of high-funded projects
high_funded = {}
for rec in funding_data:
    amount = int(rec.get('Amount', 0))
    if amount > 50000:
        high_funded[rec.get('Project_Name', '').lower()] = {
            'project_name': rec.get('Project_Name'),
            'amount': amount
        }

print('High-funded projects map created with', len(high_funded), 'entries')

# Step 2: Process civic documents to find capital projects in design
matched_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip header/footer lines
        skip_phrases = ['project schedule', 'updates', 'discussion', 'recommended action', 'agenda', 'to:', 'prepared by:', 'date ', 'meeting date', 'subject', 'complete design', 'advertise', 'begin construction']
        if any(phrase in line.lower() for phrase in skip_phrases):
            continue
        
        # Look for capital project indicators near the line
        project_name = None
        has_design = False
        has_capital = False
        
        # Check current and next few lines context
        context_start = max(0, i-1)
        context_end = min(len(lines), i+8)
        context_text = ' '.join(lines[context_start:context_end]).lower()
        
        if 'design' in context_text:
            has_design = True
        if 'capital' in context_text or 'capital improvement' in context_text:
            has_capital = True
        
        # If we found indicators, check if this line contains a project name
        if has_design and has_capital and len(line) < 100 and not line.startswith('('):
            # Clean the project name
            clean_name = line.replace('•', '').replace('●', '').replace('*', '').strip()
            if clean_name and len(clean_name) > 5:
                # Check if this project is in our high-funded set
                clean_name_lower = clean_name.lower()
                if clean_name_lower in high_funded:
                    project_info = high_funded[clean_name_lower]
                    if not any(p['name'] == project_info['project_name'] for p in matched_projects):
                        matched_projects.append({
                            'name': project_info['project_name'],
                            'amount': project_info['amount']
                        })

print('Matched projects:', len(matched_projects))
for p in matched_projects[:3]:
    print('  -', p['name'], ': $', p['amount'])

result = json.dumps({'count': len(matched_projects), 'matches': matched_projects[:10]})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
