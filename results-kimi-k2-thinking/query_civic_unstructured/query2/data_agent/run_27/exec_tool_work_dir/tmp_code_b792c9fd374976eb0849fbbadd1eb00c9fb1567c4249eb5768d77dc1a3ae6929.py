code = """import json, re

with open(locals()['var_functions.query_db:108']) as f:
    civic_docs = json.load(f)
with open(locals()['var_functions.query_db:101']) as f:
    funding_data = json.load(f)

print('Searching through civic documents for park projects completed in 2022...')

# Find all references to park projects with 2022 completion
all_matches = []

for doc in civic_docs:
    text = doc['text']
    
    # Look for park projects completed in 2022
    # Pattern: "Construction was completed [month] 2022" or "completed November 2022"
    completion_patterns = [
        r'([^.]*?park[^.]*?completed[^.]*?2022[^.]*)',
        r'([^.]*?completed[^.]*?2022[^.]*?park[^.]*)',
        r'Construction was completed[^\n]*2022[^\n]*([A-Za-z\s]+)',
    ]
    
    for pattern in completion_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            all_matches.append(match.strip())

print('All references to park + 2022 completion:')
for m in all_matches:
    print('-', m)

# Now extract project names from the actual lines
park_projects = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    for i in range(len(lines)):
        line = lines[i]
        # Check if this line mentions completion in 2022
        if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
            # Look back for project name
            for j in range(i-1, max(0, i-10), -1):
                prev_line = lines[j].strip()
                if prev_line and not prev_line.startswith('(') and len(prev_line) > 5:
                    # Check if this line contains 'park'
                    if 'park' in prev_line.lower():
                        clean = prev_line.replace('•', '').replace('◦', '').strip()
                        clean = re.sub(r'^[A-Z]\.?\s+', '', clean)
                        if clean and clean not in park_projects:
                            park_projects.append(clean)
                            print('Found project name:', clean)
                    break

print('\nAll unique park projects:', park_projects)

# Now find all funding for park-related projects
total_park_funding = 0
park_funding_records = []

for fund in funding_data:
    if 'park' in fund['Project_Name'].lower():
        amount = int(fund['Amount'])
        total_park_funding += amount
        park_funding_records.append(fund['Project_Name'])

print('\nAll park-related funding records:')
for record in park_funding_records:
    print('-', record)

print('\nTotal park funding (all years): $', total_park_funding)

# Now specifically find funding for projects completed in 2022
total_2022_funding = 0
matched_projects = []

for park in park_projects:
    park_norm = park.lower().replace(' ', '').replace('-', '')
    for fund in funding_data:
        fund_norm = fund['Project_Name'].lower().replace(' ', '').replace('-', '')
        if park_norm in fund_norm or fund_norm in park_norm:
            amount = int(fund['Amount'])
            total_2022_funding += amount
            matched_projects.append({
                'project': park,
                'funding_record': fund['Project_Name'],
                'amount': amount
            })
            break

print('\nProjects completed in 2022 with funding:')
for proj in matched_projects:
    print('-', proj['project'], ': $', proj['amount'])

print('\nTotal funding for 2022 park projects: $', total_2022_funding)

result = {'total_funding_2022': total_2022_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}, 'var_functions.execute_python:66': {'status': 'success', 'docs_loaded': 5}, 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.query_db:85': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': '87000'}], 'var_functions.query_db:96': 'file_storage/functions.query_db:96.json', 'var_functions.query_db:97': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:100': 'file_storage/functions.query_db:100.json', 'var_functions.query_db:101': 'file_storage/functions.query_db:101.json', 'var_functions.query_db:106': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}], 'var_functions.query_db:108': 'file_storage/functions.query_db:108.json', 'var_functions.execute_python:114': {'total': 21000}}

exec(code, env_args)
