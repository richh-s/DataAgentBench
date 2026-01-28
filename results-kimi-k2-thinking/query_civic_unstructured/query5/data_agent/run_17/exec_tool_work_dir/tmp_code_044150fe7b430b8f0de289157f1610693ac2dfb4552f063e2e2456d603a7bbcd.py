code = """import json, re

# Load the data from the stored file paths
civic_path = locals().get('var_functions.query_db:26')
funding_path = locals().get('var_functions.query_db:32')

# Read civic documents
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Read funding data  
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Civic docs loaded:', len(civic_docs))
print('Funding records loaded:', len(funding_data))

# Create mapping of disaster projects to their funding amounts
disaster_funding = {}
for f in funding_data:
    disaster_funding[f['Project_Name']] = int(f['Amount'])

# Find disaster projects that started in 2022 from civic docs
projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for disaster project names with 2022 dates
    # Pattern: project name containing disaster indicators near 2022 year references
    for line in text.split('\n'):
        line = line.strip()
        # Check if it is a disaster project line
        if any(indicator in line for indicator in ['(FEMA', '(CalJPIA', '(CalOES']):
            # Look for 2022 in the surrounding context
            if '2022' in text or '2022' in line:
                # Clean and store
                clean_name = re.sub('\s+', ' ', line).strip()
                projects_2022.append(clean_name)

# Remove duplicates
unique_projects = list(set(projects_2022))
print('Unique disaster projects with 2022 references:', len(unique_projects))

# Match with funding data and calculate total
total_funding = 0
matched_count = 0
for proj in unique_projects:
    for fund_name, amount in disaster_funding.items():
        if proj in fund_name or fund_name in proj:
            total_funding += amount
            matched_count += 1

print('Matched projects:', matched_count)
print('Total 2022 disaster funding:', total_funding)

# Return result in required format
result = {'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': [{'total_disaster_funding': '1410000'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:34': [{'total_disaster_funding': '1410000'}]}

exec(code, env_args)
