code = """import json
import re

# Load civic documents data
civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_data = locals()['var_functions.query_db:22']

print('Analyzing {} civic documents'.format(len(civic_docs)))
print('Analyzing {} park funding records'.format(len(funding_data)))

# Find park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for completion statements related to park projects in 2022
    # Pattern: Project name followed by completion info containing 2022
    lines = text.split('\n')
    
    project_name = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip lines that are not project names
        skip_patterns = ['(', '●', '■', 'page', 'item', 'to:', 'prepared by:', 'approved by:', 'date prepared:', 'meeting date:', 'subject:', 'recommended action:', 'discussion:', 'capital improvement', 'disaster recovery', 'public works', 'commission meeting', 'agenda report']
        if any(pattern in line.lower() for pattern in skip_patterns):
            continue
        
        # Check if line could be a project name (look ahead for project indicators)
        look_ahead_text = ' '.join(lines[i+1:i+5]).lower()
        
        if any(indicator in look_ahead_text for indicator in ['updates:', 'schedule:', 'complete', 'construction', 'project']):
            # This might be a project name
            potential_name = line
            
            # Now look for completion with 2022 in following lines
            for j in range(i, min(i+8, len(lines))):
                check_line = lines[j].strip()
                if '2022' in check_line and 'completed' in check_line.lower():
                    # Check if it's park-related
                    context = potential_name.lower() + ' ' + check_line.lower()
                    if 'park' in context:
                        year_match = re.search(r'(202\d)', check_line)
                        year = year_match.group(1) if year_match else '2022'
                        
                        park_projects_2022.append({
                            'Project_Name': potential_name,
                            'filename': filename,
                            'completion_note': check_line,
                            'year': year
                        })
                        break

print('\nFound {} park projects completed in 2022'.format(len(park_projects_2022)))

for p in park_projects_2022:
    print('Project: {}'.format(p['Project_Name']))
    print('File: {}'.format(p['filename']))
    print('Note: {}'.format(p['completion_note']))
    print('---')

# Now match with funding data
funding_matches = []
total_funding = 0

for project in park_projects_2022:
    project_name = project['Project_Name']
    
    # Find matching funding records
    for funding in funding_data:
        funding_name = funding['Project_Name']
        
        # Check for exact match or close match
        if funding_name.lower().strip() == project_name.lower().strip():
            funding_matches.append({
                'project': project_name,
                'funding_name': funding_name,
                'amount': int(funding['Amount']),
                'source': funding['Funding_Source']
            })
            total_funding += int(funding['Amount'])
            break
        
        # Also check if funding name contains the project name or vice versa
        elif (project_name.lower() in funding_name.lower() or funding_name.lower() in project_name.lower()):
            if len(project_name) > 10:  # Avoid short name matches
                funding_matches.append({
                    'project': project_name,
                    'funding_name': funding_name,
                    'amount': int(funding['Amount']),
                    'source': funding['Funding_Source']
                })
                total_funding += int(funding['Amount'])
                break

print('\nMatched {} projects with funding records'.format(len(funding_matches)))
print('Total funding: ${:,}'.format(total_funding))

for match in funding_matches:
    print('${:,} - {} ({})'.format(match['amount'], match['funding_name'], match['source']))

# Save results
output = {
    'park_projects_2022': park_projects_2022,
    'funding_matches': funding_matches,
    'total_funding': total_funding
}

with open('/tmp/park_funding_analysis.json', 'w') as f:
    json.dump(output, f, indent=2)

print('\nFull analysis saved to /tmp/park_funding_analysis.json')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}]}

exec(code, env_args)
