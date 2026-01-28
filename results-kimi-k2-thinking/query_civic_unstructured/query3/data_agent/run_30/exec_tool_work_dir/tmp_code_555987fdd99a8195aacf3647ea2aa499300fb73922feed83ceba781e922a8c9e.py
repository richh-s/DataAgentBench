code = """import json

# Load funding data from file
funding_path = locals()['var_functions.query_db:2']
with open(funding_path) as f:
    funding_data = json.load(f)

# Load civic documents data from file
civic_path = locals()['var_functions.query_db:5']
with open(civic_path) as f:
    civic_data = json.load(f)

# Step 1: Find projects with FEMA or emergency in the funding table
results = []

for record in funding_data:
    project_name = record['Project_Name']
    has_fema = 'FEMA' in project_name
    has_emergency = 'emergency' in project_name.lower()
    
    if has_fema or has_emergency:
        results.append({
            'Project_Name': project_name,
            'Funding_Source': record['Funding_Source'],
            'Amount': int(record['Amount']),
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

# Step 2: Try to find status information in civic documents
for doc in civic_data:
    text = doc.get('text', '')
    
    # Look for each project in the text
    for project in results:
        project_name = project['Project_Name']
        
        if project_name in text:
            text_lower = text.lower()
            
            # Try to determine status based on keywords
            if 'design' in text_lower and ('complete' in text_lower or 'finalize' in text_lower):
                project['Status'] = 'design'
            elif 'construction' in text_lower:
                if 'under' in text_lower or 'begin' in text_lower:
                    project['Status'] = 'construction'
                elif 'complete' in text_lower:
                    project['Status'] = 'completed'
            elif 'completed' in text_lower:
                project['Status'] = 'completed'

# Remove duplicates
clean_results = []
seen_names = set()

for project in results:
    if project['Project_Name'] not in seen_names:
        seen_names.add(project['Project_Name'])
        clean_results.append(project)

# Sort by amount descending
clean_results.sort(key=lambda x: x['Amount'], reverse=True)

# Prepare output
output = []
for project in clean_results:
    output.append({
        'Project_Name': project['Project_Name'],
        'Funding_Source': project['Funding_Source'],
        'Amount': project['Amount'],
        'Status': project['Status'],
        'Topic': project['Topic']
    })

print('Total projects:', len(output))
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_preview': 'file_storage/functions.query_db:2.json', 'civic_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:24': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:34': {'count': 20, 'sample': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:44': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}]}

exec(code, env_args)
