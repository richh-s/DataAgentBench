code = """import json, re, os
print('Starting analysis...')

# Load civic documents
civic_path = locals().get('var_functions.query_db:26')
print('Civic docs path:', type(civic_path))

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Load disaster-related funding data
funding_path = locals().get('var_functions.query_db:32')
print('Funding data path:', type(funding_path))

if isinstance(funding_path, str) and funding_path.endswith('.json'):
    with open(funding_path, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = []

print('Civic documents:', len(civic_docs))
print('Disaster funding records:', len(funding_data))

# Extract disaster projects and their 2022 start dates from documents
disaster_projects_2022 = []
disaster_project_names = set()  # To track unique names

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        
        # Check if line is a likely project name (not indented, title-like)
        if (len(line) > 5 and 
            not line.startswith('•') and 
            not line.startswith('-') and
            not line.startswith('□') and
            not re.match(r'^\s+', lines[i]) and  # Not indented
            (line[0].isupper() or line[0].isdigit())):
            
            # Check if disaster-related
            is_disaster = any(indicator in line for indicator in [
                '(FEMA', '(CalJPIA', '(CalOES', 'FEMA/CalOES'
            ])
            
            if is_disaster:
                # Look ahead for 2022 dates
                for j in range(i, min(i+8, len(lines))):
                    context_line = lines[j]
                    if '2022' in context_line:
                        # Look for phrases indicating start/beginning
                        if any(word in context_line for word in ['Start', 'start', 'Begin', 'begin', 'Advertise', 'Design']):
                            cleaned_name = re.sub(r'\s+', ' ', line).strip()
                            if cleaned_name not in disaster_project_names:
                                disaster_projects_2022.append({
                                    'name': cleaned_name,
                                    'date_context': context_line.strip()[:100]
                                })
                                disaster_project_names.add(cleaned_name)
                        break
        i += 1

print('Found', len(disaster_projects_2022), 'unique disaster projects with 2022 dates')

# Map project names to funding data
project_to_funding = {}
for f in funding_data:
    proj_name = f['Project_Name']
    amount = int(f['Amount'])
    project_to_funding[proj_name.lower()] = amount

# Match projects and sum funding
total_2022 = 0
matches = []
for project in disaster_projects_2022:
    proj_name = project['name']
    # Try to match with variations
    for funding_name, amount in project_to_funding.items():
        # Direct match or partial match
        if (proj_name.lower() in funding_name or 
            funding_name in proj_name.lower() or
            re.sub(r' \(FEMA[^)]*\)', '', proj_name).lower().strip() in funding_name or
            re.sub(r' \(CalOES[^)]*\)', '', proj_name).lower().strip() in funding_name):
            total_2022 += amount
            matches.append({
                'document_project': proj_name,
                'funding_project': [k for k,v in project_to_funding.items() if v == amount][0],
                'amount': amount
            })
            break

print('Matched projects:', len(matches))
print('Total funding for 2022 disaster projects:', total_2022)

# If no matches found, let's check what's in the funding data
if len(matches) == 0:
    print('\nDisaster project names in funding DB:')
    for f in funding_data:
        print('  -', f['Project_Name'])
    
    print('\nDisaster project names extracted from documents:')
    for p in disaster_projects_2022:
        print('  -', p['name'])

result = {
    'total_2022_disaster_funding': total_2022,
    'matched_projects': matches,
    'total_matches': len(matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': [{'total_disaster_funding': '1410000'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:34': [{'total_disaster_funding': '1410000'}]}

exec(code, env_args)
