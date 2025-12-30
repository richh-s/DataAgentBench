code = """import json

# Load Park Projects from previous query results
path_park = locals()['var_function-call-17336179596749823734']
with open(path_park, 'r') as f:
    park_projects = json.load(f)

# Load Civic Text
path_text = locals()['var_function-call-18190371962378278332']
with open(path_text, 'r') as f:
    civic_data = json.load(f)

text = civic_data[0]['text'].lower()

# Normalize and Sum Logic
funding_map = {}
for p in park_projects:
    name = p['Project_Name']
    # Normalize base name: remove (FEMA...) etc
    if "(" in name:
        base = name.split("(")[0].strip()
    else:
        base = name.strip()
    
    # Store amount
    if base not in funding_map:
        funding_map[base] = 0
    funding_map[base] += int(p['Amount'])

total_funding = 0
completed_projects = []

for base_name in funding_map:
    # Check if base_name is in text
    if base_name.lower() in text:
        # Find all occurrences or just the section?
        # A project might be mentioned multiple times (e.g. in a list then in detail).
        # We need to find the detail section.
        # Detail sections usually have "Updates:" or "Project Schedule:".
        
        # Simple scan: look for "completed" near the name.
        idx = text.find(base_name.lower())
        
        # Look at window after
        window = text[idx:idx+1500]
        
        # Check for 2022 completion
        # "construction was completed" ... "2022"
        # "completed" ... "2022"
        
        is_completed = False
        
        if "2022" in window:
            lines = window.splitlines()
            for line in lines:
                if "2022" in line:
                    if "construction was completed" in line or \
                       "construction completed" in line or \
                       "completed construction" in line:
                         is_completed = True
                    elif "completed" in line and "design" not in line and "phase" not in line:
                         # Be careful of "design phase completed"
                         is_completed = True
        
        if is_completed:
            completed_projects.append(base_name)
            total_funding += funding_map[base_name]

print("__RESULT__:")
print(json.dumps({"total": total_funding, "projects": completed_projects}))"""

env_args = {'var_function-call-18190371962378278332': 'file_storage/function-call-18190371962378278332.json', 'var_function-call-3926390822647844774': 'file_storage/function-call-3926390822647844774.json', 'var_function-call-17336179596749823734': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Trancas Playground Resurfacing', 'Amount': '90000'}]}

exec(code, env_args)
