code = """import json
import re

# Read the full results from the stored JSON files
with open('file_storage/functions.query_db:0.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:2.json', 'r') as f:
    civic_docs_data = json.load(f)

# Step 1: Identify all emergency/FEMA related funding records
emergency_fema_funding = []

for record in funding_data:
    project_name = record.get('Project_Name', '')
    funding_source = record.get('Funding_Source', '')
    
    project_name_lower = project_name.lower()
    funding_source_lower = funding_source.lower()
    
    # Check for emergency/FEMA indicators
    if (any(keyword in project_name_lower for keyword in ['emergency', 'fema']) or
        any(keyword in funding_source_lower for keyword in ['emergency', 'fema']) or
        any(suffix in project_name_lower for suffix in ['(fema project)', '(caloes project)', '(caljpia project)'])):
        emergency_fema_funding.append(record)

# Create a lookup dictionary by project name
funding_lookup = {record['Project_Name']: record for record in emergency_fema_funding}

# Extract project information from civic documents
def extract_project_info(text, project_name):
    """Extract project status and other info from document text"""
    info = {
        'status': 'not found',
        'topic': '',
        'type': '',
        'st': '',
        'et': ''
    }
    
    # Look for the project name and related context
    project_pattern = re.escape(project_name)
    matches = re.finditer(project_pattern, text, re.IGNORECASE)
    
    for match in matches:
        # Get context around the match
        start = max(0, match.start() - 200)
        end = min(len(text), match.end() + 200)
        context = text[start:end]
        
        # Check for status indicators
        if 'completed' in context.lower():
            info['status'] = 'completed'
        elif 'construction' in context.lower():
            info['status'] = 'construction'
        elif 'design' in context.lower():
            info['status'] = 'design'
        elif 'not started' in context.lower():
            info['status'] = 'not started'
        
        # Try to determine type
        if 'fema' in context.lower() or 'disaster' in context.lower():
            info['type'] = 'disaster'
        elif 'capital' in context.lower():
            info['type'] = 'capital'
        
        # Try to find topic keywords
        topics = []
        if re.search(r'(?i)\b(storm|drain|drainage)\b', context):
            topics.append('storm drain')
        if re.search(r'(?i)\b(road|street|highway)\b', context):
            topics.append('road')
        if re.search(r'(?i)\b(park|playground)\b', context):
            topics.append('park')
        if re.search(r'(?i)\b(warning|siren|sign)\b', context):
            topics.append('emergency warning')
        if re.search(r'(?i)\b(bridge|culvert|retaining)\b', context):
            topics.append('bridge')
        
        if topics:
            info['topic'] = ', '.join(topics)
        
        if info['status'] != 'not found':
            break
    
    return info

# Find all emergency/FEMA related projects in civic documents
all_emergency_projects = []
project_names_found = set()

for doc in civic_docs_data:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Look for emergency/FEMA indicators
    if 'emergency' in text_lower or 'fema' in text_lower:
        # Find project names (look for lines that might be project names)
        lines = text.split('\n')
        for line in lines:
            line_clean = line.strip()
            if len(line_clean) > 10 and len(line_clean) < 150 and not line_clean.startswith(('[', '(', '•', '-', '*', '□')):
                if any(keyword in line_clean.lower() for keyword in ['project', 'repair', 'improvement', 'drain', 'road', 'bridge']):
                    # Check if this might be a project name
                    if sum(c.isupper() for c in line_clean[:50]) > 2 or ':' in line_clean:
                        project_name = line_clean.split(':')[0].strip()
                        
                        # Skip if already processed
                        if project_name.lower() in [p.lower() for p in project_names_found]:
                            continue
                            
                        # Check if it's related to emergency/FEMA
                        is_emergency = False
                        if any(keyword in project_name.lower() for keyword in ['emergency', 'fema']):
                            is_emergency = True
                        elif any(suffix in project_name.lower() for suffix in ['(fema project)', '(caloes project)', '(caljpia project)']):
                            is_emergency = True
                        elif any(keyword in line_clean.lower() for keyword in ['emergency', 'fema']):
                            is_emergency = True
                        
                        if is_emergency:
                            project_names_found.add(project_name)
                            
                            # Extract additional info
                            project_info = extract_project_info(text, project_name)
                            
                            # Find corresponding funding info
                            funding_match = None
                            for funding_proj in emergency_fema_funding:
                                if project_name.lower() in funding_proj['Project_Name'].lower() or \
                                   funding_proj['Project_Name'].lower() in project_name.lower():
                                    funding_match = funding_proj
                                    break
                            
                            if funding_match:
                                project_data = {
                                    'Project_Name': funding_match['Project_Name'],
                                    'Funding_Source': funding_match['Funding_Source'],
                                    'Amount': int(funding_match['Amount']),
                                    'Status': project_info['status'],
                                    'Topic': project_info['topic'],
                                    'Type': project_info['type']
                                }
                            else:
                                project_data = {
                                    'Project_Name': project_name,
                                    'Funding_Source': 'Not found in funding data',
                                    'Amount': 'Unknown',
                                    'Status': project_info['status'],
                                    'Topic': project_info['topic'],
                                    'Type': project_info['type']
                                }
                            
                            all_emergency_projects.append(project_data)

# Add any funding-only projects (not found in documents)
funding_only_projects = []
for funding_proj in emergency_fema_funding:
    found_in_docs = False
    for proj in all_emergency_projects:
        if proj['Project_Name'] and funding_proj['Project_Name'] in proj['Project_Name']:
            found_in_docs = True
            break
    
    if not found_in_docs:
        funding_only_projects.append({
            'Project_Name': funding_proj['Project_Name'],
            'Funding_Source': funding_proj['Funding_Source'],
            'Amount': int(funding_proj['Amount']),
            'Status': 'Unknown',
            'Topic': 'Unknown',
            'Type': 'Unknown'
        })

# Combine all projects
final_projects = all_emergency_projects + funding_only_projects

# Remove duplicates and format output
unique_projects = {}
for proj in final_projects:
    name = proj['Project_Name']
    if name not in unique_projects or proj['Status'] != 'Unknown':
        unique_projects[name] = proj

final_results = [{
    'Project_Name': proj['Project_Name'],
    'Funding_Source': proj['Funding_Source'],
    'Amount': proj['Amount'],
    'Status': proj['Status'],
    'Topic': proj['Topic'],
    'Type': proj['Type']
} for proj in unique_projects.values()]

# Sort by project name for clean output
final_results.sort(key=lambda x: x['Project_Name'])

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_result_type': "<class 'str'>", 'civic_docs_result_type': "<class 'str'>", 'funding_result_preview': 'file_storage/functions.query_db:0.json', 'civic_docs_result_preview': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json'}

exec(code, env_args)
