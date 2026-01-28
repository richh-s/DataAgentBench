code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:2']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
civic_file = locals()['var_functions.query_db:5']
with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Step 1: Find all funding records with FEMA or emergency
fema_projects = []
for item in funding_data:
    proj_name = item['Project_Name']
    if 'FEMA' in proj_name or 'emergency' in proj_name.lower():
        fema_projects.append({
            'Project_Name': proj_name,
            'Funding_Source': item['Funding_Source'],
            'Amount': int(item['Amount']),
            'Status': 'unknown',
            'Topic': 'FEMA,emergency'
        })

# Step 2: Try to extract status from civic documents
# Create a map of project names to their status based on document structure
status_map = {}

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Track what section we're in
    current_section = None
    
    for line in lines:
        line_lower = line.strip().lower()
        
        # Identify sections
        if 'capital improvement projects (design)' in line_lower:
            current_section = 'design'
        elif 'capital improvement projects (construction)' in line_lower:
            current_section = 'construction'
        elif 'capital improvement projects (not started)' in line_lower:
            current_section = 'not started'
        elif any(keyword in line_lower for keyword in ['disaster recovery', 'fema project']):
            # For FEMA/disaster projects, use more specific detection
            for fund_proj in fema_projects:
                if fund_proj['Project_Name'] in text:
                    # Look for status in the surrounding context
                    if 'construction' in text.lower() and ('under' in text.lower() or 'current' in text.lower()):
                        status_map[fund_proj['Project_Name']] = 'construction'
                    elif 'design' in text.lower():
                        status_map[fund_proj['Project_Name']] = 'design'
                    elif 'completed' in text.lower():
                        status_map[fund_proj['Project_Name']] = 'completed'

# Step 3: Combine results
final_results = []
for proj in fema_projects:
    proj_name = proj['Project_Name']
    status = status_map.get(proj_name, 'unknown')
    final_results.append({
        'Project_Name': proj_name,
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': status,
        'Topic': proj['Topic']
    })

# Sort by amount descending
final_results.sort(key=lambda x: x['Amount'], reverse=True)

output = []
for proj in final_results:
    output.append({
        'Project_Name': proj['Project_Name'],
        'Funding_Source': proj['Funding_Source'],
        'Amount': proj['Amount'],
        'Status': proj['Status'],
        'Topic': proj['Topic']
    })

print('Projects found:', len(output))
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:22': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>", 'funding_preview': 'file_storage/functions.query_db:2.json', 'civic_preview': 'file_storage/functions.query_db:5.json'}, 'var_functions.execute_python:24': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:34': {'count': 20, 'sample': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}]}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:44': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'unknown', 'Topic': 'FEMA,emergency'}]}

exec(code, env_args)
