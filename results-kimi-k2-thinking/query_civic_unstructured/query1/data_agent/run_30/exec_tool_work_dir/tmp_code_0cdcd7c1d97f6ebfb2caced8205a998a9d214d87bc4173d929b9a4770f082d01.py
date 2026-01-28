code = """import json
import re

# Access data from storage
funding_result = var_functions.query_db:0
civic_result = var_functions.query_db:2

# Load funding data
if isinstance(funding_result, str) and funding_result.endswith('.json'):
    with open(funding_result, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_result

# Load civic docs data  
if isinstance(civic_result, str) and civic_result.endswith('.json'):
    with open(civic_result, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_result

print('Funding records loaded:', len(funding_records))
print('Civic documents loaded:', len(civic_docs))

# Find capital design projects in civic docs
capital_design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check if document has capital improvement projects in design phase
    if 'capital improvement projects' in text_lower and 'design' in text_lower:
        project_keywords = ['road', 'avenue', 'drive', 'park', 'drain', 'storm', 'bridge', 'walkway', 'trail', 'sewer', 'water', 'traffic', 'signal', 'sign', 'median', 'crosswalk', 'improvements', 'repairs']
        
        # Split into lines
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            
            if len(line) < 10:
                continue
            
            # Skip administrative lines
            skip_terms = ['updates', 'schedule', 'staff', 'city council', 'consultant', 'discussion', 'page', 'complete design', 'advertise', 'construction']
            if any(term in line.lower() for term in skip_terms):
                continue
            
            # Check if this looks like a project name
            if any(keyword in line.lower() for keyword in project_keywords):
                capital_design_projects.append(line)

# Remove duplicates
capital_design_projects = list(set(capital_design_projects))
print('Potential capital design projects found:', len(capital_design_projects))

# Match with funding data
matched_count = 0
matched_details = []

for proj in capital_design_projects:
    proj_lower = proj.lower()
    
    for fund in funding_records:
        amount = int(fund['Amount'])
        
        if amount <= 50000:
            continue
            
        fund_name = fund['Project_Name']
        fund_lower = fund_name.lower()
        
        # Check for match
        if proj_lower == fund_lower or proj_lower in fund_lower or fund_lower in proj_lower:
            matched_count += 1
            matched_details.append({
                'project': proj,
                'funding_name': fund_name,
                'amount': amount
            })
            break

print('Final count of capital design projects with funding > $50,000:', matched_count)

result = {'count': matched_count}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
