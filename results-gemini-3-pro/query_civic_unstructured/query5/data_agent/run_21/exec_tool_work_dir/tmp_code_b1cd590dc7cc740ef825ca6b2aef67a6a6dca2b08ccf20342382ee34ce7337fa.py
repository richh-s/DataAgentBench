code = """import json
import re

# Load funding data
with open(locals()['var_function-call-1312699190325446696'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-18394559643170776925'], 'r') as f:
    civic_docs = json.load(f)
    text = civic_docs[0]['text'] if civic_docs else ""

# Helper to clean project names (remove suffixes)
def clean_project_name(name):
    # Remove (FEMA...), (CalOES...), (CalJPIA...)
    # Also remove generic endings if needed, but suffixes in parenthesis are the main ones.
    name = re.sub(r'\s*\(FEMA.*?\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES.*?\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA.*?\)', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(.*?\)', '', name) # Remove any other parenthetical info? Maybe risk removing real parts.
    # The hints specific suffixes. Let's be specific first.
    return name.strip()

# Create a mapping of Base Name -> List of Funding Records
# And identify Disaster Base Names
project_funding = {}
disaster_projects = set()

for record in funding_data:
    raw_name = record['Project_Name']
    # Specific cleaning based on hints
    base_name = raw_name
    is_disaster = False
    if 'FEMA' in raw_name or 'CalOES' in raw_name or 'CalJPIA' in raw_name:
        is_disaster = True
    
    # Clean the name to get base
    # Regex to remove the specific suffixes mentioned
    cleaned = re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA).*?\)', '', raw_name, flags=re.IGNORECASE).strip()
    # Also handle combinations like "(FEMA/CalOES Project)" which the regex above handles if 'FEMA' or 'CalOES' is first.
    # Check if cleaned name still has parens?
    # Example: "Birdview Avenue Improvements (FEMA/CalOES Project)" -> "Birdview Avenue Improvements"
    
    if cleaned not in project_funding:
        project_funding[cleaned] = []
    project_funding[cleaned].append(record)
    
    if is_disaster:
        disaster_projects.add(cleaned)

# Now parse the text to find projects and their start dates
# We can identify project blocks by looking for lines that match 'base names'
# or slightly fuzzy matches.
# But exact match on "cleaned" names is best given the hint "matches the project names that can be extracted".

# Get list of all known base names
all_base_names = list(project_funding.keys())

# Sort by length desc to match longest first
all_base_names.sort(key=len, reverse=True)

lines = text.split('\n')
project_info = []
current_project = None
current_text = []

# Naive parsing: find lines that match a project name exactly (or close to it)
# We need to be careful not to match random text.
# Project names in the text seem to be on their own lines.

matched_projects = {}

for i, line in enumerate(lines):
    line_strip = line.strip()
    if not line_strip:
        continue
        
    # Check if this line is a project name
    # It might be followed by "Updates" or similar in next lines
    found_name = None
    if line_strip in all_base_names:
        found_name = line_strip
    else:
        # Check for near match or case insensitive
        for name in all_base_names:
            if line_strip.lower() == name.lower():
                found_name = name
                break
    
    if found_name:
        # Check if it looks like a header (e.g. next line has "Updates" or "Project Description" or "Schedule")
        # Look ahead a few lines
        is_header = False
        for offset in range(1, 6):
            if i + offset < len(lines):
                next_l = lines[i+offset].strip()
                if "Updates" in next_l or "Project Description" in next_l or "Project Schedule" in next_l or "Estimated Schedule" in next_l:
                    is_header = True
                    break
        
        if is_header:
            # Save previous project
            if current_project:
                matched_projects[current_project] = "\n".join(current_text)
            current_project = found_name
            current_text = []
            continue

    if current_project:
        current_text.append(line)

# Save last
if current_project:
    matched_projects[current_project] = "\n".join(current_text)

# Now analyze the extracted text for each project
funding_started_2022 = 0
found_projects_list = []

for name, p_text in matched_projects.items():
    # Check extraction of dates
    # Look for "Begin Construction: <Date>"
    # or "Start Date: <Date>"
    
    # Regex for Begin Construction
    # Matches: "Begin Construction: Fall 2023", "Begin Construction: April 2023"
    start_match = re.search(r'Begin Construction:\s*([A-Za-z0-9\s]+)', p_text, re.IGNORECASE)
    start_date = start_match.group(1).strip() if start_match else None
    
    # Check if started in 2022
    started_2022 = False
    if start_date:
        if "2022" in start_date:
            started_2022 = True
    
    # What if "Construction was completed November 2022"?
    # If the text says "Construction was completed...", did it start in 2022?
    # Hint: "Dates (st, et fields) use flexible formats..."
    # If I find "Construction began: ..." or similar?
    # Let's search for "began" or "started"
    if not started_2022:
        began_match = re.search(r'(?:began|started).*?(\d{4})', p_text, re.IGNORECASE)
        if began_match:
            year = began_match.group(1)
            if year == "2022":
                started_2022 = True
    
    # Check if disaster
    # 1. Is it in disaster_projects set?
    # 2. Does text contain keywords?
    is_disaster = False
    if name in disaster_projects:
        is_disaster = True
    else:
        # Check keywords
        if re.search(r'(FEMA|CalOES|CalJPIA|Disaster|Woolsey)', p_text, re.IGNORECASE):
            is_disaster = True
            
    if started_2022 and is_disaster:
        # Calculate funding
        # Sum all records for this base name
        total = 0
        records = project_funding.get(name, [])
        for r in records:
            total += int(r['Amount'])
        funding_started_2022 += total
        found_projects_list.append({
            "name": name,
            "start_date": start_date,
            "amount": total
        })

print("__RESULT__:")
print(json.dumps(found_projects_list))"""

env_args = {'var_function-call-7116383370985667147': ['Funding'], 'var_function-call-7116383370985666072': 'file_storage/function-call-7116383370985666072.json', 'var_function-call-1312699190325446696': 'file_storage/function-call-1312699190325446696.json', 'var_function-call-18394559643170776925': 'file_storage/function-call-18394559643170776925.json'}

exec(code, env_args)
