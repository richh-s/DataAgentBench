code = """import json, re

# Load the data
funding_records = globals()['var_functions.query_db:42']

civic_docs_file = globals()['var_functions.query_db:0']
civic_docs = json.load(open(civic_docs_file))

# Initialize results list
results = []

# For each funding record, try to find status information in civic documents
for funding_rec in funding_records:
    proj_name = funding_rec['Project_Name']
    
    # Initialize project info with defaults
    status = 'Unknown'
    project_type = 'disaster'
    topic = ''
    
    # Determine type and topics from project name
    if 'FEMA' in proj_name or 'CalOES' in proj_name or 'CalJPIA' in proj_name:
        project_type = 'disaster'
    else:
        project_type = 'capital'
    
    # Extract topics from project name
    topics = []
    if 'emergency' in proj_name.lower():
        topics.append('emergency warning')
    if 'FEMA' in proj_name:
        topics.append('FEMA')
    if 'drain' in proj_name.lower() or 'storm' in proj_name.lower() or 'culvert' in proj_name.lower():
        topics.append('drainage')
    if 'road' in proj_name.lower():
        topics.append('road')
    if 'siren' in proj_name.lower() or 'warning' in proj_name.lower():
        topics.append('emergency warning')
    if 'park' in proj_name.lower():
        topics.append('park')
    if 'bridge' in proj_name.lower():
        topics.append('bridge')
    if 'irrigation' in proj_name.lower():
        topics.append('irrigation')
    topic = ', '.join(topics) if topics else 'None'
    
    # Search for status in all civic documents
    project_lower = proj_name.lower()
    for doc in civic_docs:
        doc_text = doc['text']
        if proj_name in doc_text:
            # Found the project, now look for status keywords
            doc_lower = doc_text.lower()
            
            # Check for design status
            if 'design' in doc_lower:
                status = 'design'
                break
            # Check for construction status
            elif 'construction' in doc_lower:
                status = 'construction'
                break
            # Check for completed status
            elif 'completed' in doc_lower:
                status = 'completed'
                break
            # Check for not started
            elif 'not started' in doc_lower:
                status = 'not started'
                break
    
    # Add result
    results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding_rec['Funding_Source'],
        'Amount': int(funding_rec['Amount']),
        'Status': status,
        'Type': project_type,
        'Topic': topic
    })

# Sort by amount descending
results.sort(key=lambda x: x['Amount'], reverse=True)

# Build final response text
response = ['Emergency_FEMA Related Projects: Found %d projects' % len(results), '']
for r in results:
    response.append('Project: %s' % r['Project_Name'])
    response.append('  Funding Source: %s' % r['Funding_Source'])
    response.append('  Amount: $%s' % r['Amount'])
    response.append('  Status: %s' % r['Status'])
    response.append('  Type: %s' % r['Type'])
    response.append('  Topic: %s' % r['Topic'])
    response.append('')

final_output = '\n'.join(response)

result_dict = {
    'count': len(results),
    'response': final_output,
    'projects': results
}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:18': {'civic_docs': 5, 'funding_records': 500, 'sample_civic_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.query_db:42': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
