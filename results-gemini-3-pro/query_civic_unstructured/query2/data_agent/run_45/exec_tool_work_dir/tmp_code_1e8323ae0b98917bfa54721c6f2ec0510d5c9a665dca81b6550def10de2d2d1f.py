code = """import json

# Park Projects (List)
park_projects = locals()['var_function-call-17336179596749823734']

# Civic Text (File Path)
path_text = locals()['var_function-call-18190371962378278332']
with open(path_text, 'r') as f:
    civic_data = json.load(f)

text = civic_data[0]['text'].lower()

# Normalize and Sum Logic
funding_map = {}
for p in park_projects:
    name = p['Project_Name']
    # Normalize base name
    if "(" in name:
        base = name.split("(")[0].strip()
    else:
        base = name.strip()
    
    if base not in funding_map:
        funding_map[base] = 0
    funding_map[base] += int(p['Amount'])

total_funding = 0
completed_projects = []

for base_name in funding_map:
    # Search in text
    # Use find to locate
    idx = text.find(base_name.lower())
    if idx != -1:
        # Window
        window = text[idx:idx+2000]
        
        is_completed = False
        if "2022" in window:
            for line in window.splitlines():
                if "2022" in line:
                    if "construction was completed" in line or \
                       "construction completed" in line or \
                       "completed construction" in line:
                        is_completed = True
                    # Check for "completed, november 2022"
                    if "completed" in line and "design" not in line and "phase" not in line:
                        # Check proximity of "completed" and "2022"
                        if line.find("completed") < line.find("2022"): 
                             is_completed = True
        
        if is_completed:
            completed_projects.append(base_name)
            total_funding += funding_map[base_name]

print("__RESULT__:")
print(json.dumps({"total": total_funding, "projects": completed_projects}))"""

env_args = {'var_function-call-18190371962378278332': 'file_storage/function-call-18190371962378278332.json', 'var_function-call-3926390822647844774': 'file_storage/function-call-3926390822647844774.json', 'var_function-call-17336179596749823734': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Trancas Playground Resurfacing', 'Amount': '90000'}]}

exec(code, env_args)
