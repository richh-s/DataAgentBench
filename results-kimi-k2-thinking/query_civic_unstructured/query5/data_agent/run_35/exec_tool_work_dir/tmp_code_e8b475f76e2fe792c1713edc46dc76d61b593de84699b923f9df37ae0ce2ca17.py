code = """import json

# Load the civic documents data
docs_file = '/tmp/tmpy4j0_8x6.json'
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load all funding data
funding_file = '/tmp/tmpj4_6s1y9.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create disaster funding lookup
disaster_funding = {}
for record in funding_data:
    proj_name = record['Project_Name']
    upper_name = proj_name.upper()
    if 'FEMA' in upper_name or 'CALOES' in upper_name or 'CALJPIA' in upper_name:
        amount = int(record['Amount'])
        disaster_funding[proj_name] = amount

print('Disaster projects in funding database:', len(disaster_funding))

# Extract projects from documents with 2022 start dates
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 5 or len(line) > 200:
            continue
        
        # Skip headers and metadata
        skip_markers = ['Page', 'Agenda', 'Prepared by', 'Approved by', 'Subject:', 
                       'RECOMMENDED', 'DISCUSSION', 'To:', 'Chair', 'Date prepared',
                       'Public Works', 'Commission', 'Item', '===', '---']
        if any(marker in line for marker in skip_markers):
            continue
        if line.startswith('(') or line.startswith('•') or line.startswith('■'):
            continue
        
        # Check if disaster-related
        line_upper = line.upper()
        is_disaster = 'FEMA' in line_upper or 'CALOES' in line_upper or 'CALJPIA' in line_upper
        
        # Check if starts with 2022
        starts_2022 = line.startswith('2022')
        
        # Look for 2022 in nearby context
        found_2022_start = False
        if is_disaster or starts_2022:
            window_start = max(0, i-2)
            window_end = min(len(lines), i+5)
            
            for j in range(window_start, window_end):
                context = lines[j]
                if '2022' in context:
                    # Check if this is about starting/schedule
                    context_lower = context.lower()
                    if any(kw in context_lower for kw in ['begin', 'start', 'advertise', 'design', 'construction']):
                        found_2022_start = True
                        break
        
        # Include if disaster-related and (starts with 2022 or has 2022 start in context)
        if is_disaster and (starts_2022 or found_2022_start):
            disaster_projects_2022.append(line)

print('Disaster projects starting in 2022 found in documents:', len(disaster_projects_2022))
for proj in disaster_projects_2022:
    print('-', proj)

# Match with funding data
matched_projects = []
total_funding = 0

for project_name in disaster_projects_2022:
    # Direct match
    if project_name in disaster_funding:
        amount = disaster_funding[project_name]
        matched_projects.append({'name': project_name, 'amount': amount})
        total_funding += amount
    else:
        # Try partial matching
        for fund_name, amount in disaster_funding.items():
            # Check if base names match (without suffixes)
            base_proj = project_name.split('(')[0].strip()
            base_fund = fund_name.split('(')[0].strip()
            if base_proj == base_fund:
                matched_projects.append({'name': fund_name, 'amount': amount})
                total_funding += amount
                break

print('\nMatched projects with funding:')
for proj in matched_projects:
    print(f"- {proj['name']}: ${proj['amount']:,}")

print(f'\nTotal funding for disaster projects starting in 2022: ${total_funding:,}')

result = {
    'total_funding': total_funding,
    'project_count': len(matched_projects),
    'projects': matched_projects
}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.list_db:24': ['civic_docs'], 'var_functions.query_db:26': [{'count': '500'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:34': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
