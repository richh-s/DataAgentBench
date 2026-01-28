code = """import json
import re
# Read the funding data
with open(var_functions.query_db:6, 'r') as f:
    funding_data = json.load(f)

# Filter funding data for Amount > 50000
funding_over_50k = [record for record in funding_data if int(record['Amount']) > 50000]
print(f"Found {len(funding_over_50k)} projects with funding > $50,000")

# Read the civic documents data
with open(var_functions.query_db:5, 'r') as f:
    civic_docs = json.load(f)

print(f"Found {len(civic_docs)} civic documents")

# Parse civic documents to extract project information
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects sections
    # The pattern seems to be:
    # Capital Improvement Projects (Design)
    # Project Name
    # ...
    
    # Split by sections
    sections = re.split(r'\n(?=Capital Improvement Projects)', text)
    
    for section in sections:
        if 'Capital Improvement Projects' in section:
            # Determine status from section header
            if '(Design)' in section:
                status = 'design'
            elif '(Construction)' in section:
                status = 'construction'
            elif '(Not Started)' in section:
                status = 'not started'
            else:
                continue
                
            # Extract project names - they appear as headers without bullet points
            lines = section.split('\n')
            for i, line in enumerate(lines):
                line = line.strip()
                # Skip empty lines, headers, and bullet points
                if not line or line.startswith('Capital Improvement Projects') or line.startswith('('):
                    continue
                # Project names are typically followed by updates or schedule
                if i + 1 < len(lines) and (lines[i+1].strip().startswith('(cid:') or 
                                           'Updates:' in lines[i+1] or 
                                           'Project Schedule:' in lines[i+1]):
                    project_name = line
                    projects.append({
                        'Project_Name': project_name,
                        'type': 'capital',
                        'status': status
                    })

print(f"Extracted {len(projects)} capital projects")

# Count design status projects
design_projects = [p for p in projects if p['status'] == 'design']
print(f"Found {len(design_projects)} capital projects with design status")

# Create a set of project names from funding data for faster lookup
funding_project_names = set(record['Project_Name'] for record in funding_over_50k)

# Match design capital projects with funding > 50k
matched_projects = []
for project in design_projects:
    # Check for exact match or partial match
    for funding_record in funding_over_50k:
        funding_name = funding_record['Project_Name']
        # Check if project name matches (accounting for suffixes like (FEMA Project))
        if (project['Project_Name'] == funding_name or 
            funding_name.startswith(project['Project_Name'] + ' (') or
            project['Project_Name'].startswith(funding_name + ' (')):
            matched_projects.append({
                'Project_Name': project['Project_Name'],
                'Funding_Project_Name': funding_name,
                'Amount': int(funding_record['Amount']),
                'status': project['status'],
                'type': project['type']
            })

print(f"Matched {len(matched_projects)} capital projects with design status and funding > $50,000")

# For debugging, let's see which projects matched
for p in matched_projects:
    print(f"- {p['Project_Name']}: ${p['Amount']}")

result = len(matched_projects)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
