code = """import json

# Load the data from the variable references
funding_path = var_functions.query_db:22
civic_path = var_functions.query_db:27

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Records loaded - Funding:', len(funding_data), 'Civic docs:', len(civic_docs))

# Identify park projects completed in 2022
park_projects_2022 = []
keywords = ['park', 'playground', 'bluffs', 'landon', 'arbors', 'benches', 'walkway', 'skate park', 'shade structure']

for doc in civic_docs:
    text = doc['text']
    if '2022' not in text or 'completed' not in text.lower():
        continue
        
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        i += 1
        
        if not line or len(line) < 10:
            continue
            
        # Skip headers
        if any(marker in line for marker in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION']):
            continue
            
        # Look for project names (uppercase)
        if line.isupper() and len(line) < 200:
            # Check context
            context_start = max(0, i-5)
            context_end = min(len(lines), i+15)
            context = ' '.join(lines[context_start:context_end])
            
            ctx_lower = context.lower()
            is_park = any(kw in ctx_lower for kw in keywords)
            completed_2022 = 'completed' in ctx_lower and '2022' in context
            
            if is_park and completed_2022:
                park_projects_2022.append({'name': line, 'context': context})

print('\nPark projects from 2022:', len(park_projects_2022))
for p in park_projects_2022:
    print('- ' + p['name'])

# Match with funding
funding_lookup = {f['Project_Name'].lower(): f for f in funding_data}
total_funding = 0
matches = []

for proj in park_projects_2022:
    proj_key = proj['name'].lower()
    
    if proj_key in funding_lookup:
        fund = funding_lookup[proj_key]
        amount = int(fund['Amount'])
        total_funding += amount
        matches.append([proj['name'], fund['Project_Name'], amount, fund['Funding_Source']])
    else:
        # Fuzzy match
        for fund_key, fund in funding_lookup.items():
            if proj_key in fund_key or fund_key in proj_key:
                amount = int(fund['Amount'])
                total_funding += amount
                matches.append([proj['name'], fund['Project_Name'], amount, fund['Funding_Source']])
                break

print('\nMatched ' + str(len(matches)) + ' projects')
print('Total funding: ' + str(total_funding))

for m in matches:
    print('- ' + m[0] + ': $' + str(m[2]) + ' (' + m[3] + ')')

# Return final answer
result = {
    'total_funding_for_park_projects_completed_in_2022': total_funding,
    'number_of_matched_projects': len(matches),
    'details': matches
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '62', 'Project_Name': 'Michael Landon Center HVAC Replacement Project', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '94', 'Project_Name': 'Trancas Playground Resurfacing', 'Funding_Source': 'Impact Investment Fund', 'Amount': '90000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '63', 'Project_Name': 'Michael Landon Center Roof Replacement Project', 'Funding_Source': 'Green Energy Fund', 'Amount': '60000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}], 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json'}

exec(code, env_args)
