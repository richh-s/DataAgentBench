code = """import json
import re

# Load data
civic_docs_path = locals()['var_function-call-2424790631309893722']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_path = locals()['var_function-call-2424790631309895007']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    # Split by the bullet point used in the document (u00be)
    # We use the unicode codepoint directly to avoid regex string escaping issues
    parts = text.split('\u00be')
    
    for i in range(1, len(parts)):
        details = parts[i]
        prev_chunk = parts[i-1].strip()
        if not prev_chunk:
            continue
            
        lines = prev_chunk.split('\n')
        project_name = None
        
        # Find the project name in the previous chunk
        for line in reversed(lines):
            line = line.strip()
            if not line:
                continue
            if "Capital Improvement Projects" in line:
                continue
            if "Agenda Item" in line:
                continue
            if line.startswith("Page"):
                continue
            # Some cleaning
            if line.endswith(':'):
                line = line[:-1]
            project_name = line
            break
            
        if not project_name:
            continue
            
        # Extract Start Date
        start_date = None
        # Look for "Begin Construction:"
        # We search case-insensitive
        match = re.search(r'Begin Construction:\s*(.*)', details, re.IGNORECASE)
        if match:
            start_date = match.group(1).strip()
        
        if start_date:
            projects.append({
                "Project_Name": project_name,
                "Start_Date": start_date
            })

# Deduplicate
unique_projects = {}
for p in projects:
    unique_projects[p['Project_Name']] = p['Start_Date']

# Filter Spring 2022
spring_months = ["March", "April", "May", "Spring"]
target_year = "2022"

target_project_names = []
for name, sd in unique_projects.items():
    if target_year in sd:
        is_spring = False
        for m in spring_months:
            if m.lower() in sd.lower():
                is_spring = True
                break
        if is_spring:
            target_project_names.append(name)

# Aggregate Funding
funding_map = {}
for rec in funding_data:
    p_name = rec['Project_Name'].strip()
    amt = int(rec['Amount'])
    if p_name in funding_map:
        funding_map[p_name] += amt
    else:
        funding_map[p_name] = amt

found_funding = 0
found_count = 0
matched_list = []
unmatched_list = []

for p_name in target_project_names:
    if p_name in funding_map:
        found_funding += funding_map[p_name]
        found_count += 1
        matched_list.append(p_name)
    else:
        unmatched_list.append(p_name)

print("__RESULT__:")
print(json.dumps({
    "count": found_count,
    "total_funding": found_funding,
    "matched_projects": matched_list,
    "unmatched_projects": unmatched_list
}))"""

env_args = {'var_function-call-16991084151717076996': ['civic_docs'], 'var_function-call-16991084151717078539': ['Funding'], 'var_function-call-14749918171882353165': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14749918171882355006': 'file_storage/function-call-14749918171882355006.json', 'var_function-call-2424790631309893722': 'file_storage/function-call-2424790631309893722.json', 'var_function-call-2424790631309895007': 'file_storage/function-call-2424790631309895007.json'}

exec(code, env_args)
