code = """import json

# Get stored query results
funding_data = locals()['var_functions.query_db:36']
civic_data = locals()['var_functions.query_db:34']

print('Funding records:', len(funding_data))
print('Civic documents:', len(civic_data))

# Step 1: Identify park projects from funding data
park_funding_projects = []
for record in funding_data:
    if 'park' in record['Project_Name'].lower():
        park_funding_projects.append({
            'name': record['Project_Name'],
            'amount': int(record['Amount'])
        })

print('Park funding projects found:', len(park_funding_projects))

# Step 2: Find park projects completed in 2022 from civic docs
completed_2022_parks = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        
        # Look for park project names (lines containing 'Park' that look like titles)
        if 'park' in line_lower and len(line.strip()) > 5:
            words = line.strip().split()
            # Check if it looks like a project name (has capitalized words, not a bullet/comment)
            if any(word and word[0].isupper() for word in words) and not line.strip().startswith('('):
                # Check following lines for 2022 completion status
                for j in range(i, min(i+6, len(lines))):
                    status_line = lines[j].lower()
                    if '2022' in status_line and ('completed' in status_line or 'completion' in status_line):
                        completed_2022_parks.append(line.strip())
                        break

print('Park projects completed in 2022 found:', len(completed_2022_parks))
print('Projects:', completed_2022_parks)

# Step 3: Match projects and calculate total funding
total_funding = 0
matched_projects = []

for project_name in completed_2022_parks:
    for fund_project in park_funding_projects:
        fund_name = fund_project['name']
        # Check for matching (accounting for variations like "Bluffs Park" vs "Bluffs Park Shade Structure")
        if (project_name.lower() in fund_name.lower() or 
            fund_name.lower() in project_name.lower() or
            all(word in fund_name.lower() for word in project_name.lower().split() if len(word) > 3)):
            total_funding += fund_project['amount']
            matched_projects.append({
                'project': fund_name,
                'amount': fund_project['amount']
            })
            break

print('\nMatched projects and their funding:')
for p in matched_projects:
    print(f'  {p["project"]}: ${p["amount"]:,}')

print(f'\nTOTAL FUNDING: ${total_funding:,}')

result = {
    'total_funding_for_2022_park_completions': total_funding,
    'number_of_projects': len(matched_projects),
    'project_details': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:32': 0, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}]}

exec(code, env_args)
