code = """import json

# Load files
with open(locals()['var_function-call-17336179596749823734'], 'r') as f:
    # This is the list of park projects from SQL
    park_projects_list = json.load(f)

with open(locals()['var_function-call-18190371962378278332'], 'r') as f:
    civic_data = json.load(f)

text = civic_data[0]['text']
text_lower = text.lower()

# Helper to normalize names for matching
def normalize(name):
    # Remove suffixes like (FEMA...)
    if "(" in name:
        return name.split("(")[0].strip()
    return name.strip()

# Group funding by base name
funding_by_base = {}
for p in park_projects_list:
    full_name = p['Project_Name']
    base_name = normalize(full_name)
    amount = int(p['Amount'])
    if base_name not in funding_by_base:
        funding_by_base[base_name] = 0
    funding_by_base[base_name] += amount

# Check each base name in text for completion in 2022
completed_base_names = []

# We need to find the specific section for each project.
# Since we have the text, let's locate the base name.
for base_name in funding_by_base.keys():
    # Search for base_name in text
    if base_name.lower() in text_lower:
        # Get location
        idx = text_lower.find(base_name.lower())
        # Look ahead
        snippet = text_lower[idx:idx+2000] # 2000 chars should cover the update
        
        # Check for 2022 and completed
        if "2022" in snippet:
            # Check for completion keywords
            # "construction was completed"
            # "complete construction"
            # "completed, ... 2022"
            
            is_completed = False
            
            # Split into lines to avoid cross-project confusion if possible
            lines = snippet.split('\n')
            for line in lines:
                # Stop if we hit another project header (heuristic)
                # But headers are hard to detect without layout analysis.
                # Just look for the completion line.
                
                if "2022" in line:
                    if "construction was completed" in line or \
                       "construction completed" in line or \
                       "completed construction" in line:
                         is_completed = True
                    elif "completed" in line and "design" not in line:
                         # e.g. "Construction was completed, November 2022"
                         # or "Project completed 2022"
                         # Be careful of "Design completed"
                         if "project" in line or "construction" in line or "work" in line:
                             is_completed = True
                         # Also the pattern "Construction was completed, November 2022" matches "completed"
                         if "construction" in snippet and "completed" in line: # snippet context
                             is_completed = True

            if is_completed:
                completed_base_names.append(base_name)

# Sum funding
total = 0
for bn in completed_base_names:
    total += funding_by_base[bn]

print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_function-call-18190371962378278332': 'file_storage/function-call-18190371962378278332.json', 'var_function-call-3926390822647844774': 'file_storage/function-call-3926390822647844774.json', 'var_function-call-17336179596749823734': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Trancas Playground Resurfacing', 'Amount': '90000'}]}

exec(code, env_args)
