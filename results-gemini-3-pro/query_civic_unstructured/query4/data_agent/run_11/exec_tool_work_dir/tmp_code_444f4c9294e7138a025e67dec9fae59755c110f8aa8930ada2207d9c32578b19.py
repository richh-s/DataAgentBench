code = """import json

funding_file = locals()['var_function-call-13662082539617429622']
docs_file = locals()['var_function-call-13662082539617429133']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(docs_file, 'r') as f:
    docs_data = json.load(f)

funding_map = {}
for item in funding_data:
    name = item['Project_Name'].strip()
    try:
        amount = float(item['Amount'])
    except:
        amount = 0
    funding_map[name] = amount

projects = []
current_project = None
current_start_date = None

for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check for section start markers
        # We look for "Updates:" or "Project Description:" or "Project Updates:"
        # Avoid specific unicode chars in literal to be safe
        if "Updates:" in line or "Project Description:" in line:
            # Look backwards for project name
            j = i - 1
            found_name = None
            while j >= 0:
                prev = lines[j].strip()
                if prev:
                    found_name = prev
                    break
                j -= 1
            
            if found_name:
                # If we were processing a project, save it
                if current_project:
                    projects.append({'name': current_project, 'start': current_start_date})
                
                current_project = found_name
                current_start_date = None
        
        # Check for start date
        if current_project:
            low_line = line.lower()
            if "begin construction" in low_line:
                parts = line.split(":")
                if len(parts) > 1:
                    date_val = parts[1].strip()
                    if current_start_date is None:
                        current_start_date = date_val

    # Add last project
    if current_project:
        projects.append({'name': current_project, 'start': current_start_date})

# Filter for Spring 2022
target_dates = ["spring 2022", "march 2022", "april 2022", "may 2022"]
matched_projects = []

for p in projects:
    if p['start']:
        s_date = p['start'].lower()
        if any(t in s_date for t in target_dates):
            matched_projects.append(p['name'])

# Calculate funding
total = 0
found_list = []
missing_list = []

for name in matched_projects:
    if name in funding_map:
        total += funding_map[name]
        found_list.append(name)
    else:
        # Retry with fuzzy match (e.g. check if name in db_name or vice versa)
        # This handles cases like "Project X" vs "Project X (FEMA)"
        match_found = False
        for db_name, amt in funding_map.items():
            if name == db_name: # Already checked
                continue
            # Check if one is substring of other (case insensitive)
            if name.lower() in db_name.lower() or db_name.lower() in name.lower():
                # Potential match. Let's assume valid for now if unique.
                # But to be safe, maybe just log it. 
                # Given the problem type, exact match is preferred, but names might differ slightly.
                # The prompt says: "The Project_Name ... matches the project names ... in MongoDB".
                # Let's stick to exact match first.
                pass
        missing_list.append(name)

# If missing list is large, we might have an extraction issue.

result = {
    "count": len(found_list),
    "total_funding": total,
    "projects": found_list,
    "missing": missing_list,
    # "debug_projects": projects[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6849361195335581804': 'file_storage/function-call-6849361195335581804.json', 'var_function-call-6849361195335584623': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13662082539617429622': 'file_storage/function-call-13662082539617429622.json', 'var_function-call-13662082539617429133': 'file_storage/function-call-13662082539617429133.json'}

exec(code, env_args)
