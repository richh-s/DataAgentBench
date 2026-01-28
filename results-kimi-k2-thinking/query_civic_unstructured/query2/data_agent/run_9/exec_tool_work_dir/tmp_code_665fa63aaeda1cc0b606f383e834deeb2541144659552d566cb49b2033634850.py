code = """import json

# Load the civic documents file
file_path = locals()['var_functions.query_db:18']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f'Loaded {len(civic_docs)} civic documents')

# Load the funding data
funding_data = locals()['var_functions.query_db:20']
print(f'Loaded {len(funding_data)} funding records')

# Extract park projects from civic docs completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for completion statements in 2022 for park projects
    completion_indicators = [
        'construction was completed',
        'construction was completed, November 2022',
        'construction was completed, January 2023', # Note: completion filed in Jan but completed in 2022
        'Notice of completion filed January 2023' # Projects completed in 2022, notice filed in 2023
    ]
    
    # Check if this document contains park project completion info
    if 'Park' in text and '2022' in text:
        # Look for completed park projects
        if 'Bluffs Park Shade Structure' in text:
            # Verify completion in 2022
            if 'Construction was completed November 2022' in text:
                park_projects_2022.append({
                    'Project_Name': 'Bluffs Park Shade Structure',
                    'source': filename,
                    'completion_note': 'Construction was completed November 2022'
                })
        
        # Check for other park projects that might have been completed
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'Park' in line and len(line.strip()) > 10:
                clean_line = line.strip()
                # Check subsequent lines for completion info
                for j in range(i+1, min(i+10, len(lines))):
                    future_text = ' '.join(lines[i:j+1])
                    if '2022' in future_text and any(marker in future_text.lower() for marker in ['completed', 'construction was completed']):
                        if clean_line not in [p['Project_Name'] for p in park_projects_2022]:
                            # Check if this is a reasonable project name
                            if any(keyword in clean_line for keyword in ['Repair', 'Project', 'Structure', 'Improvement', 'Walkway', 'Shade']):
                                park_projects_2022.append({
                                    'Project_Name': clean_line,
                                    'source': filename,
                                    'trigger': 'Pattern match'
                                })
                        break

print(f'\nFound {len(park_projects_2022)} potential park projects completed in 2022:')
for proj in park_projects_2022:
    print(f"- {proj['Project_Name']}: {proj.get('completion_note', 'Pattern detected')}")

# Match with funding data
funding_lookup = {f['Project_Name'].lower(): f for f in funding_data}

matched_projects = []
total_funding = 0

for proj in park_projects_2022:
    proj_name = proj['Project_Name']
    proj_name_lower = proj_name.lower()
    
    # Try exact match first
    if proj_name_lower in funding_lookup:
        funding_info = funding_lookup[proj_name_lower]
        matched_projects.append({
            'Project_Name': proj_name,
            'Funding': funding_info['Amount'],
            'Source': funding_info['Funding_Source']
        })
        total_funding += int(funding_info['Amount'])
    else:
        # Try partial matching
        for funded_name, funding_info in funding_lookup.items():
            # Check if parts of the name match
            name_parts = proj_name_lower.replace('project', '').replace('repair', '').strip()
            if name_parts and name_parts in funded_name:
                matched_projects.append({
                    'Project_Name': proj_name,
                    'Funding': funding_info['Amount'],
                    'Source': funding_info['Funding_Source'],
                    'Matched_to': funded_name
                })
                total_funding += int(funding_info['Amount'])
                break

print(f'\nMatched with funding: {len(matched_projects)} projects')
for proj in matched_projects:
    print(f"- {proj['Project_Name']}: ${proj['Funding']}")

print(f'\nTotal funding for matched projects: ${total_funding}')

# Also check the Bluffs Park Shade Structure specifically since we saw it in the preview
bluffs_projects = [f for f in funding_data if 'Bluffs Park Shade Structure' in f['Project_Name']]
print(f'\nBluffs Park Shade Structure funding: {bluffs_projects}')

result = {
    'matched_projects': matched_projects,
    'total_funding': total_funding,
    'total_projects': len(matched_projects)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': [{'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}]}

exec(code, env_args)
