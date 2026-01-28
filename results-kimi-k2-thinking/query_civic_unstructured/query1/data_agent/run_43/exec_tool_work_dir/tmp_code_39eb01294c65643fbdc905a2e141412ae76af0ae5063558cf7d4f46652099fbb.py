code = """import json
import os

# Access the stored file paths using locals()
# The keys are based on the tool call IDs provided
funding_path = locals()['var_functions.query_db:60']
civic_path = locals()['var_functions.query_db:6']

print('Funding path:', funding_path)
print('Civic path:', civic_path)

# Load funding data (already filtered for Amount > 50000)
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(funding_data), 'funding records')
print('Loaded', len(civic_docs), 'civic documents')

# Build funding map: project name -> amount
funding_map = {}
for item in funding_data:
    project_name = item['Project_Name']
    amount = int(item['Amount'])
    funding_map[project_name] = amount

# Extract capital projects with design status
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    text_lower = text.lower()
    # Look for capital improvement projects in design phase
    if 'capital improvement projects' in text_lower and 'design' in text_lower:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) < 5:
                continue
            
            # Skip obvious non-project lines
            skip_patterns = ['page', 'schedule', 'updates', 'project description', 'staff is', 'city will', 'consultant', 'to:', 'item']
            if any(pattern in line.lower() for pattern in skip_patterns):
                continue
            
            if line.startswith('202') or line.startswith('Item'):
                continue
            
            # Check context for design status
            pos = text.find(line)
            if pos >= 0:
                lookahead_end = min(pos + 400, len(text))
                context = text[pos:lookahead_end]
                if 'Design' in context:
                    clean_name = line.replace('•', '').replace('○', '').strip()
                    if 8 < len(clean_name) < 200:
                        design_projects.add(clean_name)

# Count design projects with matching funding > 50000
count = 0
for design_proj in design_projects:
    for funded_name, amount in funding_map.items():
        # Check name similarity
        d_lower = design_proj.lower()
        f_lower = funded_name.lower()
        
        if (d_lower in f_lower) or (f_lower in d_lower):
            # Check length similarity to reduce false positives
            if abs(len(design_proj) - len(funded_name)) < 40:
                count += 1
                break

result = {'count': count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
