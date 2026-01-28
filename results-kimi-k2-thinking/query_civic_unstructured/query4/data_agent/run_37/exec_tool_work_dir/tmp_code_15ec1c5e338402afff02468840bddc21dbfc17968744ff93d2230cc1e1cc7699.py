code = """import json, os, re

# Load funding data
funding_file = "/tmp/tmp4n6h1h4h.json"
funding_data = []
if os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)

# Get civic docs data path
civic_file = "/tmp/tmp4p5a1c3b.json" if os.path.exists("/tmp/tmp4p5a1c3b.json") else None
print('Civic file exists:', os.path.exists("/tmp/tmp4p5a1c3b.json"))

civic_docs = []
if civic_file and os.path.exists(civic_file):
    with open(civic_file, 'r') as f:
        civic_docs = json.load(f)

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Extract Spring 2022 projects from civic documents
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns with 2022
    # Projects often have names like "2022 Morning View Resurfacing & Storm Drain Improvements"
    # or mention "Project Schedule: ... Spring 2022" in their description
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 5:
            continue
            
        # Skip header/footer lines
        if any(skip in line for skip in ['Page', 'RECOMMENDED', 'DISCUSSION', 'Prepared', 'Approved', 'Subject:', 'To:', 'Meeting date', 'Capital Improvement Projects', 'Project Schedule', 'Updates:', 'Project Description']):
            continue
        if line.startswith('(') or line.startswith('cid:') or line.startswith('.'):
            continue
            
        # Check for 2022 in the line (likely a project name or schedule)
        if '2022' in line:
            # Look for season indicators in surrounding context
            context_start = max(0, i-10)
            context_end = min(len(lines), i+10)
            context = ' '.join(lines[context_start:context_end])
            
            # Check if this is Spring 2022
            is_spring = 'Spring' in line or 'spring' in context or 'Spring' in context
            
            # Also check filename for date patterns
            if '03' in filename or '04' in filename or '05' in filename:
                if '2022' in filename:
                    is_spring = True
            
            if is_spring:
                # Clean up project name - remove excessive whitespace
                project_name = ' '.join(line.split())[:200]
                spring_2022_projects.append({
                    'name': project_name,
                    'filename': filename
                })

# Deduplicate projects
unique_projects = {}
for proj in spring_2022_projects:
    name = proj['name']
    if name not in unique_projects:
        unique_projects[name] = proj

deduplicated_projects = list(unique_projects.values())

print('Spring 2022 projects found:', len(deduplicated_projects))
for p in deduplicated_projects[:5]:
    print('-', p['name'][:80])

# Match projects with funding
project_names = [p['name'] for p in deduplicated_projects]
matched_funding = []

for fund in funding_data:
    fund_name = fund.get('Project_Name', '').lower()
    fund_amount = int(fund.get('Amount', 0))
    
    # Direct match or fuzzy match
    for proj in project_names:
        proj_lower = proj.lower()
        
        # Check if project name contains the funded project name or vice versa
        if (fund_name in proj_lower or proj_lower in fund_name):
            # Check if this is a high-quality match (not just a generic name)
            if len(fund_name) > 10 or len(proj_lower) > 10:
                matched_funding.append({
                    'project': proj,
                    'fund_name': fund.get('Project_Name'),
                    'amount': fund_amount
                })
                break
        
        # Check for keyword overlaps (for compound names)
        fund_parts = [p for p in fund_name.split() if len(p) > 4 and p not in ['project', 'improvements', 'repairs']]
        proj_parts = [p for p in proj_lower.split() if len(p) > 4 and p not in ['project', 'improvements', 'repairs']]
        
        common = set(fund_parts) & set(proj_parts)
        if len(common) >= 2:  # At least 2 matching keywords
            matched_funding.append({
                'project': proj,
                'fund_name': fund.get('Project_Name'),
                'amount': fund_amount
            })
            break

# Deduplicate funding matches
unique_funding = {}
for fund in matched_funding:
    key = fund['project'] + '|' + str(fund['amount'])
    if key not in unique_funding:
        unique_funding[key] = fund

deduplicated_funding = list(unique_funding.values())

# Calculate totals
total_projects = len(deduplicated_projects)
total_funding = sum(f['amount'] for f in deduplicated_funding)

print('Matched funding records:', len(deduplicated_funding))
print('Total funding:', total_funding)

result = {
    'spring_2022_projects_count': total_projects,
    'matched_funding_count': len(deduplicated_funding),
    'total_funding': total_funding,
    'sample_projects': project_names[:10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'status': 'error', 'message': "[Errno 2] No such file or directory: '/tmp/tmpub7z9f6a.json'"}, 'var_functions.execute_python:14': {'available_vars': ['var_functions.query_db:2', 'var_functions.query_db:5']}, 'var_functions.execute_python:18': {'step': 'inspection'}, 'var_functions.execute_python:20': {'check': 'complete'}, 'var_functions.query_db:22': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:34': {'status': 'checked'}, 'var_functions.execute_python:36': {'checked': True}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': [{'count': '500', 'total_funding': '28094000'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json'}

exec(code, env_args)
