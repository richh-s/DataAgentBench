code = """import json

# Read the civic documents
civic_docs_path = var_functions.query_db:10
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:10

# Read the funding data
funding_path = var_functions.query_db:11
if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = var_functions.query_db:11

print(f"Found {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Extract project information from civic docs (this is a simplified parsing)
# Looking for projects in the text that mention emergency/FEMA topics
fema_emergency_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project sections in the text (simplified approach)
    # This is a basic text parsing to identify projects related to emergency/FEMA
    lines = text.split('\n')
    current_project = None
    
    for line in lines:
        line = line.strip()
        if line and len(line) > 5:
            # Look for potential project names (typically title case or uppercase)
            if line[0].isupper() and not line.startswith('(') and not line.startswith('Page') and not line.startswith('Agenda'):
                # Check if this line mentions FEMA or emergency
                if 'FEMA' in line.upper() or 'EMERGENCY' in line.upper() or 'WARNING' in line:
                    current_project = line
                    
                    # Try to determine status
                    status = "unknown"
                    if 'design' in text.lower() and line.lower() in text.lower():
                        if 'completed' in text.lower():
                            status = "completed"
                        elif 'design' in text.lower():
                            status = "design"
                        elif 'construction' in text.lower():
                            status = "construction"
                        elif 'not started' in text.lower():
                            status = "not started"
                    
                    fema_emergency_projects.append({
                        'Project_Name': line,
                        'topic': 'emergency, FEMA, warning',
                        'type': 'disaster',
                        'status': status,
                        'source_doc': doc['filename']
                    })

print(f"Found {len(fema_emergency_projects)} potential FEMA/emergency projects in civic docs")

# Also check funding data for projects with FEMA/emergency in the name
fema_funding = []
for fund in funding_data:
    project_name = fund.get('Project_Name', '')
    if 'FEMA' in project_name.upper() or 'EMERGENCY' in project_name.upper() or 'WARNING' in project_name.upper():
        fema_funding.append(fund)

print(f"Found {len(fema_funding)} FEMA/emergency projects in funding data")

# Match funding with civic doc project information
matches = []
for fund in fema_funding:
    project_name = fund['Project_Name']
    
    # Find matching civic doc project
    civic_match = None
    for proj in fema_emergency_projects:
        if proj['Project_Name'] in project_name or project_name in proj['Project_Name']:
            civic_match = proj
            break
    
    # If no exact match, try to match by key terms
    if not civic_match:
        for proj in fema_emergency_projects:
            # Extract key terms (first few words)
            proj_terms = ' '.join(proj['Project_Name'].split()[:3])
            fund_terms = ' '.join(project_name.split()[:3])
            if proj_terms in project_name or fund_terms in proj['Project_Name']:
                civic_match = proj
                break
    
    if civic_match:
        matches.append({
            'Project_Name': project_name,
            'Funding_Source': fund['Funding_Source'],
            'Amount': fund['Amount'],
            'Status': civic_match['status'],
            'Topic': civic_match['topic'],
            'Type': civic_match['type']
        })
    else:
        # Still include the funding info even if no civic doc match
        matches.append({
            'Project_Name': project_name,
            'Funding_Source': fund['Funding_Source'],
            'Amount': fund['Amount'],
            'Status': 'unknown',
            'Topic': 'emergency, FEMA',
            'Type': 'disaster'
        })

print(f"Matched {len(matches)} FEMA/emergency projects with funding")

# Display results
for match in matches:
    print(f"Project: {match['Project_Name']}")
    print(f"  Funding: {match['Funding_Source']}")
    print(f"  Amount: ${match['Amount']}")
    print(f"  Status: {match['Status']}")
    print(f"  Topic: {match['Topic']}")
    print()

result = json.dumps(matches)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
