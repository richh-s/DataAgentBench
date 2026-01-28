code = """import json

# Load the data that was successfully retrieved
funding_data = [
  {"Project_Name": "Bluffs Park Shade Structure", "Amount": "21000"},
  {"Project_Name": "Bluffs Park Workout Station", "Amount": "39000"},
  {"Project_Name": "Legacy Park Benches and Arbors Renovation", "Amount": "41000"},
  {"Project_Name": "Legacy Park Paver Repair Project", "Amount": "69000"},
  {"Project_Name": "Malibu Bluffs Park Roof Replacement Project", "Amount": "44000"},
  {"Project_Name": "Malibu Bluffs Park South Walkway", "Amount": "91000"},
  {"Project_Name": "Malibu Bluffs Park South Walkway Repairs", "Amount": "81000"},
  {"Project_Name": "Malibu Park Drainage Improvements", "Amount": "17000"},
  {"Project_Name": "Malibu Park Resurfacing Project", "Amount": "14000"},
  {"Project_Name": "Malibu Park Storm Drain Repairs", "Amount": "50000"},
  {"Project_Name": "Permanent Skate Park", "Amount": "97000"},
  {"Project_Name": "Trancas Canyon Park Planting and Irrigation Repairs", "Amount": "78000"},
  {"Project_Name": "Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)", "Amount": "44000"},
  {"Project_Name": "Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)", "Amount": "92000"},
  {"Project_Name": "Trancas Canyon Park Playground", "Amount": "24000"},
  {"Project_Name": "Trancas Canyon Park Playground Resurfacing", "Amount": "65000"},
  {"Project_Name": "Trancas Canyon Park Slope Stabilization Project", "Amount": "68000"},
  {"Project_Name": "Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)", "Amount": "43000"},
  {"Project_Name": "Trancas Canyon Park Slope Stabilization Project (CalOES Project)", "Amount": "32000"},
  {"Project_Name": "Trancas Canyon Park Upper and Lower Slopes Repair", "Amount": "23000"}
]

# Analyze civic doc for 2022 completions
civic_doc_text = """Public Works Commission Agenda Report ...

Bluffs Park Shade Structure

Updates: Construction was completed November 2022. Notice of completion filed January 2023

Marie Canyon Green Streets
Updates: Construction was completed, January 2023

Broad Beach Road Water Quality Repair
Updates: Construction was completed, November 2022

Point Dume Walkway Repairs
Updates: Construction was completed, November 2022
"""

# Parse 2022 park completions from the civic doc
lines = civic_doc_text.split('\n')
completed_2022_parks = []

for i, line in enumerate(lines):
    line_lower = line.lower()
    if 'park' in line_lower and '2022' in line_lower and ('completed' in line_lower or 'completion' in line_lower):
        # Extract project name from previous lines
        for j in range(max(0, i-3), i):
            prev_line = lines[j].strip()
            if prev_line and len(prev_line) > 5 and not prev_line.startswith('(') and 'park' in prev_line.lower():
                completed_2022_parks.append(prev_line)
                break

print('Park projects completed in 2022:', completed_2022_parks)

# Calculate total funding for these projects
total = 0
matched = []

for project in completed_2022_parks:
    for fund in funding_data:
        if fund['Project_Name'].lower() in project.lower() or project.lower() in fund['Project_Name'].lower():
            total += int(fund['Amount'])
            matched.append(fund['Project_Name'])
            break

print('Matched park projects:', matched)
print('Total funding for 2022 park completions:', total)

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'matched_projects': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:32': 0, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}]}

exec(code, env_args)
