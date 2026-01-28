code = """import json

path_text = locals()['var_function-call-18190371962378278332']
with open(path_text, 'r') as f:
    civic_data = json.load(f)
text = civic_data[0]['text'] # Keep case for name extraction

# Split into sections based on "(cid:190) Updates" or "(cid:190) Project Description"
# We'll identify the start of each project.
# We'll create a list of (ProjectName, TextBody) tuples.

lines = text.splitlines()
projects = []

for i, line in enumerate(lines):
    if "(cid:190)" in line and ("Updates" in line or "Project Description" in line):
        # Determine Project Name from previous lines
        # Look back for non-empty line
        name_parts = []
        j = i - 1
        while j >= 0:
            prev = lines[j].strip()
            if not prev:
                j -= 1
                continue
            # Stop if we hit a known header or another marker
            if "(cid:190)" in prev or "Page" in prev or "Agenda Item" in prev or "Capital Improvement" in prev:
                break
            name_parts.insert(0, prev)
            # Usually name is 1 or 2 lines. Let's take up to 2 lines.
            if len(name_parts) >= 2:
                break
            j -= 1
        
        project_name = " ".join(name_parts)
        
        # Now get the body until next marker
        # We can just store the start index and parse later, or collect lines.
        # Let's collect lines until next marker.
        # But we are in a loop.
        # Actually, let's just mark the start line of the project (j)
        if project_name:
            projects.append({"name": project_name, "start_line": i})

# Now build the text for each project
for k in range(len(projects)):
    start = projects[k]["start_line"]
    # End is the start of next project (minus name lines) or end of file
    if k < len(projects) - 1:
        end = projects[k+1]["start_line"] - 5 # Approximate buffer for name
    else:
        end = len(lines)
    
    # Extract lines
    body_lines = lines[start:end]
    projects[k]["body"] = "\n".join(body_lines).lower()

# Filter
completed_park_projects = []

for p in projects:
    name = p["name"].strip()
    body = p["body"]
    
    # Check if park related (Name)
    if "Park" in name or "Playground" in name or "Walkway" in name: 
        # (Included Walkway to check "Malibu Bluffs Park South Walkway")
        # Ensure it has "Park" or is one of our candidates
        is_candidate = False
        if "Park" in name or "Playground" in name:
            is_candidate = True
        elif "Walkway" in name:
            # Check if it mentions "Park" in name or is in our filtered list
            if "Bluffs" in name or "Point Dume" in name:
                 # Point Dume is debatable, but user query said "park-related".
                 # If Point Dume is a park, it counts.
                 # Let's check completion first.
                 is_candidate = True
        
        if is_candidate:
            # Check completion in 2022
            # Look for "construction was completed ... 2022" in body
            matched = False
            for line in body.splitlines():
                if "2022" in line:
                    if "construction was completed" in line or \
                       "construction completed" in line or \
                       "completed construction" in line:
                        matched = True
                    elif "completed" in line and "design" not in line and "phase" not in line:
                         # e.g. "Construction was completed, November 2022" matches
                         # Ensure "completed" comes before 2022 or is associated?
                         # The text "Construction was completed November 2022" works.
                         matched = True
            
            if matched:
                completed_park_projects.append(name)

print("__RESULT__:")
print(json.dumps(completed_park_projects))"""

env_args = {'var_function-call-18190371962378278332': 'file_storage/function-call-18190371962378278332.json', 'var_function-call-3926390822647844774': 'file_storage/function-call-3926390822647844774.json', 'var_function-call-17336179596749823734': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Trancas Playground Resurfacing', 'Amount': '90000'}], 'var_function-call-18417157101231181788': {'total': 217000, 'projects': ['Bluffs Park Shade Structure', 'Malibu Bluffs Park South Walkway', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground']}, 'var_function-call-2874234682422263337': [{'project': 'Bluffs Park Shade Structure', 'line': '(cid:190) updates: construction was completed november 2022. notice of completion'}, {'project': 'Malibu Bluffs Park South Walkway', 'line': '(cid:190) updates: construction was completed november 2022. notice of completion'}, {'project': 'Malibu Bluffs Park South Walkway Repairs', 'line': '(cid:190) updates: construction was completed november 2022. notice of completion'}, {'project': 'Trancas Canyon Park Playground', 'line': '(cid:190) updates: construction was completed november 2022. notice of completion'}]}

exec(code, env_args)
