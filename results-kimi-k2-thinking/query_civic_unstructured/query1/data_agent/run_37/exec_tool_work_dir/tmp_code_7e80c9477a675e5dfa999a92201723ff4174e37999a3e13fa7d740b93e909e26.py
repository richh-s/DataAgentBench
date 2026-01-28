code = """import json
import re

# Load funding data from file path
with open('file_storage/execute_python_2/query_db_2.json', 'r') as f:
    funding_records = json.load(f)

# Load civic documents from file path
with open('file_storage/execute_python_5/query_db_5.json', 'r') as f:
    civic_docs = json.load(f)

# Step 1: Create funding lookup for projects > $50,000
funding_lookup = {}
for rec in funding_records:
    amount = int(rec.get('Amount', 0))
    if amount > 50000:
        project_name = rec.get('Project_Name', '')
        funding_lookup[project_name] = {
            'amount': amount,
            'source': rec.get('Funding_Source')
        }

# Step 2: Analyze civic documents for capital design projects
all_text = ''
for doc in civic_docs:
    all_text += ' ' + doc.get('text', '')

# Find projects mentioned in the text
capital_design_projects = []
words = all_text.split()

i = 0
while i < len(words):
    # Look for sequences of words that might be project names
    possible_name = []
    j = i
    
    # Build potential project name (up to 10 words or until punctuation)
    while j < len(words) and j < i + 10:
        word = words[j].strip('\n\r\t.,;:()')
        if word in ['Project', 'Updates', 'Schedule', 'Discussion']:
            break
        possible_name.append(word)
        j += 1
        
        if j < len(words) and (words[j-1].endswith(':') or words[j-1].endswith('.')):
            break
    
    if len(possible_name) >= 2:
        candidate_name = ' '.join(possible_name)
        
        # Check if this candidate is a funded project with capital and design status
        if candidate_name in funding_lookup:
            # Look for capital and design context
            context_start = max(0, i*10)  # approximate char position
            context_end = min(len(all_text), context_start + 500)
            context = all_text[context_start:context_end].lower()
            
            if 'capital' in context and 'design' in context:
                if not any(p['project_name'] == candidate_name for p in capital_design_projects):
                    capital_design_projects.append({
                        'project_name': candidate_name,
                        'funding_amount': funding_lookup[candidate_name]['amount']
                    })
    
    i += 1

print('Found', len(capital_design_projects), 'capital design projects with >$50k funding')
print('__RESULT__:')
print(json.dumps({'total_count': len(capital_design_projects), 'sample_projects': capital_design_projects[:5]}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
