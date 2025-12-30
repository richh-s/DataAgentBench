code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-12378432267433041329'], 'r') as f:
    civic_docs = json.load(f)

# Load Funding table
funding_data = locals()['var_function-call-7193024232373872920']

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
    lines = text.splitlines()
    lines = [l.strip() for l in lines]
    
    current_project = None
    
    for i, line in enumerate(lines):
        if not line:
            continue
            
        is_project_header = False
        # Look ahead for bullet
        found_bullet = False
        limit = min(i+5, len(lines))
        for k in range(i+1, limit):
            l_k = lines[k]
            if l_k.startswith('(cid:190)') or l_k.startswith('Updates:') or l_k.startswith('Project Description:'):
                found_bullet = True
                break
            if l_k: 
                break
        
        if found_bullet:
             lower_line = line.lower()
             if "capital improvement projects" not in lower_line and "updates:" not in lower_line and "agenda item" not in lower_line:
                is_project_header = True

        if is_project_header:
            current_project = line
            continue
        
        if current_project:
            # Check for "Begin Construction: ..."
            # Regex: begin construction[:\s]+(.*)
            # Escaped: begin construction[:\\s]+(.*)
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
    if p_name in funding_map:
        found_projects.append(p_name)
        total_funding += funding_map[p_name]
        matched = True
    else:
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
