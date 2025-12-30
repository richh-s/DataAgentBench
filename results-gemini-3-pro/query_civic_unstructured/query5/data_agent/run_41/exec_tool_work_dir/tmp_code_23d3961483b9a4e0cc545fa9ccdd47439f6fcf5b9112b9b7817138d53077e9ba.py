code = """import json
import pandas as pd
import re

# Load data
funding_path = locals()['var_function-call-14443830636332700640']
docs_path = locals()['var_function-call-14443830636332701107']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    docs_data = json.load(f)

# Create DataFrame for Funding
df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = df_funding['Amount'].astype(float)

# Extract unique project names from Funding to help parsing
# We also create a mapping of "Base Name" -> List of Funding Records
# Base Name logic: remove (...) suffixes
def get_base_name(name):
    # Remove (FEMA...), (CalOES...), etc.
    # Pattern: Space + ( + text containing FEMA/CalOES/CalJPIA + )
    # Also handle simpler cases or just strip all parens if appropriate?
    # The hint says suffixes are like "(FEMA Project)".
    # Let's try to strip any suffix in parenthesis at the end of the string
    base = re.sub(r'\s*\(.*?\)$', '', name)
    return base.strip()

project_map = {}
for _, row in df_funding.iterrows():
    full_name = row['Project_Name']
    base_name = get_base_name(full_name)
    if base_name not in project_map:
        project_map[base_name] = []
    project_map[base_name].append(row)

# Also keep a set of all full names for exact matching
all_project_names = set(df_funding['Project_Name'].tolist())
base_project_names = set(project_map.keys())

# Parsing logic
found_projects = []

def parse_date(line):
    # return year if found
    match = re.search(r'20\d\d', line)
    if match:
        return match.group(0)
    return None

def is_disaster_text(text_block):
    keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Woolsey', 'Fire', 'Disaster', 'Emergency']
    for k in keywords:
        if k.lower() in text_block.lower():
            return True
    return False

# We will iterate through the text and try to identify chunks belonging to a project.
# A project header is likely a line that matches a Base Project Name.
# Since text is unstructured, we'll iterate line by line.

extracted_projects = []

for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    current_block = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Check if line is a project name
        # We check against base_project_names
        # We need to be careful about false positives (e.g. "Public Works")
        # But project names are usually specific.
        
        # Exact match or close match?
        # The line might have extra chars or casing issues.
        # Let's assume the project name is on a line by itself or close to it.
        
        is_new_project = False
        matched_name = None
        
        if line in base_project_names:
            is_new_project = True
            matched_name = line
        elif line in all_project_names:
            is_new_project = True
            matched_name = get_base_name(line)
        else:
            # Try to see if the line starts with a project name (sometimes there's noise)
            # Or fuzzy match?
            # Let's check if any base name is in the line (and line isn't too long)
            if len(line) < 100:
                for bn in base_project_names:
                    # strict check: line must be equal to bn or bn + some suffix?
                    # The preview showed headers exactly matching names.
                    if line == bn:
                        is_new_project = True
                        matched_name = bn
                        break
        
        if is_new_project:
            # Save previous project
            if current_project:
                extracted_projects.append({
                    'name': current_project,
                    'block': "\n".join(current_block)
                })
            current_project = matched_name
            current_block = []
        else:
            if current_project:
                current_block.append(line)
    
    # Add last project
    if current_project:
        extracted_projects.append({
            'name': current_project,
            'block': "\n".join(current_block)
        })

# Now analyze extracted projects
final_project_list = []

for p in extracted_projects:
    name = p['name']
    block = p['block']
    
    # 1. Determine Start Date
    # Look for "Begin Construction", "Start", "Advertise"
    start_year = None
    
    # Prioritize "Begin Construction"
    bc_match = re.search(r'Begin [Cc]onstruction:?\s*([A-Za-z0-9 ]+)', block, re.IGNORECASE)
    if bc_match:
        date_str = bc_match.group(1)
        start_year = parse_date(date_str)
    
    if not start_year:
        # Check "Advertise"
        adv_match = re.search(r'Advertise:?\s*([A-Za-z0-9 ]+)', block, re.IGNORECASE)
        if adv_match:
            date_str = adv_match.group(1)
            start_year = parse_date(date_str)
            
    if not start_year:
        # Check "Construction was completed" - implies start was earlier?
        # "Construction was completed, November 2022" -> Start might be 2022.
        # Let's be careful. If it completed in 2022, it was active in 2022.
        # Does "started in 2022" mean the *start event* was in 2022?
        # Usually yes.
        # But if we miss the start date, we might miss a valid project.
        # Let's look for "Updates: Construction began..." or similar.
        # For now, stick to explicit start markers.
        pass
        
    # 2. Determine if Disaster Related
    is_disaster = is_disaster_text(block)
    
    # Also check if any funding source for this base name suggests disaster
    # (e.g. if Funding table has "Name (FEMA Project)")
    has_disaster_funding_record = False
    funding_records = project_map.get(name, [])
    for rec in funding_records:
        if 'FEMA' in rec['Project_Name'] or 'CalOES' in rec['Project_Name'] or 'CalJPIA' in rec['Project_Name']:
            has_disaster_funding_record = True
            break
            
    # Also check extracted Topic? (Not extracting topic explicitly but searching keywords in block)
    
    final_project_list.append({
        'name': name,
        'start_year': start_year,
        'is_disaster': is_disaster or has_disaster_funding_record,
        'funding_records': funding_records
    })

# Filter
projects_started_2022 = []
for p in final_project_list:
    if p['start_year'] == '2022' and p['is_disaster']:
        projects_started_2022.append(p)

# Sum Funding
total_funding = 0.0
# We need to avoid double counting if the same project appears in multiple docs?
# Or multiple times in one doc?
# The list `projects_started_2022` might have duplicates if found in multiple files.
# We should collect unique Project Names (Base Names) that satisfy the condition.

unique_qualified_projects = set()
for p in projects_started_2022:
    unique_qualified_projects.add(p['name'])

# Calculate sum for these unique projects
# We sum ALL funding records associated with the base name (including variants)
# assuming all variants belong to the same project.

funding_details = []
for name in unique_qualified_projects:
    records = project_map.get(name, [])
    for r in records:
        total_funding += r['Amount']
        funding_details.append(r)

result = {
    "total_funding": total_funding,
    "projects": list(unique_qualified_projects),
    "funding_details_count": len(funding_details)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14443830636332701107': 'file_storage/function-call-14443830636332701107.json', 'var_function-call-14443830636332700640': 'file_storage/function-call-14443830636332700640.json'}

exec(code, env_args)
