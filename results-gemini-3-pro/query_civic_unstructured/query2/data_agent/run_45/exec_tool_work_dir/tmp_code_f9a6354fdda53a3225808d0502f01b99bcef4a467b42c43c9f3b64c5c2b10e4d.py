code = """import json

# Park Projects (List)
park_projects = locals()['var_function-call-17336179596749823734']
# Civic Text (File Path)
path_text = locals()['var_function-call-18190371962378278332']
with open(path_text, 'r') as f:
    civic_data = json.load(f)
text = civic_data[0]['text'].lower()

funding_map = {}
for p in park_projects:
    name = p['Project_Name']
    if "(" in name: base = name.split("(")[0].strip()
    else: base = name.strip()
    if base not in funding_map: funding_map[base] = 0
    funding_map[base] += int(p['Amount'])

debug_info = []

for base_name in funding_map:
    idx = text.find(base_name.lower())
    if idx != -1:
        window = text[idx:idx+2000]
        for line in window.splitlines():
            if "2022" in line:
                # Check criteria
                matched = False
                if "construction was completed" in line or "construction completed" in line:
                    matched = True
                elif "completed" in line and "design" not in line and "phase" not in line:
                     # Filter out "Notice of completion filed January 2023" if the line doesn't have 2022
                     # But we are checking if "2022" is in line.
                     matched = True
                
                if matched:
                    debug_info.append({"project": base_name, "line": line})
                    break # Only one match needed to trigger

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-18190371962378278332': 'file_storage/function-call-18190371962378278332.json', 'var_function-call-3926390822647844774': 'file_storage/function-call-3926390822647844774.json', 'var_function-call-17336179596749823734': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Trancas Playground Resurfacing', 'Amount': '90000'}], 'var_function-call-18417157101231181788': {'total': 217000, 'projects': ['Bluffs Park Shade Structure', 'Malibu Bluffs Park South Walkway', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground']}}

exec(code, env_args)
