code = """import json
import re

# Load civic documents
civic_docs_key = 'var_functions.query_db:5'
civic_docs = locals().get(civic_docs_key, [])
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

# Load funding data
funding_key = 'var_functions.query_db:8'
funding_data = locals().get(funding_key, [])
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Parse projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project names which are typically on separate lines
    # and are followed by status information
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and common headers
        if not line or line.startswith('(') or line in ['Public Works Commission', 'Agenda Report', 
                                                        'Capital Improvement Projects (Design)', 
                                                        'Capital Improvement Projects (Construction)',
                                                        'Capital Improvement Projects (Not Started)',
                                                        'Disaster Recovery Projects']:
            continue
            
        # Look for project indicators (capital projects and disaster projects)
        # Project names usually don't contain typical agenda markers
        if len(line) > 10 and not any(marker in line for marker in ['Page', 'Agenda Item', '...', 'http', 'www', 'RECOMMENDED ACTION:']):
            
            # Check if next lines contain date information
            next_lines = ' '.join(lines[i+1:min(i+10, len(lines))])
            
            # Extract start time if mentioned
            start_time = None
            if '2022' in next_lines:
                # Look for Spring 2022 patterns
                spring_patterns = ['2022-Spring', 'Spring 2022', '2022-March', '2022-April', '2022-May',
                                  'March 2022', 'April 2022', 'May 2022', '2022-03', '2022-04', '2022-05']
                for pattern in spring_patterns:
                    if pattern in next_lines:
                        start_time = '2022-Spring'
                        break
            
            if start_time:
                projects.append({
                    'Project_Name': line,
                    'st': start_time,
                    'source_doc': doc.get('filename', '')
                })

# Group by project name to avoid duplicates
project_dict = {}
for proj in projects:
    # Normalize name (remove common suffixes that might be in funding data differently)
    name = proj['Project_Name']
    if name not in project_dict:
        project_dict[name] = proj

print(f"Found {len(project_dict)} unique projects starting in Spring 2022")
print('Sample projects:', list(project_dict.keys())[:5])

# Now find funding for these projects
project_names = list(project_dict.keys())

# Create a lookup for funding by project name
funding_lookup = {}
for fund in funding_data:
    fund_name = fund.get('Project_Name', '').strip()
    funding_lookup[fund_name] = funding_lookup.get(fund_name, 0) + int(fund.get('Amount', 0))

# Try to match project names with funding
matched_projects = []
total_funding = 0

for proj_name in project_names:
    # Direct match
    if proj_name in funding_lookup:
        matched_projects.append({
            'Project_Name': proj_name,
            'Amount': funding_lookup[proj_name]
        })
        total_funding += funding_lookup[proj_name]
    else:
        # Try variations without suffixes
        base_name = proj_name
        # Remove common suffixes
        for suffix in ['Project', 'Improvements', 'Repairs', 'Construction', 'Design']:
            if f' {suffix}' in base_name:
                base_name = base_name.replace(f' {suffix}', '')
        
        # Try to match with base name
        for fund_name, amount in funding_lookup.items():
            if (base_name in fund_name or fund_name in proj_name or 
                proj_name.lower() in fund_name.lower() or 
                fund_name.lower() in proj_name.lower()):
                matched_projects.append({
                    'Project_Name': proj_name,
                    'Amount': amount
                })
                total_funding += amount
                break

print(f"Found funding for {len(matched_projects)} projects")
print(f"Total funding: ${total_funding:,}")

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects[:10]  # First 10 for preview
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_civic_docs': 5, 'total_funding_records': 500}}

exec(code, env_args)
