code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-12378432267433041329'], 'r') as f:
    civic_docs = json.load(f)

# Load Funding table
with open(locals()['var_function-call-7193024232373872920'], 'r') as f:
    funding_data = json.load(f)

# Prepare Funding names
# We want to match text lines to these names.
funding_map = {row['Project_Name']: int(row['Amount']) for row in funding_data}
funding_names = sorted(funding_map.keys(), key=len, reverse=True)

spring_months = ['march', 'april', 'may']

def is_spring_2022(date_str):
    ds = date_str.lower()
    if 'spring 2022' in ds or 'spring, 2022' in ds:
        return True
    if '2022' in ds:
        for m in spring_months:
            if m in ds:
                return True
        if re.search(r'(03|04|05)[/-].*2022', ds):
            return True
        if re.search(r'2022.*(03|04|05)', ds):
            return True
    return False

projects_started_spring_2022 = set()
debug_info = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    lines = [l.strip() for l in lines]
    
    current_project = None
    
    for line in lines:
        if not line:
            continue
            
        # Check for project name match
        # We check if the line *contains* the project name, or is equal.
        # Given headers are usually standalone, "equal" or "starts with" is best.
        # But headers might be "Project Name - Update".
        
        matched_name = None
        for name in funding_names:
            if name.lower() in line.lower():
                # Check if the line is not too long (avoid matching name in a sentence)
                if len(line) < len(name) + 20: 
                    matched_name = name
                    break
        
        if matched_name:
            current_project = matched_name
            # Don't continue, checking for date in the same line is possible (rare for header)
        
        if current_project:
            # Look for start indicators
            # 1. "Begin Construction: ..."
            match = re.search(r'begin construction[:\s]+(.*)', line, re.IGNORECASE)
            if match:
                val = match.group(1)
                if is_spring_2022(val):
                    projects_started_spring_2022.add(current_project)
                    debug_info.append((current_project, "Begin Construction", val))

            # 2. "Construction started..."
            if "construction started" in line.lower() or "construction began" in line.lower():
                # Check if the date is in the line
                if is_spring_2022(line):
                    projects_started_spring_2022.add(current_project)
                    debug_info.append((current_project, "Construction started sentence", line))
            
            # 3. "Start Date: ..."
            match = re.search(r'start date[:\s]+(.*)', line, re.IGNORECASE)
            if match:
                val = match.group(1)
                if is_spring_2022(val):
                    projects_started_spring_2022.add(current_project)
                    debug_info.append((current_project, "Start Date", val))

            # 4. Check for just "Spring 2022" in "Project Schedule" section?
            # Too risky without context.

# Calculate totals
found_projects = list(projects_started_spring_2022)
total_funding = 0
for p in found_projects:
    total_funding += funding_map[p]

result = {
    "count": len(found_projects),
    "total_funding": total_funding,
    "projects": found_projects,
    "debug_info": debug_info
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9316415891576363491': ['Funding'], 'var_function-call-9316415891576362210': ['civic_docs'], 'var_function-call-10848218127933448238': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-10848218127933449745': 'file_storage/function-call-10848218127933449745.json', 'var_function-call-12378432267433041329': 'file_storage/function-call-12378432267433041329.json', 'var_function-call-7193024232373872920': 'file_storage/function-call-7193024232373872920.json', 'var_function-call-17452987613193022478': {'count': 0, 'total_funding': 0, 'projects': [], 'debug_dates': [['advertised for construction bids shortly after this date.', 'Spring 2022'], ['sending this project out to bid during the Spring of 2022.', 'Spring 2022'], ['is finalizing the bid documents.', 'Spring 2022'], ['timber with non-combustible materials.', 'April 2022'], ['(cid:131) The project consultant has started the design of this project.', 'Spring 2022'], ['(cid:131) The project consultant has started the design of this project.', 'Spring 2022'], ['beginning in April 2022.', 'April 2022'], ['assessment district will be created.', 'March 2022'], ['that was damaged by the Woolsey Fire.', 'Spring 2022'], ['Fire.', 'Spring 2022'], ['(cid:131) Next public community meeting is scheduled for March 25th.', 'March 2022'], ['that was damaged by the Woolsey Fire.', 'Spring 2022'], ['Fire.', 'Spring 2022'], ['scheduled for the April 11, 2022 Council meeting.', 'Spring 2022'], ['timber with non-combustible materials.', 'Spring 2022'], ['beginning in Spring 2022.', 'Spring 2022']]}}

exec(code, env_args)
