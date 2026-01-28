code = """import json
import re

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_data = locals()['var_functions.query_db:22']

print('Loaded {} civic documents and {} funding records'.format(len(civic_docs), len(funding_data)))

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip non-project lines
        skip_terms = ['(', 'page', 'item', 'to:', 'prepared by:', 'subject:', 'recommended action:', 'discussion:', 'capital improvement', 'public works', 'commission meeting']
        if any(term in line.lower() for term in skip_terms):
            continue
        
        # Check if line is a project name
        look_ahead = ' '.join(lines[i+1:i+5]).lower()
        if any(indicator in look_ahead for indicator in ['updates:', 'schedule:', 'complete', 'construction']):
            proj_name = line
            
            # Look for 2022 completion
            for j in range(i, min(i+10, len(lines))):
                check_line = lines[j].strip()
                if '2022' in check_line and 'completed' in check_line.lower():
                    if 'park' in proj_name.lower() or 'park' in check_line.lower():
                        year_match = re.search(r'(202\d)', check_line)
                        year = year_match.group(1) if year_match else '2022'
                        park_projects_2022.append({
                            'Project_Name': proj_name,
                            'completion': check_line,
                            'year': year
                        })
                        break

print('Found {} park projects completed in 2022'.format(len(park_projects_2022)))

# Match with funding
matches = []
total_funding = 0

for project in park_projects_2022:
    proj_name = project['Project_Name']
    
    for funding in funding_data:
        fund_name = funding['Project_Name']
        
        # Exact or close match
        if proj_name.lower().strip() == fund_name.lower().strip() or fund_name.lower().strip() in proj_name.lower().strip():
            amount = int(funding['Amount'])
            matches.append({
                'project': proj_name,
                'funding_name': fund_name,
                'amount': amount,
                'source': funding['Funding_Source']
            })
            total_funding += amount
            break

print('Matched {} projects with total funding ${:,}'.format(len(matches), total_funding))

# Show results
for m in matches:
    print('${:,} - {} ({})'.format(m['amount'], m['funding_name'], m['source']))

# Find specific project: Bluffs Park Shade Structure
print('\nLooking up Bluffs Park Shade Structure manually...')
for funding in funding_data:
    if 'Bluffs Park Shade Structure' in funding['Project_Name']:
        print('Found: ${:,} from {}'.format(int(funding['Amount']), funding['Funding_Source']))

__RESULT__:
json.dumps({
    'park_projects_count': len(park_projects_2022),
    'funding_matches': len(matches),
    'total_funding': total_funding,
    'matches': matches
})"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}]}

exec(code, env_args)
