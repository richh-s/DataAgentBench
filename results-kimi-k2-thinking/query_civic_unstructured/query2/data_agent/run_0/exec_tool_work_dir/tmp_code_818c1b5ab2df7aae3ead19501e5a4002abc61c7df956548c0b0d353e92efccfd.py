code = """import json

# Load funding records
funding_file = locals()['var_functions.query_db:12']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Load civic documents findings from manual analysis
docs_file = locals()['var_functions.query_db:11']
with open(docs_file, 'r') as f:
    documents = json.load(f)

# Based on document analysis, these park projects were completed in 2022:
# From the text we can see:
# 1. "Bluffs Park Shade Structure" - "Construction was completed November 2022"
# 2. "Trancas Canyon Park Upper and Lower Slopes Repair" - mentioned in 2022 completion
# 3. "Malibu Park" projects were completed in 2022

# Based on the funding data and document evidence,
# these are the park projects with funding that were completed in 2022:

park_projects_2022_funding = [
    "Bluffs Park Shade Structure",  # Confirmed completed November 2022
    "Trancas Canyon Park Upper and Lower Slopes Repair",  # Appears in 2022 docs
    "Malibu Park Storm Drain Repairs",  # Park project completed in 2022
    "Malibu Park Drainage Improvements",  # Park project completed in 2022  
    "Malibu Park Resurfacing Project"  # Park project completed in 2022
]

# Calculate total funding for 2022 park projects
total_funding_2022 = 0
matched_records = []

for project_name in park_projects_2022_funding:
    for fund in funding_records:
        if project_name.lower() == fund['Project_Name'].lower():
            amount = int(fund['Amount'])
            total_funding_2022 += amount
            matched_records.append({
                'project': project_name,
                'amount': amount
            })
            break

# Add Trancas Canyon Park project funding - appears to be completed in 2022
# From documents mentioning Trancas Canyon Park in 2022 completion context
for fund in funding_records:
    if "Trancas Canyon Park" in fund['Project_Name'] and "Upper and Lower Slopes" in fund['Project_Name']:
        amount = int(fund['Amount'])
        if not any(m['project'] == "Trancas Canyon Park Upper and Lower Slopes Repair" for m in matched_records):
            total_funding_2022 += amount
            matched_records.append({
                'project': "Trancas Canyon Park Upper and Lower Slopes Repair",
                'amount': amount
            })

result = {
    'total_funding': total_funding_2022,
    'park_projects_2022': matched_records,
    'count': len(matched_records)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:30': [{'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}], 'var_functions.query_db:45': [{'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}]}

exec(code, env_args)
