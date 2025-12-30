code = """import json
import re

# Load data
funding_file = locals()['var_function-call-13662082539617429622']
docs_file = locals()['var_function-call-13662082539617429133']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(docs_file, 'r') as f:
    docs_data = json.load(f)

# Create Funding Lookup
# Normalize project names: strip, maybe lowercase?
# The matching says "The Project_Name in the Funding SQLite table matches the project names that can be extracted from the civic documents".
# So exact match or simple stripped match should work.
funding_map = {}
for item in funding_data:
    name = item['Project_Name'].strip()
    amount = float(item['Amount']) # Amount is int/string in DB
    funding_map[name] = amount

# Extract Projects from Text
# Heuristic:
# 1. Split by lines.
# 2. Identify Project Name: A line followed shortly by "(cid:190) Updates:" or "(cid:190) Project Description:" or "(cid:190) Project Updates:".
# 3. Identify Start Date: Look for "Begin Construction: <Date>" inside the project block.
#    Project block ends at the next Project Name.

projects = []
current_project = None
current_start_date = None

# We need to process all documents
for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    # Iterate lines to find projects
    # We'll use a sliding window or index to check ahead
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if this line is a project marker (Updates/Description)
        # The preview shows markers like "(cid:190) Updates:" or "(cid:190) Project Description:"
        # In unicode, (cid:190) might be something else, but in the string it appears as text "(cid:190)" or similar.
        # Let's check for "Updates:" or "Project Description:" preceded by special chars or just at start.
        
        is_marker = False
        if "Updates:" in line or "Project Description:" in line or "Project Updates:" in line:
            # Check if it has the bullet point logic or looks like a section header
            # In the preview: "(cid:190) Updates:"
            if line.startswith("(cid:190)") or "Updates:" in line: 
                is_marker = True
        
        if is_marker:
            # Then the previous non-empty line was likely the project name
            # Let's find it
            j = i - 1
            while j >= 0:
                prev_line = lines[j].strip()
                if prev_line:
                    # found the potential name
                    # If we were already tracking a project, save it
                    if current_project:
                        projects.append({'name': current_project, 'start': current_start_date})
                    
                    current_project = prev_line
                    current_start_date = None
                    break
                j -= 1
        
        # Extract Date if we are in a project
        if current_project:
            # Look for "Begin Construction" or "Start Construction" or "Advertise" if that is the start
            # The query asks for "projects started". 
            # I'll look for "Begin Construction: <Date>"
            
            # Normalize line for checking
            lower_line = line.lower()
            if "begin construction" in lower_line:
                # Extract the date part
                # Format: "Begin Construction: Fall 2023"
                parts = line.split(":")
                if len(parts) > 1:
                    date_str = parts[-1].strip()
                    # Store only the first one found for the project? Or overwrite? 
                    # Usually there is one schedule.
                    if current_start_date is None:
                        current_start_date = date_str
    
    # Append the last project of the doc
    if current_project:
        projects.append({'name': current_project, 'start': current_start_date})

# Filter Projects started in Spring 2022
# Spring 2022 = "Spring 2022", "March 2022", "April 2022", "May 2022"
target_dates = ["Spring 2022", "March 2022", "April 2022", "May 2022"]

matched_projects = []
for p in projects:
    if p['start']:
        # Check if any target date string is in the start date (case insensitive)
        s = p['start'].lower()
        if "spring 2022" in s or "march 2022" in s or "april 2022" in s or "may 2022" in s:
            matched_projects.append(p['name'])
            
# Calculate Total Funding
total_funding = 0
found_projects = []
missing_projects = []

for pname in matched_projects:
    # Try to find in funding_map
    # Exact match?
    if pname in funding_map:
        total_funding += funding_map[pname]
        found_projects.append(pname)
    else:
        # Try fuzzy match or check if suffix matches
        # The prompt says names match.
        # But let's check for simple mismatches
        # Maybe the extracted name has extra spaces?
        found = False
        for db_name in funding_map:
            if db_name in pname or pname in db_name:
                # Use the DB amount? Be careful of partial matches.
                # If exact match failed, this is risky.
                # Let's rely on exact match first.
                pass
        missing_projects.append(pname)

# If we have missing projects, we might need to be smarter. 
# But let's print the result first.

print("__RESULT__:")
print(json.dumps({
    "count": len(found_projects),
    "total_funding": total_funding,
    "projects": found_projects,
    "missing": missing_projects, 
    "all_extracted": projects
}))"""

env_args = {'var_function-call-6849361195335581804': 'file_storage/function-call-6849361195335581804.json', 'var_function-call-6849361195335584623': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-13662082539617429622': 'file_storage/function-call-13662082539617429622.json', 'var_function-call-13662082539617429133': 'file_storage/function-call-13662082539617429133.json'}

exec(code, env_args)
