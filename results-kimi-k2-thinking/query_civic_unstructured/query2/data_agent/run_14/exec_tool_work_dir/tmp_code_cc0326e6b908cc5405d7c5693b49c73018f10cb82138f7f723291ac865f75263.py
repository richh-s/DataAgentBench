code = """import json

# Read funding and civic documents data
funding_data = json.load(open('var_functions.query_db:22', 'r'))
civic_docs = json.load(open('var_functions.query_db:27', 'r'))

# Find park projects completed in 2022 from civic documents
park_projects_2022 = []
park_keywords = ['park', 'playground', 'bluffs', 'landon', 'arbors', 'benches', 'walkway', 'skate park', 'shade structure']

# Process each document
for doc in civic_docs:
    text = doc['text']
    if '2022' not in text:
        continue
        
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
            
        # Skip headers and markers
        if line.startswith('PAGE') or 'AGENDA' in line or 'PUBLIC WORKS' in line or 'COMMISSION' in line:
            continue
            
        # Check for uppercase project names
        if line.isupper() and len(line) < 200 and ('PROJECT' in line or 'REPAIRS' in line or 'STRUCTURE' in line):
            # Check if park-related and completed in 2022
            context = line
            for j in range(i+1, min(i+15, len(lines))):
                context += ' ' + lines[j]
            
            context_lower = context.lower()
            is_park = any(kw in context_lower for kw in park_keywords)
            completed_2022 = 'completed' in context_lower and '2022' in context
            
            if is_park and completed_2022:
                park_projects_2022.append({'name': line, 'full_text': context})

# Display what we found
print('Park projects completed in 2022:', len(park_projects_2022))
for p in park_projects_2022:
    print('-', p['name'][:60])

# Match with funding records
total_funding = 0
matches = []
funding_lookup = {}

for fund in funding_data:
    funding_lookup[fund['Project_Name'].lower()] = fund

for proj in park_projects_2022:
    proj_name_lower = proj['name'].lower()
    
    # Try to match with funding
    if proj_name_lower in funding_lookup:
        fund = funding_lookup[proj_name_lower]
        amount = int(fund['Amount'])
        total_funding += amount
        matches.append({
            'project': proj['name'],
            'funding': fund['Project_Name'],
            'amount': amount,
            'source': fund['Funding_Source']
        })
    else:
        # Try partial match
        for fund_name_lower, fund in funding_lookup.items():
            if proj_name_lower in fund_name_lower or fund_name_lower in proj_name_lower:
                amount = int(fund['Amount'])
                total_funding += amount
                matches.append({
                    'project': proj['name'],
                    'funding': fund['Project_Name'],
                    'amount': amount,
                    'source': fund['Funding_Source']
                })
                break

print('\nMatched with funding:', len(matches))
print('Total funding:', total_funding)

# Print matches
for m in matches:
    print('-', m['project'][:50], ': $', m['amount'])

# Create result
result = {
    'total_funding_for_park_projects_completed_in_2022': total_funding,
    'number_of_matched_projects': len(matches),
    'project_details': matches
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '62', 'Project_Name': 'Michael Landon Center HVAC Replacement Project', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '94', 'Project_Name': 'Trancas Playground Resurfacing', 'Funding_Source': 'Impact Investment Fund', 'Amount': '90000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '63', 'Project_Name': 'Michael Landon Center Roof Replacement Project', 'Funding_Source': 'Green Energy Fund', 'Amount': '60000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}], 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json'}

exec(code, env_args)
