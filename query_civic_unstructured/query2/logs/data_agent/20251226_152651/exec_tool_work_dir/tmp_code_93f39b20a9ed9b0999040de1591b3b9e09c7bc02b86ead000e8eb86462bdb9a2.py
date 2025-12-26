code = """import re
import pandas as pd
import json

# Load the full MongoDB result from file
with open(var_call_H8GS069ZxpAeh4QJ1E1NcGL8, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

funding_records = var_call_WBBg4QCmupCMA3IFHqUxkRKC

# We need completed park-related projects from 2022.
# Scan through the civic docs and extract relevant data from text
project_infos = []
for doc in civic_docs:
    text = doc['text']
    # Find projects completed in 2022 with 'park' in the name/topic
    # We'll use regex to look for likely matches such as
    # ...<Project Name>...completed...2022 or ...construction was completed...2022
    matches = re.findall(r'(\b(?:Bluffs Park|Legacy Park|Malibu Bluffs Park|Trancas Canyon Park|Permanent Skate Park|Malibu Park)[^\n\r.]*?completed[^\n\r.]*?2022)', text, flags=re.IGNORECASE)
    for m in matches:
        # Try to extract project name
        pname_match = re.search(r'(Bluffs Park Shade Structure|Bluffs Park Workout Station|Legacy Park Benches and Arbors Renovation|Legacy Park Paver Repair Project|Malibu Bluffs Park Roof Replacement Project|Malibu Bluffs Park South Walkway|Malibu Bluffs Park South Walkway Repairs|Malibu Park Drainage Improvements|Malibu Park Resurfacing Project|Malibu Park Storm Drain Repairs|Permanent Skate Park|Trancas Canyon Park Planting and Irrigation Repairs|Trancas Canyon Park Planting and Irrigation Repairs \(CalJPIA/FEMA Project\)|Trancas Canyon Park Planting and Irrigation Repairs \(FEMA/CalOES Project\)|Trancas Canyon Park Playground|Trancas Canyon Park Playground Resurfacing|Trancas Canyon Park Slope Stabilization Project|Trancas Canyon Park Slope Stabilization Project \(CalJPIA Project\)|Trancas Canyon Park Slope Stabilization Project \(CalOES Project\)|Trancas Canyon Park Upper and Lower Slopes Repair)', m, flags=re.IGNORECASE)
        if pname_match:
            pname = pname_match.group(1)
            project_infos.append(pname)
        else:
            # Try to extract rough project name from the string (fallback)
            for rec in funding_records:
                if rec['Project_Name'].lower() in m.lower():
                    project_infos.append(rec['Project_Name'])
                    break

# Remove duplicates
project_infos = list(set(project_infos))

# Now, filter funding records for these project names
completed_2022_funding = [rec['Amount'] for rec in funding_records if rec['Project_Name'] in project_infos]
completed_2022_funding_int = [int(a) for a in completed_2022_funding]

# Total funding
total_funding = sum(completed_2022_funding_int)

print("__RESULT__:")
print(json.dumps(total_funding))"""

env_args = {'var_call_H8GS069ZxpAeh4QJ1E1NcGL8': 'file_storage/call_H8GS069ZxpAeh4QJ1E1NcGL8.json', 'var_call_WBBg4QCmupCMA3IFHqUxkRKC': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}]}

exec(code, env_args)
