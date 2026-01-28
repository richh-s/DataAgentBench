code = """import json

# Load funding data for park projects
funding_path = locals()['var_functions.query_db:36']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents (the query for 2022)
civic_path = locals()['var_functions.query_db:34']
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

print('Park funding projects:', len(funding_data))

# Find park projects completed in 2022
completed_2022_parks = []

for doc in civic_data:
    text = doc.get('text', '')
    lines = text.splitlines()
    
    for i, line in enumerate(lines):
        line_lower = line.lower()
        # Look for park project names
        if 'park' in line_lower and len(line.strip()) > 5 and not line.strip().startswith('('):
            words = line.strip().split()
            # Check if it looks like a title (has capitalized words)
            if any(word and word[0].isupper() for word in words):
                # Check nearby lines for 2022 completion
                for j in range(i, min(i+5, len(lines))):
                    status_line = lines[j].lower()
                    if '2022' in status_line and ('completed' in status_line or 'completion' in status_line):
                        completed_2022_parks.append(line.strip())
                        break

print('Park projects completed in 2022:', completed_2022_parks)

# Match with funding data and calculate total funding
total_funding = 0
matched = []

for project_name in completed_2022_parks:
    for fund in funding_data:
        fund_name = fund['Project_Name']
        # Check if they match
        if project_name.lower() in fund_name.lower() or fund_name.lower() in project_name.lower():
            amount = int(fund['Amount'])
            total_funding += amount
            matched.append({'project': fund_name, 'amount': amount})
            break

print('Total funding:', total_funding)
print('Matched projects:', len(matched))

result = {'total_funding': total_funding, 'matched': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:32': 0, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}]}

exec(code, env_args)
