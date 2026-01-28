code = """import json
import re

# Load data
with open(locals()['var_function-call-6099601671334015320'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-9845122995383564769'], 'r') as f:
    funding_data = json.load(f)

# Extract unique project base names from Funding
# Remove suffixes like (FEMA Project), (CalOES Project), (FEMA/CalOES Project)
def get_base_name(name):
    # Remove text in parentheses at the end if it contains FEMA, CalOES, Project
    # But some might just be (FEMA).
    # Regex to remove ( ... ) at end
    base = re.sub(r'\s*\(.*?(?:FEMA|CalOES|CalJPIA).*?\)$', '', name)
    return base.strip()

funding_projects = set()
for row in funding_data:
    funding_projects.add(get_base_name(row['Project_Name']))

# Helper to find project info in text
project_info = {} # base_name -> {'start_year': None, 'is_disaster': False}

# We need to find where each project is described in the text.
# The text has lines with project names.
# We will iterate through the text lines.
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if line is a project name
        # We fuzzy match against funding_projects
        # Or exact match
        found_project = None
        if line in funding_projects:
            found_project = line
        else:
            # Try matching with simple cleanup
            # Sometimes text has extra spaces or formatting
            # Check if line starts with a year (e.g. 2022 Morning View...)
            # The Funding name might be "Morning View..." or "2022 Morning View..."
            for fp in funding_projects:
                if fp == line or fp in line:
                     # Check if it's a standalone line or header
                     # This is a bit loose, but let's try
                     if len(line) < len(fp) + 10: # avoid matching inside long sentences
                         found_project = fp
                         break
        
        if found_project:
            current_project = found_project
            if current_project not in project_info:
                project_info[current_project] = {'start_year': [], 'keywords': set()}
            continue
            
        if current_project:
            # Analyze line for dates and keywords
            # Keywords for disaster
            keywords = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Emergency", "Fire"]
            for kw in keywords:
                if kw in line or kw.upper() in line.upper():
                    project_info[current_project]['keywords'].add(kw)
            
            # Start dates
            # Patterns: "Begin Construction: [Season] [Year]", "Begin Construction: [Month] [Year]"
            # "Awarded ... [Month] [Year]"
            # "Construction was completed [Month] [Year]"
            
            # Regex for "Begin Construction: <value> 2022"
            # match "Begin Construction" followed by anything then "2022"
            match_start = re.search(r'Begin Construction:.*?(\d{4})', line, re.IGNORECASE)
            if match_start:
                year = int(match_start.group(1))
                project_info[current_project]['start_year'].append(('begin', year))
                
            match_award = re.search(r'Awarded.*?(\d{4})', line, re.IGNORECASE)
            if match_award:
                year = int(match_award.group(1))
                project_info[current_project]['start_year'].append(('award', year))
                
            match_comp = re.search(r'Construction was completed.*?(\d{4})', line, re.IGNORECASE)
            if match_comp:
                year = int(match_comp.group(1))
                project_info[current_project]['start_year'].append(('completed', year))

# Now logic to determine "Started in 2022" and "Disaster"
projects_started_2022 = set()
disaster_projects = set()

for proj, info in project_info.items():
    # Determine if disaster
    is_disaster = False
    if len(info['keywords']) > 0:
        is_disaster = True
    
    # Determine start year
    # If explicit "Begin Construction" is 2022 -> Yes
    # If "Awarded" in 2022 -> Yes (Start of project)
    # If "Completed" in 2022 -> Maybe? 
    #   "Bluffs Park Shade Structure": Completed Nov 2022. Started 2022? 
    #   "Broad Beach Road": Completed Nov 2022.
    #   Usually "Completed Nov 2022" implies it started earlier in 2022 or late 2021.
    #   However, "Started in 2022" is the query. 
    #   If I have to choose, "Begin Construction: 2022" is the strongest signal.
    #   Let's check if any 'begin' or 'award' is 2022.
    
    started_2022 = False
    years = info['start_year']
    for type_, year in years:
        if year == 2022:
            if type_ in ['begin', 'award']:
                started_2022 = True
            # For 'completed', it's ambiguous. But if it's the only info...
            # If completed in Jan 2023 (like Marie Canyon), it likely started in 2022.
            # If completed in Nov 2022, it likely started in 2022.
            # Let's assume if completed in 2022, it started in 2022 (unless it was a multi-year project, but these seem like small repairs).
            # I will include 'completed' in 2022 as 'started in 2022' if no other info.
            if type_ == 'completed':
                started_2022 = True # Optimistic approach based on hints usually simplifying things
    
    if is_disaster:
        disaster_projects.add(proj)
    if started_2022:
        projects_started_2022.add(proj)

# Join with Funding
total_amount = 0
matched_rows = []

for row in funding_data:
    p_name = row['Project_Name']
    base = get_base_name(p_name)
    amount = row['Amount']
    
    # Check if this row is disaster related
    # 1. Name contains disaster keywords
    row_is_disaster = False
    if re.search(r'\(.*?(?:FEMA|CalOES|CalJPIA).*?\)', p_name):
        row_is_disaster = True
    elif base in disaster_projects:
        row_is_disaster = True
        
    # Check if project started in 2022
    # We rely on the base project info
    row_started_2022 = False
    if base in projects_started_2022:
        row_started_2022 = True
    
    # For projects that "Completed in Jan 2023", they likely started in 2022.
    # "Marie Canyon Green Streets": Completed Jan 2023. Start? Likely 2022.
    # Let's add a check: if completed in 2023 (early), start was likely 2022.
    # But for now, rely on explicit 2022 dates found.
    
    if row_is_disaster and row_started_2022:
        total_amount += int(amount)
        matched_rows.append(row)

print("__RESULT__:")
print(json.dumps({"total_funding": total_amount, "matched_projects": [r['Project_Name'] for r in matched_rows], "project_info": str(project_info)}))"""

env_args = {'var_function-call-18312166134834260107': 'file_storage/function-call-18312166134834260107.json', 'var_function-call-6099601671334015320': 'file_storage/function-call-6099601671334015320.json', 'var_function-call-9845122995383564769': 'file_storage/function-call-9845122995383564769.json'}

exec(code, env_args)
