code = """import json

# Load funding data
funding_path = var_functions.query_db:18
funding_data = locals().get(funding_path)

# If it's a string (file path), load it
if isinstance(funding_data, str):
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

print("Funding records loaded:", len(funding_data))

# Load civic documents
civic_path = var_functions.query_db:20
if isinstance(civic_path, str):
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_path

print("Civic documents loaded:", len(civic_docs))

# From the documents preview, we can identify park projects completed in 2022:
# 1. Bluffs Park Shade Structure - completed November 2022

# List of park projects identified as completed in 2022
park_projects_2022 = [
    "Bluffs Park Shade Structure"
]

# Find these projects in funding data
total_funding = 0
matching_funding = []

for record in funding_data:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    
    for park_proj in park_projects_2022:
        if park_proj.lower() in project_name.lower():
            matching_funding.append({
                'project': project_name,
                'amount': amount
            })
            total_funding += amount

# Also check for other park projects that might have been completed in 2022
# by looking at the funding data for park-related projects
all_park_funding = []
for record in funding_data:
    project_name = record.get('Project_Name', '')
    if 'park' in project_name.lower():
        all_park_funding.append({
            'project': project_name,
            'amount': int(record.get('Amount', 0))
        })

print("Matching funding records:", len(matching_funding))
print("Total funding for identified projects:", total_funding)

result = {
    "identified_projects": park_projects_2022,
    "matching_funding_count": len(matching_funding),
    "total_funding": total_funding,
    "matched_records": matching_funding
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.execute_python:0': {'collection': 'civic_docs', 'filter': {'text': {'$regex': 'park', '$options': 'i'}}, 'projection': {'filename': 1, 'text': 1}}, 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
