code = """import json

# Load the civic documents to find park projects completed in 2022
file_path = locals()['var_functions.query_db:18']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

# Load funding data
funding_data = locals()['var_functions.query_db:20']

print(f'Processing {len(civic_docs)} civic documents')
print(f'Processing {len(funding_data)} funding records')

# Create lookup for funding data by project name
funding_lookup = {}
for fund in funding_data:
    name_lower = fund['Project_Name'].lower()
    funding_lookup[name_lower] = {
        'amount': int(fund['Amount']),
        'source': fund['Funding_Source'],
        'original_name': fund['Project_Name']
    }

# Search for park projects completed in 2022
park_projects_completed_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for park projects with completion in 2022
    if 'Park' in text and '2022' in text:
        # Check for specific completion patterns
        if 'Construction was completed November 2022' in text and 'Bluffs Park Shade Structure' in text:
            park_projects_completed_2022.append('Bluffs Park Shade Structure')
        
        # Look for other park projects completed in 2022
        # Check for any park project name that appears near 2022 completion text
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip short or irrelevant lines
            if len(line) < 10 or any(skip in line for skip in ['Page', 'Agenda', 'Meeting', 'Commission', 'Item', 'Public Works']):
                continue
            
            # Check if line contains park project name
            if 'Park' in line:
                # Look ahead for completion info
                for j in range(i+1, min(i+15, len(lines))):
                    look_ahead = ' '.join(lines[i:j+1])
                    if '2022' in look_ahead and any(marker in look_ahead.lower() for marker in ['completed', 'construction was completed', 'notice of completion']):
                        # Clean up project name
                        proj_name = line
                        # Skip if it's clearly a section header
                        if not any(header in proj_name.lower() for header in ['capital improvement', 'disaster recovery', 'design', 'construction', 'not started']):
                            if proj_name not in park_projects_completed_2022:
                                park_projects_completed_2022.append(proj_name)
                        break

print(f'\nFound {len(park_projects_completed_2022)} potential park projects completed in 2022:')
for proj in park_projects_completed_2022:
    print(f'- {proj}')

# Match with funding data and calculate totals
total_funding = 0
matched_projects = []
unmatched_projects = []

for proj_name in park_projects_completed_2022:
    proj_lower = proj_name.lower()
    
    # Try to find exact match
    if proj_lower in funding_lookup:
        funding_info = funding_lookup[proj_lower]
        amount = funding_info['amount']
        total_funding += amount
        matched_projects.append({
            'project': proj_name,
            'amount': amount,
            'source': funding_info['source']
        })
    else:
        # Try partial matching
        matched = False
        for funded_lower, funding_info in funding_lookup.items():
            # Check if the project name contains key parts
            proj_parts = proj_lower.replace('project', '').replace('repair', '').strip()
            if len(proj_parts) > 5 and proj_parts in funded_lower:
                amount = funding_info['amount']
                total_funding += amount
                matched_projects.append({
                    'project': proj_name,
                    'matched_to': funding_info['original_name'],
                    'amount': amount,
                    'source': funding_info['source']
                })
                matched = True
                break
            
            # Check reverse - if funded name contains project name parts
            funded_parts = funded_lower.replace('project', '').replace('repair', '').strip()
            if len(funded_parts) > 5 and funded_parts in proj_lower:
                amount = funding_info['amount']
                total_funding += amount
                matched_projects.append({
                    'project': proj_name,
                    'matched_to': funding_info['original_name'],
                    'amount': amount,
                    'source': funding_info['source']
                })
                matched = True
                break
        
        if not matched:
            unmatched_projects.append(proj_name)

print(f'\nSuccessfully matched {len(matched_projects)} projects with funding:')
for proj in matched_projects:
    matched_info = f" (matched to: {proj.get('matched_to')})" if 'matched_to' in proj else ""
    print(f'- {proj["project"]}{matched_info}: ${proj["amount"]:,} ({proj["source"]})')

if unmatched_projects:
    print(f'\nUnmatched projects ({len(unmatched_projects)}):')
    for proj in unmatched_projects:
        print(f'- {proj}')

# Special case: Bluffs Park Shade Structure is confirmed completed in Nov 2022
print(f'\n=== KEY FINDING ===')
print(f'Bluffs Park Shade Structure was explicitly confirmed as completed in November 2022')
if 'bluffs park shade structure' in funding_lookup:
    bluffs_funding = funding_lookup['bluffs park shade structure']
    print(f'Bluffs Park Shade Structure funding: ${bluffs_funding["amount"]:,} ({bluffs_funding["source"]})')

print(f'\n=== FINAL RESULT ===')
print(f'Total funding for park projects completed in 2022: ${total_funding:,}')
print(f'Total number of funded projects: {len(matched_projects)}')

result = {
    'total_funding': total_funding,
    'total_projects': len(matched_projects),
    'matched_projects': matched_projects,
    'unmatched_projects': unmatched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}], 'var_functions.execute_python:26': {'status': 'success'}, 'var_functions.execute_python:28': {'park_funding_projects': [{'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}], 'count': 20}}

exec(code, env_args)
