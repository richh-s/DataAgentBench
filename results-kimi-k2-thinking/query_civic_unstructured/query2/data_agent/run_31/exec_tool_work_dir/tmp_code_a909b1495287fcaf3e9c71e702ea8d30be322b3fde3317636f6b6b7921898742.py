code = """import json

# Access stored results correctly
funding_data = None
civic_docs = None

# Check what variables are available in locals()
for key in locals().keys():
    if 'query_db' in key and 'funding' in key.lower():
        funding_var = locals()[key]
        if isinstance(funding_var, str) and '.json' in funding_var:
            with open(funding_var, 'r') as f:
                funding_data = json.load(f)
        else:
            funding_data = funding_var
    elif 'query_db' in key and 'civic' in key.lower():
        civic_var = locals()[key]
        if isinstance(civic_var, str) and '.json' in civic_var:
            with open(civic_var, 'r') as f:
                civic_docs = json.load(f)
        else:
            civic_docs = civic_var

if funding_data is None:
    print("Funding data not found")
    funding_data = []

if civic_docs is None:
    print("Civic docs not found")
    civic_docs = []

# Identify park projects completed in 2022 from civic documents
park_projects_2022 = []

for doc in civic_docs:
    if not isinstance(doc, dict):
        continue
    text = doc.get('text', '').lower()
    if 'park' in text and 'completed' in text and '2022' in text:
        # Look for Bluffs Park Shade Structure specifically
        if 'bluffs park shade structure' in text:
            if 'completed' in text and '2022' in text:
                # Check if it's the specific completion mention
                lines = doc.get('text', '').split('\n')
                for line in lines:
                    lower_line = line.lower()
                    if 'bluffs park shade structure' in lower_line and 'completed' in lower_line and '2022' in lower_line:
                        park_projects_2022.append('Bluffs Park Shade Structure')

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Find matching funding records
total_funding = 0
matched_records = []

for record in funding_data:
    if not isinstance(record, dict):
        continue
    project_name = record.get('Project_Name', '')
    amount_str = str(record.get('Amount', '0'))
    amount = int(amount_str) if amount_str.isdigit() else 0
    
    for park_proj in park_projects_2022:
        if park_proj.lower() == project_name.lower():
            matched_records.append({
                'project': project_name,
                'amount': amount
            })
            total_funding += amount

result = {
    'total_funding': total_funding,
    'projects': park_projects_2022,
    'funding_records': matched_records
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.execute_python:0': {'collection': 'civic_docs', 'filter': {'text': {'$regex': 'park', '$options': 'i'}}, 'projection': {'filename': 1, 'text': 1}}, 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
