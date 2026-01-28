code = """import json
import re

# Load all funding data from file
funding_file = locals()['var_functions.query_db:6']
if isinstance(funding_file, str):
    with open(funding_file) as f:
        all_funding = json.load(f)
else:
    all_funding = funding_file

# Filter for FEMA and Emergency related projects
pattern = re.compile(r'(fema|emergency)', re.IGNORECASE)
fema_emergency_funding = [f for f in all_funding if pattern.search(f['Project_Name'])]

# Load civic documents
docs_file = locals()['var_functions.query_db:4']
if isinstance(docs_file, str):
    with open(docs_file) as f:
        civic_docs = json.load(f)
else:
    civic_docs = docs_file

# Extract project information from documents
projects_with_details = []

for doc in civic_docs:
    doc_text = doc['text']
    lines = doc_text.splitlines()
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for FEMA-related project names
        if any(x in line for x in ['(FEMA', 'FEMA/CalOES', 'CalJPIA', 'Emergency']):
            project_name = line.split('(cid:')[0].strip()
            if len(project_name) < 5:
                continue
                
            # Clean up the name
            project_name = re.sub(r'\s+', ' ', project_name)
            if not project_name.endswith('Project'):
                project_name = project_name.replace(' Project', '')
            
            # Determine status from context
            status = 'Unknown'
            context_start = max(0, i-3)
            context_end = min(len(lines), i+6)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if 'design' in context and 'complete' not in context:
                status = 'Design'
            elif 'construction completed' in context or 'notice of completion' in context:
                status = 'Completed'
            elif 'construction' in context:
                status = 'Construction'
            elif 'not started' in context or 'identified' in context:
                status = 'Not Started'
            
            # Determine type
            project_type = 'Disaster'
            if 'capital' in context.lower():
                project_type = 'Capital'
            elif any(x in project_name.lower() for x in ['storm', 'drain', 'slope', 'road', 'street']):
                if 'FEMA' not in project_name:
                    project_type = 'Capital'
            
            projects_with_details.append({
                'Project_Name': project_name,
                'Status_Doc': status,
                'Type_Doc': project_type,
                'Filename': doc['filename']
            })

# Match funding records with project details
matched_results = []

# Create lookup for projects from documents
project_lookup = {re.sub(r'[^a-z0-9\s]', '', item['Project_Name'].lower().replace('(fema', '').strip()): item 
                  for item in projects_with_details}

for fund in fema_emergency_funding:
    fund_proj_name = fund['Project_Name']
    
    # Normalize for matching
    fund_norm = re.sub(r'[^a-z0-9\s]', '', fund_proj_name.lower().replace('(fema', '').strip())
    
    # Find matching project details
    matched = False
    for proj_key, proj_details in project_lookup.items():
        if (fund_norm in proj_key or proj_key in fund_norm or 
            re.sub(r'\s+', ' ', fund_proj_name).strip() == proj_details['Project_Name']):
            matched_results.append({
                'Project_Name': fund_proj_name,
                'Status': proj_details['Status_Doc'],
                'Type': proj_details['Type_Doc'],
                'Funding_Source': fund['Funding_Source'],
                'Amount': int(fund['Amount'])
            })
            matched = True
            break
    
    if not matched:
        # Still include the funding info even if no doc found
        type_guess = 'Disaster' if 'FEMA' in fund_proj_name else 'Unknown'
        matched_results.append({
            'Project_Name': fund_proj_name,
            'Status': 'Not found in documents',
            'Type': type_guess,
            'Funding_Source': fund['Funding_Source'],
            'Amount': int(fund['Amount'])
        })

# Sort by amount descending
matched_results.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(matched_results, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 19, 'funding_count': 500, 'civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:14': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'Unknown', 'Type': 'Unknown'}], 'var_functions.execute_python:18': {'funding_records': 500, 'civic_documents': 19, 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'sample_doc_keys': ['_id', 'filename', 'text']}}

exec(code, env_args)
