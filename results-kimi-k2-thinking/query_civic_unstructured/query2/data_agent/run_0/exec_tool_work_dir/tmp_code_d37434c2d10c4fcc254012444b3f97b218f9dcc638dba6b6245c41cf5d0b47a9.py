code = """import json

# Load all data
funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

docs_file = locals()['var_functions.query_db:11']
with open(docs_file, 'r') as f:
    documents = json.load(f)

# Based on the documents, find park projects completed in 2022
# From visual inspection of the document text, I can see these were completed in 2022:
# - Bluffs Park Shade Structure (completed November 2022)
# - Other park projects with 2022 completion

# Let's search more carefully for completion patterns
park_projects_2022 = []

for doc in documents:
    text = doc.get('text', '')
    # Look for patterns like "Construction was completed November 2022" or similar
    if 'park' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_lower = line.strip().lower()
            if 'completed' in line_lower and '2022' in line_lower:
                # Look backwards for project name containing park
                for j in range(i-1, max(0, i-5), -1):
                    prev = lines[j].strip()
                    if 'park' in prev.lower() and len(prev) < 200:
                        # Skip common headers
                        if not any(x in prev.lower() for x in ['capital improvement', 'disaster recovery', 'public works', 'commission']):
                            park_projects_2022.append(prev)
                            break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

# Now find funding for these projects
total_amount = 0
matching_records = []

for project in park_projects_2022:
    proj_lower = project.lower()
    for fund in funding_records:
        fund_name = fund['Project_Name'].lower()
        # Check if project name matches funding record
        if proj_lower in fund_name or fund_name in proj_lower:
            amount = int(fund['Amount'])
            total_amount += amount
            matching_records.append({'project': project, 'funding': fund['Project_Name'], 'amount': amount})

result_data = {
    'total_funding': total_amount,
    'park_projects_found': park_projects_2022,
    'matching_funding_records': matching_records
}

print('__RESULT__:')
print(result_data)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:30': [{'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}]}

exec(code, env_args)
