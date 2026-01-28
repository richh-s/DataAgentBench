code = """import json, re

# Load data from the stored result
funding_records = globals()['var_functions.query_db:42']

civic_docs = json.load(open(globals()['var_functions.query_db:0']))

print('Found', len(funding_records), 'funding records for emergency/FEMA projects')
print('Loaded', len(civic_docs), 'civic documents')

# Extract project names from funding records
project_names_from_funding = [rec['Project_Name'] for rec in funding_records]
print('Project names to search for:', len(project_names_from_funding))

# Function to extract project information from document text
def extract_project_info(text, search_names):
    projects_found = []
    lines = text.split('\n')
    
    for search_name in search_names:
        # Look for the project name in the text
        if search_name in text:
            project_info = {
                'Project_Name': search_name,
                'status': '',
                'topic': '',
                'type': '',
                'st': '',
                'et': ''
            }
            
            # Determine type from project name
            if 'FEMA' in search_name or 'CalOES' in search_name or 'CalJPIA' in search_name:
                project_info['type'] = 'disaster'
            else:
                project_info['type'] = 'capital'
            
            # Extract topics from project name
            topics = []
            if 'emergency' in search_name.lower():
                topics.append('emergency warning')
            if 'FEMA' in search_name:
                topics.append('FEMA')
            if 'drain' in search_name.lower() or 'storm' in search_name.lower():
                topics.append('drainage')
            if 'road' in search_name.lower():
                topics.append('road')
            if 'siren' in search_name.lower() or 'warning' in search_name.lower():
                topics.append('emergency warning')
            if 'park' in search_name.lower():
                topics.append('park')
            if 'bridge' in search_name.lower():
                topics.append('bridge')
            if 'culvert' in search_name.lower():
                topics.append('drainage')
            project_info['topic'] = ', '.join(topics)
            
            # Look for status information near the project name in the text
            text_lower = text.lower()
            name_lower = search_name.lower()
            
            # Check for status keywords in the entire document
            status_indicators = [
                ('design', 'design'),
                ('construction', 'construction'),
                ('completed', 'completed'),
                ('not started', 'not started'),
                ('advertise', 'design'),
                ('begin construction', 'construction'),
                ('complete construction', 'construction')
            ]
            
            for keyword, status in status_indicators:
                if keyword in text_lower:
                    project_info['status'] = status
                    break
            
            # Look for dates
            date_matches = re.findall(r'(Spring|Summer|Fall|Winter)[\s-](\d{4})', text, re.IGNORECASE)
            if date_matches:
                project_info['st'] = date_matches[0][1] + '-' + date_matches[0][0].title()
                if len(date_matches) > 1:
                    project_info['et'] = date_matches[-1][1] + '-' + date_matches[-1][0].title()
            
            projects_found.append(project_info)
    
    return projects_found

# Extract project information from all documents
all_project_info = []
for doc in civic_docs:
    projects = extract_project_info(doc['text'], project_names_from_funding)
    all_project_info.extend(projects)

print('Extracted project info for', len(all_project_info), 'projects')

# Create a lookup for project information
project_info_lookup = {}
for proj in all_project_info:
    if proj['Project_Name'] not in project_info_lookup:
        project_info_lookup[proj['Project_Name']] = proj

# Combine funding data with project information
final_results = []
for funding_rec in funding_records:
    proj_name = funding_rec['Project_Name']
    
    # Get project info
    proj_info = project_info_lookup.get(proj_name, {})
    
    final_results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding_rec['Funding_Source'],
        'Amount': int(funding_rec['Amount']),
        'Status': proj_info.get('status', 'Unknown'),
        'Type': proj_info.get('type', 'Unknown'),
        'Topic': proj_info.get('topic', 'None')
    })

# Sort by amount descending
final_results.sort(key=lambda x: x['Amount'], reverse=True)

# Build output
output_text = 'Emergency/FEMA Related Projects:\n\n'
for r in final_results:
    output_text += 'Project: %s\n' % r['Project_Name']
    output_text += '  Funding Source: %s\n' % r['Funding_Source']
    output_text += '  Amount: $%s\n' % r['Amount']
    output_text += '  Status: %s\n' % r['Status']
    output_text += '  Type: %s\n' % r['Type']
    output_text += '  Topic: %s\n\n' % r['Topic']

print('__RESULT__:')
print(json.dumps(output_text))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.query_db:42': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
