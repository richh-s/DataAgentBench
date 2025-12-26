code = """import re
import pandas as pd
import json

with open(var_call_H8GS069ZxpAeh4QJ1E1NcGL8, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

funding_records = var_call_WBBg4QCmupCMA3IFHqUxkRKC

# List of all park-related projects
park_projects = [rec['Project_Name'] for rec in funding_records]

# Find park-related projects completed in 2022 from civic docs
completed_2022_projects = set()
for doc in civic_docs:
    text = doc['text']
    for pname in park_projects:
        # Check for completion in 2022 mentions
        pattern = rf'{re.escape(pname)}[\s\S]{{0,100}}completed[\s\S]*2022'
        if re.search(pattern, text, re.IGNORECASE):
            completed_2022_projects.add(pname)

# Sum the funding amounts for these projects
total_funding = 0
for rec in funding_records:
    if rec['Project_Name'] in completed_2022_projects:
        try:
            total_funding += int(rec['Amount'])
        except:
            pass

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_call_H8GS069ZxpAeh4QJ1E1NcGL8': 'file_storage/call_H8GS069ZxpAeh4QJ1E1NcGL8.json', 'var_call_WBBg4QCmupCMA3IFHqUxkRKC': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}]}

exec(code, env_args)
