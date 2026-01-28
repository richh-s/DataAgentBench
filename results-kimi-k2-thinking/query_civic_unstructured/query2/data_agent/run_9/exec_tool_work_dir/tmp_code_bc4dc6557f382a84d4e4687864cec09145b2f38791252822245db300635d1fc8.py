code = """import json

# Load both datasets
file_path = locals()['var_functions.query_db:18']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

funding_data = locals()['var_functions.query_db:20']

print('Documents loaded:', len(civic_docs))
print('Funding records loaded:', len(funding_data))

# Find park projects from civic docs that were completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for specific patterns of park projects completed in 2022
    if all(keyword in text for keyword in ['Park', '2022']):
        # Check for known project completions
        if 'Bluffs Park Shade Structure' in text and 'Construction was completed November 2022' in text:
            if not any(p['Project_Name'] == 'Bluffs Park Shade Structure' for p in park_projects):
                park_projects.append({
                    'Project_Name': 'Bluffs Park Shade Structure',
                    'source': filename
                })
        
        # Extract other park projects
        lines = text.split('\n')
        for line in lines:
            if 'Park' in line and len(line.strip()) > 10:
                clean_line = line.strip()
                # Skip header/footer lines
                if any(skip in clean_line for skip in ['Page', 'Agenda', 'Meeting', 'Commission']):
                    continue
                # Look for project name patterns
                if any(keyword in clean_line for keyword in ['Repair', 'Project', 'Structure', 'Improvement', 'Walkway', 'Shade', 'Playground']):
                    # Check if already added
                    if not any(p['Project_Name'] == clean_line for p in park_projects):
                        park_projects.append({
                            'Project_Name': clean_line,
                            'source': filename
                        })

print('Park projects found:', len(park_projects))
for p in park_projects:
    print('-', p['Project_Name'])

# Match with funding data
funding_dict = {f['Project_Name'].lower(): f for f in funding_data}

matched = []
total = 0

for proj in park_projects:
    name = proj['Project_Name']
    name_lower = name.lower()
    
    # Try to find matching funding
    for funded_name, funding_info in funding_dict.items():
        if funded_name in name_lower or name_lower in funded_name:
            amount = int(funding_info['Amount'])
            matched.append({
                'project': name,
                'funding': amount,
                'source': funding_info['Funding_Source']
            })
            total += amount
            break

print('\nMatched with funding:', len(matched))
for m in matched:
    print(f'- {m["project"]}: ${m["funding"]}')

print('\nTotal funding:', total)

result = {
    'total_funding': total,
    'matches': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}]}

exec(code, env_args)
