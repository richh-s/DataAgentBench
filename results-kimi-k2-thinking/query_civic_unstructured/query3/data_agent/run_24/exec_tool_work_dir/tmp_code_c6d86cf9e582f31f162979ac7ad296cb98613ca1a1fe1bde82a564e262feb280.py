code = """import json

# Load the MongoDB documents
mongo_file = var_functions.query_db:26
with open(mongo_file, 'r') as f:
    mongo_docs = json.load(f)

print('MongoDB documents loaded:', len(mongo_docs))

# Load the funding data
funding_file = var_functions.query_db:28
funding_data = funding_file  # This is already a Python object (list)

print('Funding records loaded:', len(funding_data))

# Extract project statuses from MongoDB documents
project_status_map = {}

for doc in mongo_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    section_type = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Detect section headers
        if 'Design' in line and ('Capital' in line or 'Disaster' in line):
            section_type = 'design'
            continue
        elif 'Construction' in line and ('Capital' in line or 'Disaster' in line):
            section_type = 'construction'
            continue
        elif 'Not Started' in line and ('Capital' in line or 'Disaster' in line):
            section_type = 'not_started'
            continue
        
        # Extract project names from section content
        if section_type and len(line) > 10:
            # Skip markers
            if line.startswith('(') or line.startswith('•') or line.startswith('■'):
                continue
            if 'Updates:' in line or 'Schedule:' in line or 'Project Description:' in line:
                continue
            if 'Page' in line:
                continue
            
            # Check if next lines indicate this is a project name
            next_segment = '\n'.join(lines[i:i+4])
            if 'Updates:' in next_segment or 'Schedule:' in next_segment or 'Project Description:' in next_segment:
                # Clean project name (remove parenthetical markers for matching)
                clean_name = line.split('(')[0].strip()
                
                # Map status
                if section_type == 'construction':
                    status = 'completed'
                else:
                    status = section_type
                
                project_status_map[clean_name] = status

print('Project status map created with', len(project_status_map), 'entries')
print('Sample entries:')
for name, status in list(project_status_map.items())[:10]:
    print(f'  {name}: {status}')

# Match funding data with statuses
results = []

for rec in funding_data:
    project_name = rec['Project_Name']
    funding_source = rec['Funding_Source']
    amount = int(rec['Amount'])
    
    # Find matching status - look for exact match or parent project name
    status = 'unknown'
    
    # Direct match with full project name
    if project_name in project_status_map:
        status = project_status_map[project_name]
    else:
        # Try matching with parenthetical parts removed
        base_name = project_name.split('(')[0].strip()
        if base_name in project_status_map:
            status = project_status_map[base_name]
        else:
            # Try fuzzy matching with existing project names
            for mapped_name, mapped_status in project_status_map.items():
                if base_name.lower() in mapped_name.lower() or mapped_name.lower() in base_name.lower():
                    status = mapped_status
                    break
    
    results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_source,
        'Amount': amount,
        'Status': status
    })

print('\nFinal results count:', len(results))
print('Results preview:')
for r in results[:10]:
    print(f"  {r['Project_Name'][:60]} | ${r['Amount']} | {r['Funding_Source']} | {r['Status']}")

# Return results
final_result = results
print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}]}

exec(code, env_args)
