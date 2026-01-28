code = """import json

# Load funding data (park projects only)
funding_data = locals()['var_functions.query_db:36']

# Load civic documents (contain project status information)
civic_data = locals()['var_functions.query_db:34']

# Step 1: Identify park projects completed in 2022 from civic documents
completed_2022_park_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    # Look for park projects with 2022 completion status
    for i, line in enumerate(lines):
        line_lower = line.lower()
        if 'park' in line_lower and '2022' in line_lower:
            if 'completed' in line_lower or 'completion' in line_lower:
                # Extract the project name (usually on a previous line or same line)
                project_name = line.strip()
                # If this line is a status update, look backwards for the project name
                if 'updates' in line_lower or 'construction' in line_lower:
                    for j in range(i-3, i):
                        if j >= 0:
                            prev_line = lines[j].strip()
                            if prev_line and 'park' in prev_line.lower() and len(prev_line) > 5:
                                project_name = prev_line
                                break
                completed_2022_park_projects.append(project_name)

# Remove duplicates
completed_2022_park_projects = list(set(completed_2022_park_projects))

print('Park projects completed in 2022:', completed_2022_park_projects)

# Step 2: Match with funding data and calculate total
total_funding = 0
matched_projects = []

for project in completed_2022_park_projects:
    for fund_record in funding_data:
        fund_name = fund_record['Project_Name']
        # Check if funding record matches the completed project
        if (fund_name.lower() in project.lower() or 
            project.lower() in fund_name.lower() or
            all(word in project.lower() for word in fund_name.lower().split() if len(word) > 3)):
            amount = int(fund_record['Amount'])
            total_funding += amount
            matched_projects.append({
                'project_name': fund_name,
                'amount': amount
            })
            break

# Special case: Check for Bluffs Park Shade Structure which mentions 2022 completion
bluffs_park_found = False
for fund in funding_data:
    if 'Bluffs Park Shade Structure' in fund['Project_Name']:
        # Check if in civic data
        for doc in civic_data:
            if 'Bluffs Park Shade Structure' in doc.get('text', '') and '2022' in doc.get('text', ''):
                amount = int(fund['Amount'])
                total_funding += amount
                matched_projects.append({
                    'project_name': fund['Project_Name'],
                    'amount': amount
                })
                bluffs_park_found = True
                break

# Remove duplicates from matched projects
unique_projects = {}
for proj in matched_projects:
    unique_projects[proj['project_name']] = proj['amount']

total_funding = sum(unique_projects.values())
matched_projects = [{'project_name': k, 'amount': v} for k, v in unique_projects.items()]

print('\nMatched park projects and funding:')
for proj in matched_projects:
    print(f"  {proj['project_name']}: ${proj['amount']:,}")

print(f'\nTOTAL: ${total_funding:,}')

result = {
    'total_funding_for_park_projects_completed_in_2022': total_funding,
    'number_of_projects': len(matched_projects),
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:32': 0, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}]}

exec(code, env_args)
