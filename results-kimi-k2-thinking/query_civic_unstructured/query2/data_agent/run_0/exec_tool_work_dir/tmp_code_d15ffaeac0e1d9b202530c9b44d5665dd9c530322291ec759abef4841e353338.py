code = """import json

# Load data
funding_file = locals()['var_functions.query_db:12']
docs_file = locals()['var_functions.query_db:11']

with open(docs_file, 'r') as f:
    docs = json.load(f)
with open(funding_file, 'r') as f:
    funding = json.load(f)

# Find park projects completed in 2022
park_projects_completed_2022 = []

for doc in docs:
    text = doc.get('text', '')
    # Simple approach: find documents mentioning park and 2022 completion
    if 'park' in text.lower() and '2022' in text and 'completed' in text.lower():
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if '2022' in line and 'completed' in line.lower():
                for j in range(max(0, i-5), i):
                    prev = lines[j].strip()
                    if prev and 'park' in prev.lower() and len(prev) < 200:
                        park_projects_completed_2022.append(prev)
                        break

park_projects_completed_2022 = list(set(park_projects_completed_2022))

# Match funding
total_funding = 0
for project in park_projects_completed_2022:
    for fund in funding:
        if project.lower() in fund['Project_Name'].lower() or fund['Project_Name'].lower() in project.lower():
            total_funding += int(fund['Amount'])

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': 'file_storage/functions.execute_python:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:30': [{'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}]}

exec(code, env_args)
