code = """import json
import re

# Load funding data  
funding_data = var_functions.query_db:0
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data, 'r') as f:
        funding_records = json.load(f)
else:
    funding_records = funding_data

print(f"Funding records with Amount > 50000: {len(funding_records)}")

# Load civic docs data
civic_data = var_functions.query_db:2
if isinstance(civic_data, str) and civic_data.endswith('.json'):
    with open(civic_data, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_data

print(f"Number of civic documents: {len(civic_docs)}")

# Extract capital design projects from civic docs
projects = []

design_indicators = ['design', 'finalizing', 'complete design', 'design plans', 'design consultant']
project_keywords = ['road', 'avenue', 'drive', 'street', 'park', 'drain', 'storm', 'bridge', 'walkway', 'trail', 'sewer', 'water', 'traffic', 'signal', 'sign', 'median', 'crosswalk', 'improvements', 'repairs', 'project']

for doc in civic_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check if document mentions capital projects in design
    if 'capital improvement projects' in text_lower and 'design' in text_lower:
        # Look for project names in the document
        lines = text.split('\n')
        
        for line in lines:
            line_clean = line.strip()
            
            if not line_clean:
                continue
            
            # Skip administrative lines
            if any(x in line_clean.lower() for x in ['updates:', 'schedule:', 'staff is', 'city council', 'city submitted', 'consultant', 'estimated schedule', 'discussion:', 'page ', 'project ', 'complete design', 'advertise:', 'begin construction']):
                continue
            
            if len(line_clean) < 10:
                continue
            
            # Check if line looks like a project name (contains project keywords)
            if any(keyword in line_clean.lower() for keyword in project_keywords):
                projects.append({
                    'Project_Name': line_clean,
                    'type': 'capital',
                    'status': 'design'
                })

# Remove duplicates
unique_projects = []
seen = set()

for proj in projects:
    key = proj['Project_Name'].lower().strip()
    if key not in seen:
        seen.add(key)
        unique_projects.append(proj)

projects = unique_projects

print(f"Extracted {len(projects)} potential projects")
for i, p in enumerate(projects[:10]):
    print(f" {i+1}. {p['Project_Name']}")

# Match with funding data
matched = []

for proj in projects:
    proj_name_lower = proj['Project_Name'].lower()
    
    for fund in funding_records:
        fund_name = fund['Project_Name']
        fund_amount = int(fund['Amount'])
        
        if fund_amount <= 50000:
            continue
            
        fund_name_lower = fund_name.lower()
        
        # Direct or partial match
        if (proj_name_lower == fund_name_lower or 
            proj_name_lower in fund_name_lower or 
            fund_name_lower in proj_name_lower):
            
            matched.append({
                'Project_Name': proj['Project_Name'],
                'Funding_Project_Name': fund_name,
                'Amount': fund_amount,
                'Funding_Source': fund['Funding_Source']
            })
            break

print(f"\nTotal matches: {len(matched)}")

result = {
    'count': len(matched)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
