code = """import json
import re

# Read the civic documents
with open('var_functions.query_db:18', 'r') as f:
    civic_docs = json.load(f)

# Read the funding data
with open('var_functions.query_db:24', 'r') as f:
    funding_data = json.load(f)

print('Documents loaded:', len(civic_docs))
print('Funding records loaded:', len(funding_data))

# Find emergency/FEMA projects in civic documents
all_projects = []

doc_count = 0
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lower_text = text.lower()
    has_fema = 'fema' in lower_text
    has_emergency = 'emergency' in lower_text
    
    if has_fema or has_emergency:
        doc_count += 1
        # Split into lines and look for project names
        lines = text.split('\n')
        for idx, line in enumerate(lines):
            line = line.strip()
            # Look for lines that might be project names (not too short, not headers)
            if len(line) > 10:
                # Skip header lines
                if line.find('Capital Improvement') >= 0 or line.find('Disaster Recovery') >= 0:
                    continue
                if line.find('Agenda Report') >= 0 or line.find('Public Works Commission') >= 0:
                    continue
                if line.find('To:') >= 0 or line.find('Prepared by:') >= 0:
                    continue
                
                # Check if this line is followed by project details marker
                if idx + 1 < len(lines) and lines[idx+1].find('(cid:190)') >= 0:
                    project_name = line
                    
                    # Find status from context
                    status = 'not started'
                    context = ' '.join(lines[idx:idx+15])
                    context_lower = context.lower()
                    
                    if context_lower.find('under construction') >= 0:
                        status = 'construction'
                    elif context_lower.find('design') >= 0 and context_lower.find('complete') >= 0:
                        status = 'design'
                    elif context_lower.find('design') >= 0:
                        status = 'design'
                    elif context_lower.find('complete') >= 0 or context_lower.find('completed') >= 0:
                        status = 'completed'
                    
                    # Build topics
                    topics = []
                    if has_fema:
                        topics.append('FEMA')
                    if has_emergency:
                        topics.append('emergency')
                    
                    # Determine type
                    project_type = 'disaster' if has_fema else 'capital'
                    
                    all_projects.append({
                        'Project_Name': project_name,
                        'topics': ','.join(topics),
                        'type': project_type,
                        'status': status
                    })

print('Documents with emergency/FEMA:', doc_count)
print('Projects extracted:', len(all_projects))

# Build funding lookup
funding_lookup = {}
for item in funding_data:
    name = item.get('Project_Name', '')
    if name not in funding_lookup:
        funding_lookup[name] = []
    funding_lookup[name].append({
        'source': item.get('Funding_Source', 'Unknown'),
        'amount': int(item.get('Amount', 0))
    })

print('Funding lookup size:', len(funding_lookup))

# Merge with funding data
results = []
for project in all_projects:
    proj_name = project['Project_Name']
    matched = False
    
    # Direct match
    if proj_name in funding_lookup:
        for fund in funding_lookup[proj_name]:
            results.append({
                'Project_Name': proj_name,
                'Funding_Source': fund['source'],
                'Amount': fund['amount'],
                'Status': project['status'],
                'Topic': project['topics'],
                'Type': project['type']
            })
        matched = True
    else:
        # Fuzzy match
        for funded_name in funding_lookup.keys():
            if proj_name in funded_name or funded_name in proj_name:
                for fund in funding_lookup[funded_name]:
                    results.append({
                        'Project_Name': proj_name,
                        'Funding_Source': fund['source'],
                        'Amount': fund['amount'],
                        'Status': project['status'],
                        'Topic': project['topics'],
                        'Type': project['type']
                    })
                matched = True
                break
    
    if not matched:
        results.append({
            'Project_Name': proj_name,
            'Funding_Source': 'No funding record',
            'Amount': 0,
            'Status': project['status'],
            'Topic': project['topics'],
            'Type': project['type']
        })

print('Final results count:', len(results))

# Output
output = json.dumps(results, ensure_ascii=False)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'name': 'Funding'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
