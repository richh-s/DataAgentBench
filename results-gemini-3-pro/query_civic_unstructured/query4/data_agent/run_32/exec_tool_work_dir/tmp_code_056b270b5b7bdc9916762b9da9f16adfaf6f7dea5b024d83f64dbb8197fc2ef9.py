code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-12378432267433041329'], 'r') as f:
    civic_docs = json.load(f)

# Load Funding table
funding_data = locals()['var_function-call-7193024232373872920']
# funding_data is a list of dicts.

# Prepare Funding dict
funding_map = {} 
for row in funding_data:
    funding_map[row['Project_Name']] = int(row['Amount'])

spring_months = ['march', 'april', 'may']

def is_spring_2022(date_str):
    ds = date_str.lower()
    if 'spring 2022' in ds or 'spring, 2022' in ds:
        return True
    if '2022' in ds:
        for m in spring_months:
            if m in ds:
                return True
        # Check numerical dates
        if re.search(r'(03|04|05)[/-].*2022', ds):
            return True
        if re.search(r'2022.*(03|04|05)', ds):
            return True
    return False

projects_started_spring_2022 = set()
debug_dates = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    lines = [l.strip() for l in lines]
    
    current_project = None
    
    for i, line in enumerate(lines):
        if not line:
            continue
            
        is_project_header = False
        # Check if next line starts with (cid:190)
        # We need to look ahead, skipping empty lines? 
        # I already stripped empty lines from list? No, I did `[l.strip() for l in lines]`.
        # Some elements might be empty strings now.
        
        # Let's clean the list of lines to remove empty ones for easier processing?
        # But context matters.
        
        # Check ahead
        found_bullet = False
        for k in range(i+1, min(i+5, len(lines))):
            if lines[k].startswith('(cid:190)') or lines[k].startswith('Updates:') or lines[k].startswith('Project Description:'):
                found_bullet = True
                break
            if lines[k]: # Found a non-empty line that isn't a bullet
                break
        
        if found_bullet and "capital improvement projects" not in line.lower() and "updates:" not in line.lower():
            is_project_header = True

        if is_project_header:
            current_project = line
            continue
        
        if current_project:
            # Check for "Begin Construction: ..."
            match = re.search(r'begin construction[:\s]+(.*)', line, re.IGNORECASE)
            if match:
                val = match.group(1)
                if is_spring_2022(val):
                    projects_started_spring_2022.add(current_project)
                    debug_dates.append((current_project, val))
            
            # Check for "Start Date: ..."
            match = re.search(r'start date[:\s]+(.*)', line, re.IGNORECASE)
            if match:
                val = match.group(1)
                if is_spring_2022(val):
                    projects_started_spring_2022.add(current_project)
                    debug_dates.append((current_project, val))

            if "construction started" in line.lower() or "construction began" in line.lower():
                 if is_spring_2022(line):
                     projects_started_spring_2022.add(current_project)
                     debug_dates.append((current_project, line))

# Match with funding
found_projects = []
total_funding = 0
matched_projects = set()

for p_name in projects_started_spring_2022:
    if p_name in matched_projects:
        continue
        
    matched = False
    # Exact match
    if p_name in funding_map:
        found_projects.append(p_name)
        total_funding += funding_map[p_name]
        matched = True
    else:
        # Case insensitive
        for k in funding_map:
            if k.lower() == p_name.lower():
                found_projects.append(k)
                total_funding += funding_map[k]
                matched = True
                break
    
    if matched:
        matched_projects.add(p_name)

result = {
    "count": len(found_projects),
    "total_funding": total_funding,
    "projects": found_projects,
    "debug_dates": debug_dates
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9316415891576363491': ['Funding'], 'var_function-call-9316415891576362210': ['civic_docs'], 'var_function-call-10848218127933448238': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-10848218127933449745': 'file_storage/function-call-10848218127933449745.json', 'var_function-call-12378432267433041329': 'file_storage/function-call-12378432267433041329.json', 'var_function-call-7193024232373872920': 'file_storage/function-call-7193024232373872920.json'}

exec(code, env_args)
