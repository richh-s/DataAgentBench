code = """import json
import re

# Load the data
civic_docs = locals()['var_functions.query_db:4'] if not isinstance(locals()['var_functions.query_db:4'], str) else json.load(open(locals()['var_functions.query_db:4']))
funding_data = locals()['var_functions.query_db:6'] if not isinstance(locals()['var_functions.query_db:6'], str) else json.load(open(locals()['var_functions.query_db:6']))

# Extract funding for emergency/FEMA projects
emergency_fema_funding = []
emergency_fema_pattern = re.compile(r'(emergency|fema)', re.IGNORECASE)

for record in funding_data:
    if emergency_fema_pattern.search(record['Project_Name']):
        emergency_fema_funding.append(record)

# Extract project details from civic documents text
projects = []

# Patterns for project sections
project_patterns = [
    (r'([A-Z][A-Za-z\s&\-]+?(?:\([^)]+\))?)\s*\(cid:\d+\)\s*Updates:', r'([A-Z][A-Za-z\s&\-]+?(?:\([^)]+\))?)\s*\(cid:\d+\)\s*Updates:', 'updates'),
    (r'([A-Z][A-Za-z\s&\-]+?(?:\([^)]+\))?)\s*\(cid:\d+\)\s*Project Schedule:', r'([A-Z][A-Za-z\s&\-]+?(?:\([^)]+\))?)\s*\(cid:\d+\)\s*Project Schedule:', 'schedule'),
    (r'([A-Z][A-Za-z\s&\-]+?(?:\([^)]+\))?)\s*\n\(cid:\d+\)\s*Updates:', r'([A-Z][A-Za-z\s&\-]+?(?:\([^)]+\))?)\s*\n\(cid:\d+\)\s*Updates:', 'updates2'),
]

status_keywords = {
    'design': ['design', 'planning', 'preliminary'],
    'completed': ['completed', 'construction was completed', 'notice of completion'],
    'not started': ['not started', 'identified', 'preliminary design']
}

topic_keywords = [
    'emergency', 'fema', 'fire', 'drainage', 'storm drain', 'warning', 'siren',
    'park', 'road', 'bridge', 'street', 'canyon', 'highway', 'guardrail'
]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    project_info = {}
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check for project name
        for pattern, name_pattern, info_type in project_patterns:
            match = re.search(pattern, text[i-200:i+200] if i > 200 else text[:i+200])
            if match and len(match.group(1).strip()) > 10:
                name = match.group(1).strip()
                if emergency_fema_pattern.search(name) or any(keyword in text.lower() for keyword in ['emergency', 'fema']):
                    current_project = name
                    project_info = {
                        'Project_Name': name,
                        'Status': 'unknown',
                        'Topic': [],
                        'Type': 'unknown',
                        'Source_Document': doc['filename']
                    }
                    projects.append(project_info)
                break
        
        # Determine status
        if current_project:
            low_line = line.lower()
            if any(keyword in low_line for keyword in status_keywords['design']):
                if 'delay' not in low_line and 'delayed' not in low_line:
                    project_info['Status'] = 'design'
            elif any(keyword in low_line for keyword in status_keywords['completed']):
                project_info['Status'] = 'completed'
            elif any(keyword in low_line for keyword in status_keywords['not started']):
                project_info['Status'] = 'not started'
            
            # Determine type
            if '(FEMA' in current_project or 'FEMA' in current_project:
                project_info['Type'] = 'disaster'
            elif any(x in current_project.lower() for x in ['storm', 'drain', 'slope', 'road', 'street']):
                project_info['Type'] = 'capital'
            
            # Extract topics
            for keyword in topic_keywords:
                if keyword in line.lower():
                    if keyword not in project_info['Topic']:
                        project_info['Topic'].append(keyword)

# Normalize project names for matching
def normalize_name(name):
    if not name:
        return ""
    # Remove parentheticals, standardize spacing and case
    cleaned = re.sub(r'\([^)]*\)', '', name).strip()
    return re.sub(r'\s+', ' ', cleaned).lower()

# Create lookup for funding data
funding_lookup = {}
for fund in emergency_fema_funding:
    norm_name = normalize_name(fund['Project_Name'])
    if norm_name not in funding_lookup:
        funding_lookup[norm_name] = []
    funding_lookup[norm_name].append(fund)

# Match projects with funding
matched_projects = []
for proj in projects:
    norm_proj_name = normalize_name(proj['Project_Name'])
    
    # Direct match
    if norm_proj_name in funding_lookup:
        for fund_record in funding_lookup[norm_proj_name]:
            matched_projects.append({
                'Project_Name': proj['Project_Name'],
                'Status': proj['Status'],
                'Type': proj['Type'],
                'Topic': ', '.join(proj['Topic']),
                'Funding_Source': fund_record['Funding_Source'],
                'Amount': int(fund_record['Amount']),
                'Source_Document': proj['Source_Document']
            })
    else:
        # Try partial matching
        for fund_norm_name, fund_records in funding_lookup.items():
            if fund_norm_name in norm_proj_name or norm_proj_name in fund_norm_name:
                for fund_record in fund_records:
                    matched_projects.append({
                        'Project_Name': proj['Project_Name'],
                        'Status': proj['Status'],
                        'Type': proj['Type'],
                        'Topic': ', '.join(proj['Topic']),
                        'Funding_Source': fund_record['Funding_Source'],
                        'Amount': int(fund_record['Amount']),
                        'Source_Document': proj['Source_Document']
                    })
                break

# Also include any funding records that didn't get matched but contain FEMA/emergency
unmatched_funding = []
for fund in emergency_fema_funding:
    norm_name = normalize_name(fund['Project_Name'])
    is_matched = False
    for proj in matched_projects:
        if normalize_name(proj['Project_Name']) == norm_name:
            is_matched = True
            break
    
    if not is_matched:
        unmatched_funding.append({
            'Project_Name': fund['Project_Name'],
            'Status': 'not found in documents',
            'Type': 'unknown',
            'Topic': 'emergency/fema',
            'Funding_Source': fund['Funding_Source'],
            'Amount': int(fund['Amount']),
            'Source_Document': 'N/A'
        })

final_results = matched_projects + unmatched_funding

# Sort by amount descending
final_results.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(final_results[:50], indent=2) if final_results else json.dumps([]))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 19, 'funding_count': 500, 'civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}}

exec(code, env_args)
