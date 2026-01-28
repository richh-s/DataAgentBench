code = """import json
import re

# Load data
funding_path = locals()['var_function-call-1630870777495368104']
docs_path = locals()['var_function-call-1630870777495368997']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(docs_path, 'r') as f:
    docs_data = json.load(f)

full_text = chr(10).join([d['text'] for d in docs_data])

# Filter and prepare projects
junk_names = ["Discussion", "Recommended Action", "General Public Comment", "Staff Report"]
projects = []
for row in funding_data:
    if row['Project_Name'] not in junk_names:
        projects.append({
            'name': row['Project_Name'],
            'amount': float(row['Amount']),
            'id': row['Funding_ID']
        })

# Find all matches for all projects
# matches = list of (start, end, project_index)
all_matches = []
for i, p in enumerate(projects):
    name = p['name']
    # Exact match
    for m in re.finditer(re.escape(name), full_text, re.IGNORECASE):
        all_matches.append((m.start(), m.end(), i))
    
    # Root match if suffix exists
    # If name has suffix, also look for root?
    # Actually, relying on exact match of the Funding Name is safer to distinguish variants.
    # But if the text only contains the root name, we might miss the "FEMA" funding record.
    # However, if the text only has the root name, how can we be sure it refers to the FEMA funding slice?
    # Maybe the FEMA funding slice *requires* the FEMA project name to be used?
    # Or maybe the text describes the project generally, and ALL funding slices apply.
    # Let's add root matches for suffixed projects, BUT map them to the suffixed project.
    if "(" in name and ")" in name:
        root = re.sub(r"\s*\(.*?\)$", "", name)
        if len(root) > 5 and root != name:
             for m in re.finditer(re.escape(root), full_text, re.IGNORECASE):
                 all_matches.append((m.start(), m.end(), i))

# Sort matches by start position
all_matches.sort(key=lambda x: x[0])

# Determine valid projects
total_funding = 0.0
valid_projects = set() # ids
matched_details = []

disaster_suffixes = ["(FEMA Project)", "(CalJPIA Project)", "(CalOES Project)", "(FEMA)", "(CalOES)"]
disaster_keywords = ["FEMA", "CalOES", "Woolsey Fire", "Disaster", "Emergency", "CalJPIA"]
start_indicators = ["Begin Construction", "Start Construction", "Advertise", "Awarded", "Bids", "Project Schedule", "Start Date", "Notice to Proceed", "Construction Start"]

for k, (start, end, p_idx) in enumerate(all_matches):
    p = projects[p_idx]
    
    # Determine context boundary
    # End at the start of the next match that is NOT the same project (or a subset/superset at same pos)
    # Actually, simpler: End at the start of the next match in the list, 
    # provided the next match starts significantly after this one (e.g. > 5 chars) to avoid overlapping variations.
    
    next_start = len(full_text)
    for j in range(k + 1, len(all_matches)):
        m_start = all_matches[j][0]
        if m_start > start + 5: # Next distinct match
            next_start = m_start
            break
            
    # Limit context to say 1500 chars to avoid reading too far if no next match
    limit = min(next_start, end + 1500)
    context = full_text[end:limit]
    
    # Check Disaster
    name_is_disaster = any(s in p['name'] for s in disaster_suffixes)
    context_is_disaster = any(kw.lower() in context.lower() for kw in disaster_keywords)
    
    if not (name_is_disaster or context_is_disaster):
        continue
        
    # Check Start 2022
    # Check lines
    is_started_2022 = False
    lines = context.split(chr(10))
    for line in lines:
        if "2022" in line:
            if any(ind in line for ind in start_indicators):
                is_started_2022 = True
                break
            if "received" in line.lower() and "bids" in line.lower():
                is_started_2022 = True
                break
            # Also check for "Construction was completed ... 2022" logic? 
            # If completed in 2022, it might not have started in 2022.
            # But "Projects that started in 2022". 
            # If I stick to strictly "start" indicators, I am safer.
            
    if is_started_2022:
        if p['id'] not in valid_projects:
            valid_projects.add(p['id'])
            total_funding += p['amount']
            matched_details.append({'name': p['name'], 'amount': p['amount']})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'matches': matched_projects})) # matched_details"""

env_args = {'var_function-call-1630870777495368104': 'file_storage/function-call-1630870777495368104.json', 'var_function-call-1630870777495368997': 'file_storage/function-call-1630870777495368997.json', 'var_function-call-9795375164875002863': {'total_funding': 1354000.0, 'matches': [{'name': '2021 Annual Street Maintenance', 'amount': 24000.0}, {'name': 'Annual Street Maintenance', 'amount': 23000.0}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'amount': 87000.0}, {'name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'amount': 81000.0}, {'name': 'Clover Heights Storm Drain', 'amount': 53000.0}, {'name': 'Clover Heights Storm Drain (FEMA Project)', 'amount': 21000.0}, {'name': 'Corral Canyon Culvert Repairs', 'amount': 54000.0}, {'name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'amount': 15000.0}, {'name': 'Corral Canyon Road Bridge Repairs', 'amount': 68000.0}, {'name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'amount': 58000.0}, {'name': 'Encinal Canyon Road Drainage Improvements', 'amount': 34000.0}, {'name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'amount': 18000.0}, {'name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'amount': 94000.0}, {'name': 'Latigo Canyon Road Culvert Repairs', 'amount': 57000.0}, {'name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'amount': 36000.0}, {'name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'amount': 44000.0}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'amount': 19000.0}, {'name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'amount': 91000.0}, {'name': 'Malibu Road Slope Repairs', 'amount': 44000.0}, {'name': 'Malibu Road Slope Repairs (CalOES Project)', 'amount': 37000.0}, {'name': 'Recommended Action', 'amount': 86000.0}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'amount': 78000.0}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'amount': 44000.0}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'amount': 68000.0}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'amount': 43000.0}, {'name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'amount': 77000.0}]}, 'var_function-call-1943388607922845221': [{'Project_Name': 'Discussion'}, {'Project_Name': 'Recommended Action'}]}

exec(code, env_args)
