code = """import json
import re

# Read the full results from the stored JSON files
with open('file_storage/functions.query_db:0.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs_data = json.load(f)

# Step 1: Filter for emergency/FEMA related funding records
emergency_fema_projects = []

for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    funding_source = record.get('Funding_Source', '').lower()
    
    # Check for emergency/FEMA indicators
    if (any(keyword in project_name for keyword in ['emergency', 'fema']) or
        any(keyword in funding_source for keyword in ['emergency', 'fema']) or
        any(suffix in project_name for suffix in ['(fema project)', '(caloes project)', '(caljpia project)'])):
        
        emergency_fema_projects.append({
            'Project_Name': record['Project_Name'],
            'Funding_Source': record['Funding_Source'],
            'Amount': int(record['Amount']),
            'Status': 'Unknown',
            'Topic': 'Unknown',
            'Type': 'Unknown'
        })

print(f"Found {len(emergency_fema_projects)} emergency/FEMA funding projects")
print("Sample projects:", [p['Project_Name'] for p in emergency_fema_projects[:5]])

# Step 2: Extract status information from civic documents
all_doc_text = " ".join([doc.get('text', '') for doc in civic_docs_data])
all_doc_text_lower = all_doc_text.lower()

# Update project statuses based on document text
for project in emergency_fema_projects:
    project_name_lower = project['Project_Name'].lower()
    
    # Find mentions of this project in documents
    pattern = re.escape(project_name_lower)
    matches = list(re.finditer(pattern, all_doc_text_lower))
    
    if matches:
        project['Status'] = 'Mentioned in documents'
        
        # Try to extract specific status
        for match in matches:
            context_start = max(0, match.start() - 200)
            context_end = min(len(all_doc_text_lower), match.end() + 200)
            context = all_doc_text_lower[context_start:context_end]
            
            if 'completed' in context:
                project['Status'] = 'completed'
                break
            elif 'construction' in context or 'under construction' in context:
                project['Status'] = 'construction'
                break
            elif 'design' in context:
                project['Status'] = 'design'
                break
    
    # Determine type based on project name
    if any(keyword in project_name_lower for keyword in ['fema', 'disaster', 'emergency']):
        project['Type'] = 'disaster'
    else:
        project['Type'] = 'capital'
    
    # Determine topic based on project name
    name_lower = project['Project_Name'].lower()
    if 'storm' in name_lower or 'drain' in name_lower:
        project['Topic'] = 'storm drain'
    elif 'road' in name_lower or 'street' in name_lower:
        project['Topic'] = 'road'
    elif 'siren' in name_lower or 'warning' in name_lower:
        project['Topic'] = 'emergency warning'
    elif 'bridge' in name_lower or 'culvert' in name_lower:
        project['Topic'] = 'bridge'
    elif 'park' in name_lower:
        project['Topic'] = 'park'

# Format final results
results = []
for project in emergency_fema_projects:
    results.append({
        'Project_Name': project['Project_Name'],
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': project['Status'],
        'Topic': project['Topic'],
        'Type': project['Type']
    })

results.sort(key=lambda x: x['Project_Name'])

# Print results in required format
output = '__RESULT__:\n' + json.dumps(results, indent=2)
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_result_type': "<class 'str'>", 'civic_docs_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:0.json', 'civic_docs_result_preview': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
