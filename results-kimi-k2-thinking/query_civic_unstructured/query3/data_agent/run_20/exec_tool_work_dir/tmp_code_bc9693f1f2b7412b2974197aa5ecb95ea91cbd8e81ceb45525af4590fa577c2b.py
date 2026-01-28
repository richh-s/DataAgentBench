code = """import json
import re

# Load all funding data
funding_data = locals()['var_functions.query_db:6'] if not isinstance(locals()['var_functions.query_db:6'], str) else json.load(open(locals()['var_functions.query_db:6']))

# Load civic documents
civic_docs = locals()['var_functions.query_db:4'] if not isinstance(locals()['var_functions.query_db:4'], str) else json.load(open(locals()['var_functions.query_db:4']))

# Step 1: Extract all FEMA/emergency related funding
fema_funding = []
pattern = re.compile(r'(emergency|fema)', re.IGNORECASE)

for record in funding_data:
    if pattern.search(record['Project_Name']):
        fema_funding.append(record)

# Step 2: Extract projects from civic documents
projects_from_docs = []

for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    
    # Look for Disaster Recovery Projects section specifically
    if 'Disaster Recovery Projects' in text or 'FEMA' in text:
        # Extract project names that appear with FEMA indicators
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Look for project names with FEMA/CalOES/CalJPIA
            if any(indicator in line for indicator in ['(FEMA', 'FEMA/CalOES', 'CalJPIA', 'Emergency']):
                # Clean up the project name
                project_name = line.split('(cid:')[0].strip()
                project_name = re.sub(r'\s+', ' ', project_name)
                
                if len(project_name) > 10:  # Filter out short lines
                    # Try to find status in nearby lines
                    status = 'Unknown'
                    context_window = lines[max(0, i-5):min(len(lines), i+5)]
                    context = ' '.join(context_window).lower()
                    
                    if 'design' in context:
                        status = 'Design'
                    elif 'construction' in context and 'completed' in context:
                        status = 'Completed'
                    elif 'construction' in context:
                        status = 'Construction'
                    elif 'not started' in context:
                        status = 'Not Started'
                    
                    # Determine type
                    project_type = 'Disaster'
                    if 'capital' in context:
                        project_type = 'Capital'
                    
                    projects_from_docs.append({
                        'Project_Name': project_name,
                        'Status': status,
                        'Type': project_type,
                        'Document': filename
                    })

# Step 3: Match funding with project information
results = []

# Create a lookup for projects from documents
project_lookup = {}
for proj in projects_from_docs:
    # Normalize name for matching
    norm_name = proj['Project_Name'].lower().replace('(fema', '').replace('fema/caloes', '').replace('caljpia', '').strip()
    norm_name = re.sub(r'[^a-z0-9\s]', '', norm_name)
    norm_name = re.sub(r'\s+', ' ', norm_name)
    project_lookup[norm_name] = proj

# Match funding records with project info
for fund in fema_funding:
    fund_name = fund['Project_Name']
    
    # Normalize funding project name
    norm_fund = fund_name.lower().replace('(fema', '').replace('fema/caloes', '').replace('caljpia', '').strip()
    norm_fund = re.sub(r'[^a-z0-9\s]', '', norm_fund)
    norm_fund = re.sub(r'\s+', ' ', norm_fund)
    
    # Find matching project
    matched_project = None
    for proj_key, proj in project_lookup.items():
        if (norm_fund in proj_key or proj_key in norm_fund or 
            fund['Project_Name'] == proj['Project_Name']):
            matched_project = proj
            break
    
    if matched_project:
        results.append({
            'Project_Name': fund_name,
            'Status': matched_project['Status'],
            'Type': matched_project['Type'],
            'Funding_Source': fund['Funding_Source'],
            'Amount': int(fund['Amount'])
        })
    else:
        # Add funding record even if no project doc found
        results.append({
            'Project_Name': fund_name,
            'Status': 'Not found in documents',
            'Type': 'Unknown (FEMA/Disaster Likely)',
            'Funding_Source': fund['Funding_Source'],
            'Amount': int(fund['Amount'])
        })

# Sort by amount
disaster_projects = [r for r in results if 'FEMA' in r['Project_Name'] or 'Disaster' in r['Type']]
disaster_projects.sort(key=lambda x: x['Amount'], reverse=True)

print('__RESULT__:')
print(json.dumps(disaster_projects[:30], indent=2))"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'civic_docs_count': 19, 'funding_count': 500, 'civic_doc_keys': ['_id', 'filename', 'text'], 'sample_funding': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}}, 'var_functions.execute_python:14': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000, 'Status': 'Unknown', 'Type': 'Unknown'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000, 'Status': 'Unknown', 'Type': 'Unknown'}]}

exec(code, env_args)
