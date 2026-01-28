code = """import json

# Read funding data from the stored path
with open('var_functions.query_db:22', 'r') as f:
    park_funding_data = json.load(f)

# Read civic documents from the stored path
with open('var_functions.query_db:27', 'r') as f:
    civic_docs = json.load(f)

print('Funding records loaded:', len(park_funding_data))
print('Civic documents loaded:', len(civic_docs))

# Process documents to find park projects completed in 2022
park_projects_2022 = []
park_keywords = ['park', 'playground', 'bluffs', 'landon', 'arbors', 'benches', 'walkway', 'skate park', 'shade structure']

for doc in civic_docs:
    text = doc['text']
    if '2022' in text and ('completed' in text.lower() or 'completion' in text.lower()):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if not line or len(line) < 10:
                continue
                
            # Skip headers
            if any(skip in line for skip in ['PAGE', 'AGENDA', 'PUBLIC WORKS', 'COMMISSION', 'CITY OF']):
                continue
                
            # Check for project names (uppercase lines)
            if line.isupper() and len(line) < 200 and ('PROJECT' in line or 'REPAIRS' in line or 'STRUCTURE' in line):
                # Look ahead for context
                context = line + '\n'
                for j in range(i+1, min(i+20, len(lines))):
                    context += lines[j] + '\n'
                
                context_lower = context.lower()
                
                # Check if park-related and completed in 2022
                is_park = any(kw in context_lower for kw in park_keywords)
                completed_2022 = ('completed' in context_lower or 'completion' in context_lower) and '2022' in context
                
                if is_park and completed_2022:
                    park_projects_2022.append({
                        'name': line,
                        'context': context
                    })

print('\nPark projects completed in 2022:', len(park_projects_2022))
for p in park_projects_2022:
    print('-', p['name'])

# Match with funding records
total_funding = 0
matched = []

# Build funding lookup
funding_lookup = {}
for fund in park_funding_data:
    funding_lookup[fund['Project_Name'].lower()] = fund

for proj in park_projects_2022:
    proj_name_lower = proj['name'].lower()
    
    # Direct match
    if proj_name_lower in funding_lookup:
        fund = funding_lookup[proj_name_lower]
        amount = int(fund['Amount'])
        total_funding += amount
        matched.append({
            'project': proj['name'],
            'funding': fund['Project_Name'],
            'amount': amount,
            'source': fund['Funding_Source']
        })
        continue
    
    # Fuzzy match
    for fund_name_lower, fund in funding_lookup.items():
        if proj_name_lower in fund_name_lower or fund_name_lower in proj_name_lower:
            amount = int(fund['Amount'])
            total_funding += amount
            matched.append({
                'project': proj['name'],
                'funding': fund['Project_Name'],
                'amount': amount,
                'source': fund['Funding_Source']
            })
            break

print('\nMatched projects:', len(matched))
print('Total funding:', total_funding)

for m in matched:
    print('-', m['project'], ': $', m['amount'], '(', m['source'], ')')

result = {
    'total_funding_for_park_projects_2022': total_funding,
    'number_of_projects_matched': len(matched),
    'projects': matched
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '62', 'Project_Name': 'Michael Landon Center HVAC Replacement Project', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '94', 'Project_Name': 'Trancas Playground Resurfacing', 'Funding_Source': 'Impact Investment Fund', 'Amount': '90000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '63', 'Project_Name': 'Michael Landon Center Roof Replacement Project', 'Funding_Source': 'Green Energy Fund', 'Amount': '60000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}], 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json'}

exec(code, env_args)
