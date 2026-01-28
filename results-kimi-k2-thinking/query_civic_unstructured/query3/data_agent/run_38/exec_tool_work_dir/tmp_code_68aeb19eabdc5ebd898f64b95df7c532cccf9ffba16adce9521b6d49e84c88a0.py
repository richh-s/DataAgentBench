code = """import json
import re

# Load data from both sources
with open('var_functions.query_db:18', 'r') as f:
    civic_docs = json.load(f)

with open('var_functions.query_db:24', 'r') as f:
    funding_records = json.load(f)

print('Loaded', len(civic_docs), 'civic documents and', len(funding_records), 'funding records')

# Extract emergency/FEMA projects from civic documents
emergency_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    lower_text = text.lower()
    has_fema = 'fema' in lower_text
    has_emergency = 'emergency' in lower_text
    
    if has_fema or has_emergency:
        # Find project names - they appear before (cid:190) markers
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            # Skip empty or very short lines, and lines that look like headers
            if len(line) < 10 or 'Capital Improvement' in line or 'Disaster Recovery' in line:
                continue
            if 'Agenda Report' in line or 'Public Works Commission' in line:
                continue
                
            # Check if this line is followed by project details
            if i + 1 < len(lines) and '(cid:190)' in lines[i+1]:
                project_name = line
                
                # Determine status from following text
                status = 'not started'
                next_lines = ' '.join(lines[i:i+15]).lower()
                
                if 'under construction' in next_lines:
                    status = 'construction'
                elif 'design' in next_lines and ('complete' in next_lines or 'completed' in next_lines):
                    # This is "Complete Design" - still in design phase
                    status = 'design'
                elif 'design' in next_lines:
                    status = 'design'
                elif 'complete' in next_lines or 'completed' in next_lines:
                    status = 'completed'
                
                # Build topics list
                topics = []
                if has_fema:
                    topics.append('FEMA')
                if has_emergency:
                    topics.append('emergency')
                
                # Determine project type
                project_type = 'disaster' if has_fema else 'capital'
                
                emergency_projects.append({
                    'Project_Name': project_name,
                    'topics': ','.join(topics),
                    'type': project_type,
                    'status': status
                })

print('Extracted', len(emergency_projects), 'emergency/FEMA projects')

# Create funding lookup dictionary
funding_lookup = {}
for record in funding_records:
    proj_name = record.get('Project_Name', '')
    if proj_name not in funding_lookup:
        funding_lookup[proj_name] = []
    funding_lookup[proj_name].append({
        'Funding_Source': record.get('Funding_Source', 'Unknown'),
        'Amount': int(record.get('Amount', 0))
    })

print('Created funding lookup with', len(funding_lookup), 'project names')

# Merge projects with funding data
final_results = []

for project in emergency_projects:
    proj_name = project['Project_Name']
    found_funding = False
    
    # Try direct match first
    if proj_name in funding_lookup:
        for funding in funding_lookup[proj_name]:
            final_results.append({
                'Project_Name': proj_name,
                'Funding_Source': funding['Funding_Source'],
                'Amount': funding['Amount'],
                'Status': project['status'],
                'Topic': project['topics'],
                'Type': project['type']
            })
        found_funding = True
    else:
        # Try fuzzy matching - check if extracted name is contained in funded name
        for funded_name in funding_lookup.keys():
            if proj_name in funded_name or funded_name in proj_name:
                for funding in funding_lookup[funded_name]:
                    final_results.append({
                        'Project_Name': proj_name,
                        'Funding_Source': funding['Funding_Source'],
                        'Amount': funding['Amount'],
                        'Status': project['status'],
                        'Topic': project['topics'],
                        'Type': project['type']
                    })
                found_funding = True
                break
    
    if not found_funding:
        # No funding found for this project
        final_results.append({
            'Project_Name': proj_name,
            'Funding_Source': 'No funding record',
            'Amount': 0,
            'Status': project['status'],
            'Topic': project['topics'],
            'Type': project['type']
        })

print('Generated', len(final_results), 'final results')

# Output as JSON
json_result = json.dumps(final_results, ensure_ascii=False)
print('__RESULT__:')
print(json_result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'name': 'Funding'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
