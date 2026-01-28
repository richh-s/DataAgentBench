code = """import json
import re

# Load the funding data (from var_functions.query_db:4)
with open('/tmp/tmp_hb9f3fdk.json', 'r') as f:
    funding_data = json.load(f)

# Load the civic docs data (from var_functions.query_db:5)
with open('/tmp/tmp_cdv8r04p.json', 'r') as f:
    civic_docs_data = json.load(f)

# Process funding data into dictionary for easy lookup
funding_dict = {}
for record in funding_data:
    proj_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_dict[proj_name] = amount

# Extract project information from civic documents
import re

# Pattern to match project entries in the text
# Looking for patterns like:
# Project Name (status)
# - topic: ...
# - type: ...
# - st: ...
# - et: ...

def extract_projects_from_text(text):
    projects = []
    
    # Split text into lines for easier processing
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for project name lines (often have status in parentheses)
        # Pattern: Project Name (status)
        project_match = re.match(r'^([^(]+)\(([a-zA-Z\s]+)\)$', line)
        if project_match and i + 4 < len(lines):
            project_name = project_match.group(1).strip()
            status = project_match.group(2).strip().lower()
            
            # Look for next lines with topic, type, st, et
            topic = None
            type_val = None
            st = None
            et = None
            
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j].strip()
                if next_line.startswith('topic:'):
                    topic = next_line.replace('topic:', '').strip()
                elif next_line.startswith('type:'):
                    type_val = next_line.replace('type:', '').strip()
                elif next_line.startswith('st:'):
                    st = next_line.replace('st:', '').strip()
                elif next_line.startswith('et:'):
                    et = next_line.replace('et:', '').strip()
            
            # If we found the required fields, add the project
            if topic and type_val and st:
                projects.append({
                    'Project_Name': project_name,
                    'topic': topic,
                    'type': type_val,
                    'status': status,
                    'st': st,
                    'et': et
                })
        
        i += 1
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    projects = extract_projects_from_text(text)
    all_projects.extend(projects)

# Filter for disaster projects that started in 2022
disaster_projects_2022 = []
for proj in all_projects:
    if proj['type'] == 'disaster' and '2022' in proj['st']:
        disaster_projects_2022.append(proj)

# Also check for projects with FEMA/CalJPIA/CalOES suffixes in their names
# These are likely disaster projects even if not explicitly marked as such
fema_pattern = r'\((FEMA|CalJPIA|CalOES)\s+Project\)'

additional_disaster_projects = []
for proj in all_projects:
    if re.search(fema_pattern, proj['Project_Name'], re.IGNORECASE):
        if '2022' in proj['st'] and proj['type'] != 'disaster':
            # Update the type to disaster
            proj['type'] = 'disaster'
            additional_disaster_projects.append(proj)

disaster_projects_2022.extend(additional_disaster_projects)

# Remove duplicates based on project name
unique_projects = {}
for proj in disaster_projects_2022:
    proj_name = proj['Project_Name']
    if proj_name not in unique_projects:
        unique_projects[proj_name] = proj

disaster_projects_2022 = list(unique_projects.values())

# Now match with funding data
total_funding = 0
funded_projects = []

for proj in disaster_projects_2022:
    proj_name = proj['Project_Name']
    if proj_name in funding_dict:
        amount = funding_dict[proj_name]
        total_funding += amount
        funded_projects.append({
            'Project_Name': proj_name,
            'Amount': amount,
            'st': proj['st'],
            'topic': proj['topic']
        })

# Also check for partial name matches (in case the names don't match exactly)
# Create a mapping of all funding projects for fuzzy matching
remaining_funding = {k: v for k, v in funding_dict.items() if k not in [p['Project_Name'] for p in funded_projects]}

for proj in disaster_projects_2022:
    proj_name = proj['Project_Name']
    if proj_name in remaining_funding:
        continue  # Already matched
    
    # Try to find matching funding project
    for fund_name, amount in remaining_funding.items():
        # Clean both names for comparison
        clean_proj = proj_name.lower().replace('(', '').replace(')', '').strip()
        clean_fund = fund_name.lower().replace('(', '').replace(')', '').strip()
        
        # Check if one is a substring of the other
        if clean_proj in clean_fund or clean_fund in clean_proj:
            total_funding += amount
            funded_projects.append({
                'Project_Name': proj_name,
                'Funding_Project_Name': fund_name,
                'Amount': amount,
                'st': proj['st'],
                'topic': proj['topic']
            })
            del remaining_funding[fund_name]
            break

# Print results in required format
result_str = json.dumps({
    'total_funding': total_funding,
    'project_count': len(funded_projects),
    'projects': funded_projects
})

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
