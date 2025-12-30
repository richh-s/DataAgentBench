code = """import json
import re

# Load data
with open(locals()['var_function-call-2424790631309893722'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2424790631309895007'], 'r') as f:
    funding_data = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    # The text uses (cid:190) which is \u00be
    # Split by \u00be
    # The structure is: Name \n\n \u00be ...
    
    parts = re.split(r'\u00be', text)
    
    # parts[0] is header material before first project.
    # parts[i] starts with " Updates:..." or " Project Description:..."
    # The project name should be at the end of parts[i-1]
    
    for i in range(1, len(parts)):
        # details are in parts[i]
        details = parts[i]
        
        # name is at the end of parts[i-1]
        # Get the last non-empty line of parts[i-1]
        prev_chunk = parts[i-1].strip()
        if not prev_chunk:
            continue
            
        lines = prev_chunk.split('\n')
        # Iterate backwards to find the name
        # The name is likely the last non-empty line. 
        # But sometimes there are empty lines or "Capital Improvement Projects (Design)" headers.
        # We need to be careful.
        # Usually, the project name is just one line.
        
        # Let's take the last line that is not a known section header
        # Known headers seen in preview: "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)"
        
        project_name = None
        for line in reversed(lines):
            line = line.strip()
            if not line:
                continue
            if "Capital Improvement Projects" in line:
                continue
            # Also "Agenda Item" or page numbers might be there if the split was bad, but \u00be is usually at the start of a block
            project_name = line
            break
            
        if not project_name:
            continue
            
        # Extract Start Date from details
        # Look for "Begin Construction: <value>" or "Start: <value>"
        # Using (cid:131) which is \u0083 as bullet for sub-items
        
        start_date = None
        # Regex for Begin Construction
        # It might be on a line like "\u0083 Begin Construction: Fall 2023"
        match = re.search(r'Begin Construction:\s*(.*)', details, re.IGNORECASE)
        if match:
            start_date = match.group(1).strip()
        else:
            # Check for "Start:"
            match = re.search(r'Start:\s*(.*)', details, re.IGNORECASE)
            if match:
                start_date = match.group(1).strip()
        
        if start_date:
            projects.append({
                "Project_Name": project_name,
                "Start_Date": start_date
            })

# Filter for Spring 2022
# Spring 2022 = March, April, May 2022 or "Spring 2022"
spring_months = ["March", "April", "May", "Spring"]
target_year = "2022"

target_projects = []
for p in projects:
    sd = p['Start_Date']
    # Check for 2022
    if target_year in sd:
        # Check for month/season
        is_spring = False
        for m in spring_months:
            if m.lower() in sd.lower():
                is_spring = True
                break
        
        # Also need to exclude "Spring 2023" if the year check wasn't specific enough
        # But I checked "2022" in sd.
        # What if "Spring 2023" (contains no 2022)? Correct.
        # What if "March 15, 2022"? Contains March and 2022. Correct.
        
        if is_spring:
            target_projects.append(p)

# Join with Funding
# Prepare funding lookup
# Funding table has Amount (int in schema, but string in JSON result "Amount": "24000")
# I'll sum the amount.

total_funding = 0
matched_projects_count = 0
matched_names = []

# Create a map of Project_Name -> Total Amount (sum if duplicates exist, though schema implies 1 row per funding source, multiple rows per project?)
# The Funding table has Project_Name. Multiple rows can have same Project_Name?
# Yes, e.g. "Birdview Avenue Improvements" appears multiple times with different sources.

funding_map = {} # Project_Name -> Total Amount
for rec in funding_data:
    p_name = rec['Project_Name'].strip()
    amt = int(rec['Amount'])
    if p_name in funding_map:
        funding_map[p_name] += amt
    else:
        funding_map[p_name] = amt

# Now calculate total for target projects
# We need to match names.
# "2022 Morning View Resurfacing & Storm Drain Improvements"
# vs
# "2022 Morning View Resurfacing & Storm Drain Improvements" in funding?

# Let's do exact match first.
found_funding = 0
found_count = 0

# To avoid double counting if multiple docs mention the same project?
# The prompt says "Each document contains descriptions of multiple civic projects".
# If multiple documents mention the same project, we should deduplicate based on name.
unique_target_projects = {} # Name -> StartDate
for p in target_projects:
    unique_target_projects[p['Project_Name']] = p['Start_Date']

for p_name in unique_target_projects:
    # Try exact match
    if p_name in funding_map:
        found_funding += funding_map[p_name]
        found_count += 1
        matched_names.append(p_name)
    else:
        # Try fuzzy match?
        # Maybe the name in doc is "Project A" and in DB is "Project A (FEMA)"?
        # Hint: "Disaster project names often include suffixes like..."
        # So maybe the extracted name is the prefix?
        # Or extracted name has the suffix?
        # Let's check keys in funding_map that start with p_name
        
        # Case 1: Doc name "X", DB name "X (FEMA)"
        # Case 2: Doc name "X (FEMA)", DB name "X"
        
        match_found = False
        for db_name in funding_map:
            # Check if db_name starts with p_name or p_name starts with db_name
            # But be careful.
            if db_name.startswith(p_name) or p_name.startswith(db_name):
                 # This is risky. "Park" starts with "P".
                 # Let's check for containment with some length constraint or exact containment
                 if db_name == p_name:
                     found_funding += funding_map[db_name]
                     match_found = True
                     break
                 # Check specific suffixes mentioned in hints
                 # "(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)"
                 # If db_name has these, strip them and compare?
                 
                 # Let's look at the data. 
                 pass
        
        # If strict match failed, let's print the failed ones to debug.
        pass

print("__RESULT__:")
print(json.dumps({
    "count": found_count,
    "total_funding": found_funding,
    "projects": matched_names,
    "target_projects_extracted": list(unique_target_projects.keys())
}))"""

env_args = {'var_function-call-16991084151717076996': ['civic_docs'], 'var_function-call-16991084151717078539': ['Funding'], 'var_function-call-14749918171882353165': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14749918171882355006': 'file_storage/function-call-14749918171882355006.json', 'var_function-call-2424790631309893722': 'file_storage/function-call-2424790631309893722.json', 'var_function-call-2424790631309895007': 'file_storage/function-call-2424790631309895007.json'}

exec(code, env_args)
