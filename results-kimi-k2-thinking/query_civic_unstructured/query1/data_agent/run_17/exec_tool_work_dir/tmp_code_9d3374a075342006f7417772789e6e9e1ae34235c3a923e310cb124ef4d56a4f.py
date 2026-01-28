code = """import json
import re

# Load funding data (Amount > 50000)
with open('funding_results.json', 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
with open('civic_docs_results.json', 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic docs
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Split by sections to identify project types and statuses
    # Look for Capital Improvement Projects sections
    
    # Pattern for capital projects with design status
    design_pattern = r'Capital Improvement Projects \(Design\)(.*?)(?=Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION|$)'
    design_section = re.search(design_pattern, text, re.DOTALL)
    
    if design_section:
        # Extract project names from this section
        # Look for lines that start with project names (typically bold or all caps)
        section_text = design_section.group(1)
        
        # Split into lines and process
        lines = section_text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for project name patterns (skip empty lines, status lines, etc.)
            if line and not line.startswith('(') and not line.startswith('cid:') and \
               'Updates:' not in line and 'Project Schedule:' not in line and \
               'Complete Design:' not in line and 'Advertise:' not in line and \
               'Begin Construction:' not in line and not re.match(r'^[A-Z]\.*$', line):
                
                # Skip lines that are just status indicators
                if any(keyword in line for keyword in ['Updates', 'Schedule', 'Complete', 'Advertise', 'Begin', 'Spring', 'Summer', 'Fall', 'Winter', '202']):
                    continue
                    
                # This looks like a project name
                if len(line) > 5 and not line.isupper():  # Not all caps (those are usually headings)
                    project_name = line.strip()
                    projects.append({
                        'Project_Name': project_name,
                        'type': 'capital',
                        'status': 'design'
                    })

# Now match with funding data
matches = []
funding_project_names = [f['Project_Name'] for f in funding_data]

for proj in projects:
    proj_name = proj['Project_Name']
    # Look for exact match or close match in funding data
    for fund_proj in funding_data:
        fund_name = fund_proj['Project_Name']
        # Check for exact match
        if proj_name == fund_name:
            matches.append({
                'Project_Name': proj_name,
                'type': proj['type'],
                'status': proj['status'],
                'Amount': int(fund_proj['Amount'])
            })
            break
        # Check if project name is contained within funding name
        elif proj_name in fund_name:
            matches.append({
                'Project_Name': fund_name,  # Use the more complete name from funding
                'type': proj['type'],
                'status': proj['status'],
                'Amount': int(fund_proj['Amount'])
            })
            break
        # Check if funding name is contained within project name
        elif fund_name in proj_name:
            matches.append({
                'Project_Name': proj_name,
                'type': proj['type'],
                'status': proj['status'],
                'Amount': int(fund_proj['Amount'])
            })
            break

# Filter for Amount > 50000 (already filtered in funding_data, but double-check)
final_matches = [m for m in matches if m['Amount'] > 50000]

print('__RESULT__:')
print(json.dumps({
    'count': len(final_matches),
    'projects': final_matches
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
