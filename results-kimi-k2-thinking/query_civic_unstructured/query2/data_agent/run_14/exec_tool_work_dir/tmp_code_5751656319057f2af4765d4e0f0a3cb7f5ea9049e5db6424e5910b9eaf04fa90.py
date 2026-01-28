code = """import json

# Load funding data
funding_file = open(var_functions.query_db:22, 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Load civic documents
civic_file = open(var_functions.query_db:27, 'r')
civic_docs = json.load(civic_file)
civic_file.close()

# Count total records
print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_docs))

# Find park projects completed in 2022
park_projects_2022 = []
search_terms = ['park', 'playground', 'bluffs', 'landon', 'arbors', 'benches', 'walkway', 'skate park', 'shade structure']

for doc in civic_docs:
    text = doc['text']
    if '2022' not in text:
        continue
    
    text_lower = text.lower()
    if 'completed' not in text_lower:
        continue
    
    # Check if any park keyword appears with 2022 and completed
    for term in search_terms:
        if term in text_lower and '2022' in text:
            # Extract project names if possible
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line.isupper() and len(line) < 200 and (term in line.lower()):
                    # Verify this project was completed in 2022
                    line_lower = line.lower()
                    if 'project' in line_lower or 'repairs' in line_lower or 'structure' in line_lower:
                        park_projects_2022.append(line)

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))
print('\nPark projects completed in 2022:', len(park_projects_2022))
for p in park_projects_2022:
    print('-', p[:60])

# Match with funding records
funding_lookup = {}
for fund in funding_data:
    funding_lookup[fund['Project_Name']] = int(fund['Amount'])

total_funding = 0
matched_count = 0

for proj in park_projects_2022:
    if proj in funding_lookup:
        amount = funding_lookup[proj]
        total_funding += amount
        matched_count += 1
        print(f'Matched: {proj[:50]} - ${amount:,}')

# For projects not directly matched, try keyword matching
if matched_count == 0:
    for proj in park_projects_2022:
        proj_lower = proj.lower()
        for fund_name, amount in funding_lookup.items():
            if proj_lower in fund_name.lower() or fund_name.lower() in proj_lower:
                total_funding += amount
                matched_count += 1
                print(f'Matched via keyword: {proj[:50]} - ${amount:,}')
                break

print('\nFinal results:')
print('Total funding:', total_funding)
print('Matched projects:', matched_count)

# Return final result
result = {
    'total_funding_for_park_projects_completed_in_2022': total_funding,
    'matched_projects': matched_count
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '62', 'Project_Name': 'Michael Landon Center HVAC Replacement Project', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '94', 'Project_Name': 'Trancas Playground Resurfacing', 'Funding_Source': 'Impact Investment Fund', 'Amount': '90000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '63', 'Project_Name': 'Michael Landon Center Roof Replacement Project', 'Funding_Source': 'Green Energy Fund', 'Amount': '60000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}], 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json'}

exec(code, env_args)
